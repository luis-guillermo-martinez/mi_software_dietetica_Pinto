# Software de Gestión para Dietética

Este es un software de escritorio desarrollado en Python para la gestión de una dietética. Permite la administración de ventas, clientes, proveedores, stock, reportes y estadísticas, con una interfaz visual intuitiva.

## 📌 Características
- **Gestión de Ventas**: Creación y búsqueda de comprobantes.
- **Caja**: Registro de ingresos y extracciones.
- **Clientes y Proveedores**: Alta, baja y modificación de datos.
- **Artículos**: Gestión de stock y control de precios.
- **Reportes y Estadísticas**: Análisis de ventas y productos.
- **Administración de Usuarios**: Alta, baja y modificación de usuarios.
- **Sistema de Login**: Acceso seguro con credenciales almacenadas en base de datos.

## 🛠️ Tecnologías Utilizadas
- **Python 3.13**
- **Tkinter** (Interfaz gráfica)
- **SQLite** (Base de datos local)

## 📂 Estructura del Proyecto
```
mi_software_dietetica/
│-- modulos/
│   ├── ventas.py
│   ├── caja.py
│   ├── clientes.py
│   ├── proveedores.py
│   ├── articulos.py
│   ├── reportes.py
│   ├── estadisticas.py
│   ├── operaciones.py
│   ├── administracion.py
│-- login.py
│-- main.py
│-- crear_db.py
│-- base_datos.db
│-- README.md
```

## 🚀 Instalación y Uso
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/mi_software_dietetica.git
cd mi_software_dietetica
```

### 2️⃣ Instalar dependencias
```bash
pip install tk
```

### 3️⃣ Crear la base de datos (Solo la primera vez)
```bash
python crear_db.py
```

### 4️⃣ Ejecutar la aplicación
```bash
python login.py
```

## 📌 Credenciales de Prueba
➡ **Usuario:** `admin`  
➡ **Contraseña:** `1234`

## 📜 Licencia
Este proyecto es de código abierto bajo la licencia MIT.

