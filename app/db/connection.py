import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,      
        user="root",
        password="",    
        database="globalsettler_db"
    )
    
def init_db():
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
    conn.commit()
    c.close()
    conn.close()

def insert_conversion(amount_cop, exchange_rate, total_usd, target_currency):
    conn = get_db_connection()
    c = conn.cursor()
    
    
    query = """
        INSERT INTO history (amount_cop, exchange_rate, total_usd, target_currency) 
        VALUES (%s, %s, %s, %s)
    """
    c.execute(query, (amount_cop, exchange_rate, total_usd, target_currency))
    
    conn.commit()
    c.close()
    conn.close()

def get_all_history():
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("""
        SELECT id, amount_cop, exchange_rate, total_usd, target_currency, date 
        FROM history 
        ORDER BY date DESC
    """)
    rows = c.fetchall()
    
    c.close()
    conn.close()
    return rows