import tkinter as tk
from tkinter import Label

def mostrar_alta_articulo(frame):
    """ Función para mostrar la pantalla de alta de artículo en el frame principal """
    for widget in frame.winfo_children():
        widget.destroy()  # Limpiar el frame antes de cargar la sección
    
    label = Label(frame, text="Alta de Artículo", font=("Arial", 14))
    label.pack(pady=20)

def mostrar_control_precio(frame):
    """ Función para mostrar la pantalla de control de precio en el frame principal """
    for widget in frame.winfo_children():
        widget.destroy()  
    
    label = Label(frame, text="Control de Precio", font=("Arial", 14))
    label.pack(pady=20)
