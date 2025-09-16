# main.py (ajustado para persistencia MySQL)
import os
import platform
from getpass import getpass
from servicios import ServicioUsuarios

def limpiar_pantalla():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def menu_principal(servicio: ServicioUsuarios):
    usuario_actual = None
    while True:
        limpiar_pantalla()
        if usuario_actual:
            if usuario_actual.rol == "administrador":
                usuario_actual = menu_administrador(servicio, usuario_actual)
            else:
                usuario_actual = menu_estandar(servicio, usuario_actual)
        else:
            print("--- SISTEMA DE GESTIÓN (PERSISTENCIA MySQL) ---")
            print("1. Iniciar Sesión")
            print("2. Registrarse")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                usuario_actual = gestionar_inicio_sesion(servicio)
            elif opcion == '2':
                gestionar_registro(servicio)
            elif opcion == '3':
                print("¡Hasta luego!")
                break

def gestionar_registro(servicio: ServicioUsuarios):
    limpiar_pantalla()
    print("--- REGISTRO DE NUEVO USUARIO ---")
    nombre = input("Nombre de usuario: ")
    email = input("Email: ")
    contrasena = getpass("Contraseña: ")
    resultado = servicio.registrar_usuario(nombre, email, contrasena)
    if isinstance(resultado, str):
        print(f"\n{resultado}")
    else:
        print("\n¡Usuario registrado con éxito!")
    input("\nPresione Enter para continuar...")

def gestionar_inicio_sesion(servicio: ServicioUsuarios):
    limpiar_pantalla()
    print("--- INICIO DE SESIÓN ---")
    nombre = input("Nombre de usuario: ")
    contrasena = getpass("Contraseña: ")
    usuario = servicio.iniciar_sesion(nombre, contrasena)
    if usuario:
        print(f"\n¡Bienvenido, {usuario.nombre_usuario}! Rol: {usuario.rol}")
        input("\nPresione Enter para continuar...")
        return usuario
    else:
        print("\nError: Usuario o contraseña incorrectos.")
        input("\nPresione Enter para continuar...")
        return None

def menu_estandar(servicio: ServicioUsuarios, usuario):
    print(f"--- MENÚ DE USUARIO: {usuario.nombre_usuario} ---")
    print("1. Ver mis datos")
    print("2. Editar mis datos (nombre y email)")
    print("3. Cambiar mi contraseña")
    print("4. Cerrar Sesión")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print(f"\nID: {usuario.id_usuario}")
        print(f"Nombre: {usuario.nombre_usuario}")
        print(f"Email: {usuario.email}")
        print(f"Rol: {usuario.rol}")
        input("\nPresione Enter para continuar...")

    elif opcion == '2':
        nuevo_nombre = input("Nuevo nombre de usuario: ")
        nuevo_email = input("Nuevo email: ")
        resultado = servicio.actualizar_mis_datos(usuario.id_usuario, nuevo_nombre, nuevo_email)
        if resultado is True:
            print("\nDatos actualizados.")
            # Actualizamos el objeto en memoria para que el menú refleje cambios
            usuario.nombre_usuario = nuevo_nombre
            usuario.email = nuevo_email
        else:
            print(f"\n{resultado}")
        input("\nPresione Enter para continuar...")

    elif opcion == '3':
        from getpass import getpass
        actual = getpass("Contraseña actual: ")
        nueva = getpass("Nueva contraseña: ")
        resultado = servicio.cambiar_mi_contrasena(usuario.id_usuario, actual, nueva)
        print("\nContraseña actualizada." if resultado is True else f"\n{resultado}")
        input("\nPresione Enter para continuar...")

    elif opcion == '4':
        return None

    return usuario


def menu_administrador(servicio: ServicioUsuarios, usuario):
    print(f"--- MENÚ DE ADMINISTRADOR: {usuario.nombre_usuario} ---")
    print("1. Ver todos los usuarios")
    print("2. Cambiar rol de un usuario")
    print("3. Eliminar un usuario")
    print("4. Cerrar Sesión")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        limpiar_pantalla()
        print("--- LISTADO DE USUARIOS ---")
        for u in servicio.obtener_todos_los_usuarios():
            print(f"ID: {u.id_usuario}, Nombre: {u.nombre_usuario}, Rol: {u.rol}")
        input("\nPresione Enter para continuar...")
    elif opcion == '2':
        id_str = input("Ingrese el ID del usuario a modificar: ")
        nuevo_rol = input("Ingrese el nuevo rol (administrador/estandar): ")
        print("Rol actualizado." if servicio.cambiar_rol(int(id_str), nuevo_rol) else "No se pudo actualizar el rol.")
        input("\nPresione Enter para continuar...")
    elif opcion == '3':
        id_str = input("Ingrese el ID del usuario a eliminar: ")
        if int(id_str) == usuario.id_usuario:
            print("No puede eliminarse a sí mismo.")
        else:
            print("Usuario eliminado." if servicio.eliminar_usuario(int(id_str)) else "No se pudo eliminar el usuario.")
        input("\nPresione Enter para continuar...")
    elif opcion == '4':
        return None
    return usuario

if __name__ == "__main__":
    servicio_usuarios = ServicioUsuarios()
    menu_principal(servicio_usuarios)
