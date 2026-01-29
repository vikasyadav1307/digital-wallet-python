import sqlite3
from datetime import datetime


# ---------------- CONNECT DATABASE ----------------
def connect_db():
    return sqlite3.connect("wallet.db")


# ---------------- CREATE TABLES ----------------
def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    # -------- USERS TABLE --------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # -------- TRANSACTIONS TABLE (WITH STATUS) --------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        txn_type TEXT,
        amount REAL,
        description TEXT,
        status TEXT,
        timestamp TEXT

    )
    """)

    conn.commit()
    conn.close()


# ---------------- SAVE TRANSACTION ----------------
def save_transaction(user_id, txn_type, amount, description, status="SUCCESS"):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO transactions(user_id, txn_type, amount, description, status, timestamp) VALUES(?,?,?,?,?,?)",
        (user_id, txn_type, amount, description, status, timestamp)
    )

    conn.commit()
    conn.close()


# ---------------- LOAD TRANSACTIONS ----------------
def load_transactions(user_id):
    try:
        conn = connect_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT txn_type, amount, description, status, timestamp FROM transactions WHERE user_id=?",
            (user_id,)
        )

        data = cur.fetchall()
        conn.close()

        return data

    except Exception as e:
        print("Load Transaction Error:", e)
        return []
