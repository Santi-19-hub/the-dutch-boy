import mysql.connector

def get_db_connection():
    """Establece la conexión con la base de datos MySQL en XAMPP."""
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="",
        database="globalsettler_db"
    )

def init_db():
    """Inicializa la base de datos creando las tablas si no existen."""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount_cop REAL NOT NULL,
            exchange_rate REAL NOT NULL,
            total_usd REAL NOT NULL,
            target_currency VARCHAR(10) NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    c.close()
    conn.close()

def insert_user(username: str, email: str, password_hash: str):
    """Inserta un nuevo usuario en la base de datos."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        c.execute(sql, (username, email, password_hash))
        conn.commit()
    finally:
        c.close()
        conn.close()

def insert_conversion(amount_cop: float, exchange_rate: float, total_usd: float, target_currency: str):
    """Inserta una nueva conversión en la tabla history."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        sql = """
            INSERT INTO history (amount_cop, exchange_rate, total_usd, target_currency) 
            VALUES (%s, %s, %s, %s)
        """
        c.execute(sql, (amount_cop, exchange_rate, total_usd, target_currency))
        conn.commit()
    finally:
        c.close()
        conn.close()