# StockPoint_ProgWebFullStack

 – StokPoint®

## Descripción
El **Sistema de Gestión de Stock (StokPoint®)** es una aplicación orientada a pequeños negocios, depósitos, talleres y PYMES.  
Permite registrar productos, controlar inventario en tiempo real y gestionar movimientos de entrada y salida, asegurando un seguimiento eficiente de los recursos.


## Objetivos
- Mantener actualizado el stock automáticamente.  
- Permitir diferentes roles de usuario con permisos específicos.  
- Facilitar la toma de decisiones con informes claros.  
- Brindar una herramienta digital adaptable a distintos tipos de negocio.  


## Funcionalidades principales
- **Productos:** Registro, modificación, consulta de stock.  
- **Movimientos:** Registro de entradas y salidas, validación y actualización automática.  
- **Usuarios y Roles:** Administración de usuarios, asignación de roles y permisos.  
- **Informes:** Consulta de inventario en tiempo real, exportación digital.  

## Modelo de datos
El sistema se basa en una **base de datos relacional** con las siguientes entidades:  
- `Producto`  
- `Movimiento`  
- `Usuario`  
- `Rol`  
- `Permiso`  
- `Rol_Permiso`  

## Clases principales
- **Producto** → `actualizarInfoProducto()`, `cambiarPrecio()`, `obtenerStock()`  
- **Movimiento** → `afectarStock()`, `validarMovimiento()`, `registrarMovimiento()`, `mostrarMovimiento()`  
- **Usuario** → `verificar_permiso()`  
- **Rol** → `tiene_permiso()`, `agregar_permiso()`, `remover_permiso()`  


   ```bash
   git clone https://github.com/usuario/gestion-stock.git
