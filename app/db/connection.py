import sqlite3

def init_db():

    conn = sqlite3.connect("savings.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount_cop REAL,
        exchange_rate REAL,
        total_usd REAL,
        target_currency TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    def insert_conversion(amount_cop, exchange_rate, total_usd, target_currency):
        conn = sqlite3.connect("savings.db")
        c = conn.cursor()
    
        c.execute("""
        INSERT INTO history (amount_cop, exchange_rate, total_usd, target_currency)
        VALUES (?, ?, ?, ?)
        """, (amount_cop, exchange_rate, total_usd, target_currency))
        
        conn.commit()
        conn.close()
        
    def get_all_history():
        conn= sqlite3.connect("savings.db")    
        c = conn.cursor()
        
        
        c.execute("SELECT id, amount_cop, exchange_rate, total_usd, target currency date FROM history ORDER by date DESC")
        rows = c.fetchall()
        
        conn.close()
        return rows