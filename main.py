import tkinter as tk
from tkinter import Menu
from modulos import ventas, caja, clientes, proveedores, estadisticas, reportes, articulos, operaciones, administracion

def iniciar_aplicacion():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Software de Gestión - Dietética")
    root.geometry("800x600")

    # Crear el contenedor donde se mostrarán las secciones
    frame_contenedor = tk.Frame(root)
    frame_contenedor.pack(fill=tk.BOTH, expand=True)

    # Crear la barra de menú
    menu_bar = Menu(root)

    # --- Menú VENTAS ---
    menu_ventas = Menu(menu_bar, tearoff=0)
    menu_ventas.add_command(label="Nueva Venta / Comprobante Nuevo", command=lambda: ventas.mostrar_ventas(frame_contenedor))
    menu_ventas.add_command(label="Guardar Comprobante", command=lambda: ventas.mostrar_ventas(frame_contenedor))
    menu_ventas.add_command(label="Buscar Comprobante", command=lambda: ventas.mostrar_ventas(frame_contenedor))
    menu_ventas.add_separator()
    menu_ventas.add_command(label="Salir", command=root.quit)
    menu_bar.add_cascade(label="VENTAS", menu=menu_ventas)

    # --- Menú CAJA ---
    menu_caja = Menu(menu_bar, tearoff=0)
    
    submenu_extracciones = Menu(menu_caja, tearoff=0)
    submenu_extracciones.add_command(label="INGRESOS de dinero a Caja (ingreso de efectivo)", command=lambda: caja.mostrar_caja(frame_contenedor))
    submenu_extracciones.add_command(label="EXTRACCIONES de dinero de Caja (gastos externos)", command=lambda: caja.mostrar_caja(frame_contenedor))
    submenu_extracciones.add_command(label="Ver Extracciones e Ingresos de Caja Abierta", command=lambda: caja.mostrar_caja(frame_contenedor))

    menu_caja.add_cascade(label="Extracción e Ingresos de Caja (externo a ventas)", menu=submenu_extracciones)
    menu_caja.add_separator()
    menu_caja.add_command(label="APERTURA de Caja", command=lambda: caja.mostrar_caja(frame_contenedor))
    menu_caja.add_command(label="CIERRE de Caja", command=lambda: caja.mostrar_caja(frame_contenedor))
    menu_caja.add_command(label="VER Cajas Cerradas", command=lambda: caja.mostrar_caja(frame_contenedor))
    
    menu_bar.add_cascade(label="CAJA", menu=menu_caja)

    # --- Menú CLIENTES ---
    menu_clientes = Menu(menu_bar, tearoff=0)
    menu_clientes.add_command(label="Alta Cliente", command=lambda: clientes.mostrar_alta_cliente(frame_contenedor))
    menu_bar.add_cascade(label="CLIENTES", menu=menu_clientes)

    # --- Menú PROVEEDORES ---
    menu_proveedores = Menu(menu_bar, tearoff=0)
    menu_proveedores.add_command(label="Alta Proveedor", command=lambda: proveedores.mostrar_alta_proveedor(frame_contenedor))
    menu_proveedores.add_command(label="Entrada de Mercadería", command=lambda: proveedores.mostrar_entrada_mercaderia(frame_contenedor))
    menu_bar.add_cascade(label="PROVEEDORES", menu=menu_proveedores)

    # --- Menú ESTADÍSTICAS ---
    menu_estadisticas = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="ESTADÍSTICAS", menu=menu_estadisticas)

    # --- Menú REPORTES ---
    menu_reportes = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="REPORTES", menu=menu_reportes)

    # --- Menú ARTÍCULOS ---
    menu_articulos = Menu(menu_bar, tearoff=0)
    menu_articulos.add_command(label="Alta Artículo", command=lambda: articulos.mostrar_alta_articulo(frame_contenedor))
    menu_articulos.add_command(label="Control de Precio", command=lambda: articulos.mostrar_control_precio(frame_contenedor))
    menu_bar.add_cascade(label="ARTÍCULOS", menu=menu_articulos)

    # --- Menú OPERACIONES ---
    menu_operaciones = Menu(menu_bar, tearoff=0)
    menu_operaciones.add_command(label="Operación 1", command=lambda: operaciones.operacion_1(frame_contenedor))
    menu_operaciones.add_command(label="Operación 2", command=lambda: operaciones.operacion_2(frame_contenedor))
    menu_bar.add_cascade(label="OPERACIONES", menu=menu_operaciones)

    # --- Menú ADMINISTRACIÓN ---
    menu_administracion = Menu(menu_bar, tearoff=0)
    menu_administracion.add_command(label="Gestión de Usuarios", command=administracion.abrir_gestion_usuarios)
    menu_administracion.add_command(label="Configuraciones Generales", command=lambda: administracion.configuraciones(frame_contenedor))
    menu_bar.add_cascade(label="ADMINISTRACIÓN", menu=menu_administracion)

    # Configurar la barra de menú en la ventana principal
    root.config(menu=menu_bar)

    # Ejecutar la aplicación
    root.mainloop()

# Verificar login antes de ejecutar main.py
if __name__ == "__main__":
    if verificar_login():
        iniciar_aplicacion()
    else:
        print("Acceso denegado.")
