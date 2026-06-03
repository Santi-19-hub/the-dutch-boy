from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Recibe un string limpio y lo encripta usando Bcrypt."""
    clean_password = str(password)
    return pwd_context.hash(clean_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si una contraseña en texto plano coincide con el hash guardado."""
    return pwd_context.verify(str(plain_password), hashed_password)