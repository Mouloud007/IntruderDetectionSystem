import sqlite3

# Connect to SQLite database (creates 'faces.db' if it doesn’t exist)
conn = sqlite3.connect("faces.db")
cursor = conn.cursor()

# **Drop old table (if needed) and create a fresh one**
cursor.execute("DROP TABLE IF EXISTS known_faces")  # Reset database
cursor.execute("""
CREATE TABLE known_faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    encoding BLOB NOT NULL
)
""")

conn.commit()
conn.close()
print("✅ Database created & reset successfully!")
