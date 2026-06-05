import pytest
import time

def test_register_user_success(client):
    """Prueba que un usuario se pueda registrar exitosamente con datos válidos."""
    timestamp = int(time.time())
    payload = {
        "username": f"user_{timestamp}",
        "email": f"user_{timestamp}@gmail.com",
        "password": "password123"  
    }
    
    response = client.post("/auth/register", json=payload)
    
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_register_user_duplicate_email(client):
    """Prueba que el sistema rechace un registro si el correo ya existe."""
    timestamp = int(time.time())
    email_repetido = f"duplicado_{timestamp}@gmail.com"
    
    payload1 = {
        "username": f"user1_{timestamp}",
        "email": email_repetido,
        "password": "password123"
    }
    payload2 = {
        "username": f"user2_{timestamp}",
        "email": email_repetido,
        "password": "password123"
    }
    resp1 = client.post("/auth/register", json=payload1)
    assert resp1.status_code == 200
    
    resp2 = client.post("/auth/register", json=payload2)
    

    assert resp2.status_code == 400
    assert "ya se encuentra registrado" in resp2.json()["detail"]