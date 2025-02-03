import tkinter as tk
from tkinter import messagebox
import sqlite3

def abrir_gestion_usuarios():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Usuarios")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    # Etiquetas y Entradas
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(ventana, text="Usuario:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(ventana, text="Contraseña:").grid(row=2, column=0, padx=10, pady=5)

    entry_nombre = tk.Entry(ventana)
    entry_usuario = tk.Entry(ventana)
    entry_password = tk.Entry(ventana, show="*")

    entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    entry_usuario.grid(row=1, column=1, padx=10, pady=5)
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    # Lista de usuarios
    lista_usuarios = tk.Listbox(ventana, height=10, width=50)
    lista_usuarios.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Función para actualizar la lista de usuarios
    def actualizar_lista():
        lista_usuarios.delete(0, tk.END)
        conn = sqlite3.connect("gestion.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, usuario FROM usuarios")
        for usuario in cursor.fetchall():
            lista_usuarios.insert(tk.END, f"{usuario[0]} - {usuario[1]} ({usuario[2]})")
        conn.close()

    actualizar_lista()

    # Función para agregar usuario
    def agregar_usuario():
        nombre = entry_nombre.get()
        usuario = entry_usuario.get()
        password = entry_password.get()

        if nombre and usuario and password:
            conn = sqlite3.connect("gestion.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO usuarios (nombre, usuario, password) VALUES (?, ?, ?)",
                               (nombre, usuario, password))
                conn.commit()
                messagebox.showinfo("Éxito", "Usuario agregado correctamente")
                entry_nombre.delete(0, tk.END)
                entry_usuario.delete(0, tk.END)
                entry_password.delete(0, tk.END)
                actualizar_lista()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El usuario ya existe")
            finally:
                conn.close()
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")

    # Función para eliminar usuario
    def eliminar_usuario():
        try:
            seleccion = lista_usuarios.get(lista_usuarios.curselection())
            usuario_id = seleccion.split(" - ")[0]
        except:
            messagebox.showwarning("Atención", "Seleccione un usuario para eliminar")
            return

        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este usuario?")
        if respuesta:
            conn = sqlite3.connect("gestion.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
            actualizar_lista()

    # Función para cargar usuario en los campos para editar
    def cargar_usuario():
        try:
            seleccion = lista_usuarios.get(lista_usuarios.curselection())
            usuario_id = seleccion.split(" - ")[0]
        except:
            messagebox.showwarning("Atención", "Seleccione un usuario para editar")
            return

        conn = sqlite3.connect("gestion.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, usuario, password FROM usuarios WHERE id=?", (usuario_id,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            entry_nombre.delete(0, tk.END)
            entry_usuario.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_nombre.insert(0, usuario[0])
            entry_usuario.insert(0, usuario[1])
            entry_password.insert(0, usuario[2])
            btn_guardar_edicion.config(state=tk.NORMAL)
            btn_guardar_edicion.config(command=lambda: editar_usuario(usuario_id))

    # Función para editar usuario
    def editar_usuario(usuario_id):
        nombre = entry_nombre.get()
        usuario = entry_usuario.get()
        password = entry_password.get()

        if nombre and usuario and password:
            conn = sqlite3.connect("gestion.db")
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE usuarios SET nombre=?, usuario=?, password=? WHERE id=?",
                               (nombre, usuario, password, usuario_id))
                conn.commit()
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                entry_nombre.delete(0, tk.END)
                entry_usuario.delete(0, tk.END)
                entry_password.delete(0, tk.END)
                actualizar_lista()
                btn_guardar_edicion.config(state=tk.DISABLED)
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El usuario ya existe")
            finally:
                conn.close()
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")

    # Botones
    btn_guardar = tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario)
    btn_guardar.grid(row=3, column=0, pady=5, padx=10)

    btn_eliminar = tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario)
    btn_eliminar.grid(row=3, column=1, pady=5, padx=10)

    btn_cargar = tk.Button(ventana, text="Editar Usuario", command=cargar_usuario)
    btn_cargar.grid(row=5, column=0, pady=5, padx=10)

    btn_guardar_edicion = tk.Button(ventana, text="Guardar Cambios", state=tk.DISABLED)
    btn_guardar_edicion.grid(row=5, column=1, pady=5, padx=10)

    ventana.mainloop()
