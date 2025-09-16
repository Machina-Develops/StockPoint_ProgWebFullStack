[README.md](https://github.com/user-attachments/files/22373129/README.md)
# 📦 Sistema de Gestión de Stock - StokPoint®

**StokPoint®** es una aplicación orientada a pequeños negocios, depósitos, talleres y PYMEs.  
Permite registrar productos, controlar inventario en tiempo real y gestionar movimientos de entrada y salida, asegurando un seguimiento eficiente de los recursos.

---

## 🎯 Objetivos
- Mantener actualizado el stock automáticamente.  
- Permitir diferentes roles de usuario con permisos específicos.  
- Facilitar la toma de decisiones con informes claros.  
- Brindar una herramienta digital adaptable a distintos tipos de negocio.  

---

## 🔑 Funcionalidades principales
- **Productos**: Registro, modificación y consulta de stock.  
- **Movimientos**: Registro de entradas y salidas, validación y actualización automática.  
- **Usuarios y Roles**: Administración de usuarios, asignación de roles y permisos.  
- **Reportes**: Consulta de inventario en tiempo real y exportación digital (PDF/Excel).  

---

## 🗄️ Modelo de datos
El sistema se basa en una **base de datos relacional** con las siguientes entidades:
- **Producto**
- **Movimiento**
- **Usuario**
- **Rol**
- **Permiso**
- **Rol_Permiso**

### 📌 Clases principales
- **Producto** → `updateInfoProducto`, `cambiarPrecio`, `obtenerStock`  
- **Movimiento** → `afectarStock`, `validarMovimiento`, `registrarMovimiento`, `mostrarMovimiento`  
- **Usuario** → `verificar_permiso`  
- **Rol** → `tiene_permiso`, `agregar_permiso`, `remover_permiso`  

---

## 🛠️ Tecnologías utilizadas
- **Backend**: Python 3.10+ (Flask / FastAPI)  
- **Base de datos**: MySQL (desarrollo inicial en SQLite)  
- **Frontend**: HTML5, CSS3, JavaScript  

---

## ⚙️ Requisitos
- Python 3.10+  
- Librerías: `sqlite3`, `tabulate` (y las que se incluyan en `requirements.txt`)  
- MySQL (para despliegue final)  

---

## 🚀 Instalación y uso
1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/Machina-Develops/StockPoint_ProgWebFullStack.git
   cd StockPoint_ProgWebFullStack
