import tkinter as tk
from tkinter import messagebox
import sqlite3
import main  # Importamos el main para abrir la aplicación luego del login

def verificar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    # Conectar a la base de datos
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()

    # Verificar credenciales
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (usuario, password))
    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        root.destroy()  # Cierra la ventana de login
        main.iniciar_aplicacion()  # Llama a la función en main.py para abrir la aplicación
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana de login
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Etiqueta y campo de entrada para usuario
tk.Label(root, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

# Etiqueta y campo de entrada para contraseña
tk.Label(root, text="Contraseña:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botón para iniciar sesión
tk.Button(root, text="Iniciar Sesión", command=verificar_login).pack(pady=10)

# Ejecutar la ventana
root.mainloop()
