# repositorio_mysql.py
from typing import Optional, List
from usuario import Usuario
from db import get_connection

class RepositorioUsuarios:
    """Repositorio persistente en MySQL."""
    def __init__(self):
        pass

    # CREATE
    def crear_usuario(self, nombre_usuario: str, email: str, contrasena_hash: str, rol: str = "estandar") -> Usuario:
        sql = """
        INSERT INTO usuarios (nombre_usuario, email, contrasena_hash, rol)
        VALUES (%s, %s, %s, %s)
        """
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (nombre_usuario, email, contrasena_hash, rol))
            new_id = cur.lastrowid
        return Usuario(
            id_usuario=new_id,
            nombre_usuario=nombre_usuario,
            email=email,
            contrasena_hash=contrasena_hash,
            rol=rol
        )

    # READ
    def _row_to_usuario(self, row) -> Usuario:
        return Usuario(
            id_usuario=row[0],
            nombre_usuario=row[1],
            email=row[2],
            contrasena_hash=row[3],
            rol=row[4]
        )

    def buscar_por_nombre(self, nombre_usuario: str) -> Optional[Usuario]:
        sql = "SELECT id, nombre_usuario, email, contrasena_hash, rol FROM usuarios WHERE nombre_usuario = %s LIMIT 1"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (nombre_usuario,))
            row = cur.fetchone()
            return self._row_to_usuario(row) if row else None

    def buscar_por_id(self, id_usuario: int) -> Optional[Usuario]:
        sql = "SELECT id, nombre_usuario, email, contrasena_hash, rol FROM usuarios WHERE id = %s LIMIT 1"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_usuario,))
            row = cur.fetchone()
            return self._row_to_usuario(row) if row else None

    def obtener_todos(self) -> List[Usuario]:
        sql = "SELECT id, nombre_usuario, email, contrasena_hash, rol FROM usuarios ORDER BY id"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql)
            return [self._row_to_usuario(r) for r in cur.fetchall()]

    # UPDATE
    def actualizar_rol(self, id_usuario: int, nuevo_rol: str) -> bool:
        sql = "UPDATE usuarios SET rol = %s WHERE id = %s"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (nuevo_rol, id_usuario))
            return cur.rowcount == 1

    # NUEVO: actualizar mis datos (nombre y email)
    def actualizar_mis_datos(self, id_usuario: int, nombre_usuario: str, email: str) -> bool:
        sql = "UPDATE usuarios SET nombre_usuario = %s, email = %s WHERE id = %s"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (nombre_usuario, email, id_usuario))
            return cur.rowcount == 1

    # NUEVO: actualizar contraseña (hash)
    def actualizar_contrasena(self, id_usuario: int, nuevo_hash: str) -> bool:
        sql = "UPDATE usuarios SET contrasena_hash = %s WHERE id = %s"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (nuevo_hash, id_usuario))
            return cur.rowcount == 1

    # DELETE
    def eliminar_por_id(self, id_usuario: int) -> bool:
        sql = "DELETE FROM usuarios WHERE id = %s"
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_usuario,))
            return cur.rowcount == 1
