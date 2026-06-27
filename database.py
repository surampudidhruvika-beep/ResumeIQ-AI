import sqlite3

DB_NAME = "analysis.db"


# ---------------- ANALYSIS TABLE ---------------- #
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            score INTEGER,
            ai_feedback TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(filename, score, ai_feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analysis (filename, score, ai_feedback)
        VALUES (?, ?, ?)
    """, (filename, score, ai_feedback))

    conn.commit()
    conn.close()


# ---------------- USERS TABLE ---------------- #
def create_user_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()