import tkinter as tk
from tkinter import Label

def mostrar_operaciones(frame):
    """Pantalla principal del módulo Operaciones"""
    for widget in frame.winfo_children():
        widget.destroy()
    
    label = Label(frame, text="Módulo de Operaciones", font=("Arial", 14))
    label.pack(pady=20)

def operacion_1(frame):
    """Función para la primera opción del submenú"""
    for widget in frame.winfo_children():
        widget.destroy()

    label = Label(frame, text="Operación 1 en proceso...", font=("Arial", 14))
    label.pack(pady=20)

def operacion_2(frame):
    """Función para la segunda opción del submenú"""
    for widget in frame.winfo_children():
        widget.destroy()

    label = Label(frame, text="Operación 2 en proceso...", font=("Arial", 14))
    label.pack(pady=20)
