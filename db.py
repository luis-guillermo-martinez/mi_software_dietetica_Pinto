import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()

# Crear la tabla "usuarios" si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        usuario TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Agregar un usuario de prueba (solo si la tabla está vacía)
cursor.execute("SELECT COUNT(*) FROM usuarios")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO usuarios (nombre, usuario, password) VALUES ('Admin', 'admin', '1234')")
    conexion.commit()

# Cerrar la conexión
conexion.close()

print("Base de datos y usuario creados correctamente.")
