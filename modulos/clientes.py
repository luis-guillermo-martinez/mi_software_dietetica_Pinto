from tkinter import Label, Entry, Button

def mostrar_alta_cliente(frame_contenedor):
    # Elimina cualquier contenido anterior
    for widget in frame_contenedor.winfo_children():
        widget.destroy()

    # Título
    Label(frame_contenedor, text="Alta de Cliente", font=("Arial", 20)).pack(pady=10)

    # Campos del formulario
    Label(frame_contenedor, text="Nombre:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Apellido:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="DNI / CUIT:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Teléfono:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Dirección:").pack()
    Entry(frame_contenedor, width=40).pack()

    # Botón para guardar
    Button(frame_contenedor, text="Guardar Cliente", bg="green", fg="white").pack(pady=10)
