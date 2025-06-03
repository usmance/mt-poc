# tests/conftest.py - Simple test setup
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
os.environ["TESTING"] = "1"

from main import app
from db.session import get_db, Base 
# Use SQLite for simple testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override database for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture
def client():
    """Create test client."""
    # Create test database
    Base.metadata.create_all(bind=engine)
    
    # Override database dependency
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    # Cleanup
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_user():
    """Sample user data for testing."""
    return {
        "email": "test@example.com",
        "password": "testpass123",
        "organization_id":"0",
        "role":"manager"

    }

@pytest.fixture
def auth_token(client, sample_user):
    """Get auth token for protected endpoints."""
    # Register user
    client.post("/api/auth/signup", json=sample_user)
    print("First signup done")
    # Login to get token
    login_response = client.post("/api/auth/login", json={
        "email": sample_user["email"],
        "password": sample_user["password"]
    })
    
    if login_response.status_code == 200:
        token = login_response.json()["token"]
        return {"Authorization": f"Bearer {token}"}
    return {}