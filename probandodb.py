import sqlite3

conn = sqlite3.connect("gestion.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios';")
tabla = cursor.fetchone()

if tabla:
    print("✅ La tabla 'usuarios' existe.")
else:
    print("❌ La tabla 'usuarios' NO existe.")

conn.close()
