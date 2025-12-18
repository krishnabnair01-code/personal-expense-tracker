import sqlite3

def connect_db():
    return sqlite3.connect("data/expenses.db")

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()
