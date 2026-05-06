import sqlite3

DB_NAME='learning.db'

def get_connection():
    conn=sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS performance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        topic TEXT,
        score INTEGER
        )
        ''')

    conn.commit()
    conn.close()