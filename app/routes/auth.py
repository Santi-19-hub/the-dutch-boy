from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
import mysql.connector
from app.core.security import get_password_hash
from app.db.connection import insert_user

router = APIRouter(prefix="/auth", tags=["Autenticación"])

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post("/register", summary="Registrar un nuevo usuario")
def register_user(user_data: UserRegister):
    try:
        
        raw_password = user_data.password
        hashed_pwd = get_password_hash(raw_password)
        
        
        insert_user(user_data.username, user_data.email, hashed_pwd)
        return {"status": "success", "message": "Usuario registrado exitosamente en MySQL"}
        
    except mysql.connector.Error as err:
        if err.errno == 1062:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya se encuentra registrado."
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos: {err.msg}"
        )
    except ValueError as val_err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error en el formato de los datos: {str(val_err)}"
        )
        
from app.core.security import verify_password
from app.db.connection import get_db_connection  # Asegúrate de usar el nombre exacto de tu función de conexión

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login", summary="Iniciar sesión y obtener token")
def login_user(login_data: UserLogin):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        
        cursor.execute("SELECT * FROM users WHERE username = %s", (login_data.username,))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        
        if not user or not verify_password(login_data.password, user["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas"
            )
            
        
        return {
            "access_token": f"token_estatico_para_tests_{user['username']}",
            "token_type": "bearer",
            "status": "success"
        }
        
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos en el login: {err.msg}"
        )