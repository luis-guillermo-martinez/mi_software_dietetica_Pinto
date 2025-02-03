import tkinter as tk
from tkinter import Label

def mostrar_estadisticas(frame):
    """ Función para mostrar la pantalla de estadísticas en el frame principal """
    for widget in frame.winfo_children():
        widget.destroy()  # Limpiar el frame antes de cargar la sección
    
    label = Label(frame, text="Módulo de Estadísticas", font=("Arial", 14))
    label.pack(pady=20)
