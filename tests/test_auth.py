import pytest
import time

def test_register_user_success(client):
    """Prueba que un usuario se pueda registrar exitosamente."""
    timestamp = int(time.time())
    payload = {
        "username": f"user_{timestamp}",
        "email": f"user_{timestamp}@gmail.com",
        "password": "password123"  
    }
    
    response = client.post("/auth/register", json=payload)
    
    if response.status_code != 200:
        pytest.fail(f"Fallo test exitoso. Status: {response.status_code}, Detalle: {response.text}")
        
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_register_user_duplicate_email(client):
    """Prueba que el sistema rechace un registro si el email ya existe."""
    timestamp = int(time.time())
    unique_email = f"duplicate_{timestamp}@gmail.com"
    
    payload1 = {
        "username": f"uniq1_{timestamp}",
        "email": unique_email,
        "password": "password123"
    }
    first_resp = client.post("/auth/register", json=payload1)
    assert first_resp.status_code == 200
    
    payload2 = {
        "username": f"uniq2_{timestamp}",
        "email": unique_email,
        "password": "password123"
    }
    second_resp = client.post("/auth/register", json=payload2)
    
    assert second_resp.status_code == 400