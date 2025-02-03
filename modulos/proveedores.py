from tkinter import Label, Entry, Button

def mostrar_alta_proveedor(frame_contenedor):
    # Limpiar contenido previo
    for widget in frame_contenedor.winfo_children():
        widget.destroy()

    Label(frame_contenedor, text="Alta de Proveedor", font=("Arial", 20)).pack(pady=10)

    Label(frame_contenedor, text="Razón Social:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="CUIT:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Teléfono:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Dirección:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Correo Electrónico:").pack()
    Entry(frame_contenedor, width=40).pack()

    Button(frame_contenedor, text="Guardar Proveedor", bg="green", fg="white").pack(pady=10)

def mostrar_entrada_mercaderia(frame_contenedor):
    # Limpiar contenido previo
    for widget in frame_contenedor.winfo_children():
        widget.destroy()

    Label(frame_contenedor, text="Entrada de Mercadería", font=("Arial", 20)).pack(pady=10)

    Label(frame_contenedor, text="Proveedor:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Producto:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Cantidad:").pack()
    Entry(frame_contenedor, width=40).pack()

    Label(frame_contenedor, text="Fecha de Ingreso:").pack()
    Entry(frame_contenedor, width=40).pack()

    Button(frame_contenedor, text="Registrar Entrada", bg="blue", fg="white").pack(pady=10)
