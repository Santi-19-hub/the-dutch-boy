import pytest
import time
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="function")
def client():
    """Cliente de pruebas síncrono nativo de FastAPI."""
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="function")
def auth_headers(client):
    """Registra un usuario, inicia sesión y devuelve el token en los headers."""
    timestamp = int(time.time())
    username = f"user_auth_{timestamp}"
    email = f"email_auth_{timestamp}@gmail.com"
    password = "password123"
    
    client.post("/auth/register", json={
        "username": username,
        "email": email,
        "password": password
    })
    
    login_resp = client.post("/auth/login", json={
        "username": username,
        "password": password
    })
    
    
    token = login_resp.json().get("access_token") or login_resp.json().get("token")
    
    return {"Authorization": f"Bearer {token}"}