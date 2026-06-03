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