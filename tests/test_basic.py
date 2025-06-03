
# tests/test_basic.py - Basic API health tests
def test_app_starts(client):
    """Test that the app starts and responds."""
    # Test root endpoint or health check
    response = client.get("/")
    
    # App should respond (even if it's 404, it means app is running)
    assert response.status_code in [200, 404]

def test_api_docs_available(client):
    """Test that API docs are accessible."""
    response = client.get("/docs")
    
    # Should return the Swagger UI
    assert response.status_code == 200