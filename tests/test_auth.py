# tests/test_auth.py - Basic authentication tests
def test_register_user(client, sample_user):
    """Test user registration."""
    response = client.post("/api/auth/signup", json=sample_user)
    # Adjust status code based on your actual API
    assert response.status_code in [200, 201]
    data = response.json()

    assert data["email"] == sample_user["email"]


def test_login_user(client, sample_user):
    """Test user login."""
    # Register first - IMPORTANT: Each test gets clean database
    register_response = client.post("/api/auth/signup", json=sample_user)
    assert register_response.status_code in [200, 201]
    
    # Now login with the user we just created
    response = client.post("/api/auth/login", json={
        "email": sample_user["email"],
        "password": sample_user["password"]
    })
    
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_invalid_credentials(client,sample_user):
    """Test user login."""
    # Register first - IMPORTANT: Each test gets clean database
    register_response = client.post("/api/auth/signup", json=sample_user)
    assert register_response.status_code in [200, 201]
    
    # Now login with the user we just created

    """Test login with wrong credentials."""
    response = client.post("/api/auth/login", json={
        "email": "wrong@example.com",
        "password": "wrongpass"
    })
    
    assert response.status_code == 401