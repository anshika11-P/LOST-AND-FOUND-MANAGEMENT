import sqlite3

conn = sqlite3.connect("lostfound.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Lost Items Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS lost_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

# Found Items Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS found_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")