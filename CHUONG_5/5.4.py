import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute(
    ("""
    SELECT name FROM sqlite_master
    WHERE type='table'
    """)
)
cursor.fetchall()