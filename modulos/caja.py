from tkinter import Label

def mostrar_caja(frame_contenedor):
    # Elimina cualquier contenido anterior
    for widget in frame_contenedor.winfo_children():
        widget.destroy()

    # Muestra el contenido de la sección
    Label(frame_contenedor, text="Sección: Caja", font=("Arial", 20)).pack(pady=50)
