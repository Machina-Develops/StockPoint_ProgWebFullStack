# servicios.py (versión persistente con MySQL)
import hashlib
# from repositorio import RepositorioUsuarios              # <- memoria (antiguo)
from repositorio_mysql import RepositorioUsuarios           # <- persistencia MySQL
from usuario import Usuario

class ServicioUsuarios:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
        self._crear_admin_por_defecto()

    def _hashear_contrasena(self, contrasena: str) -> str:
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

    def _validar_contrasena(self, contrasena: str) -> bool:
        if len(contrasena) < 6: 
            return False
        return any(c.isalpha() for c in contrasena) and any(c.isdigit() for c in contrasena)

    def _crear_admin_por_defecto(self):
        # La BD ya lo seedéa, pero mantenemos por idempotencia
        admin = self.__repositorio.buscar_por_nombre("admin")
        if not admin:
            self.__repositorio.crear_usuario(
                nombre_usuario="admin",
                email="admin@sistema.com",
                contrasena_hash=self._hashear_contrasena("Admin123"),
                rol="administrador"
            )

    def registrar_usuario(self, nombre_usuario: str, email: str, contrasena: str):
        if not self._validar_contrasena(contrasena):
            return "Error: La contraseña no cumple los requisitos."
        if self.__repositorio.buscar_por_nombre(nombre_usuario):
            return "Error: El nombre de usuario ya existe."
        contrasena_hash = self._hashear_contrasena(contrasena)
        try:
            return self.__repositorio.crear_usuario(nombre_usuario, email, contrasena_hash)
        except Exception as e:
            msg = str(e)
            if "Duplicate" in msg or "1062" in msg:
                return "Error: Ya existe un usuario con ese email o nombre."
            return f"Error de base de datos: {msg}"

    def iniciar_sesion(self, nombre_usuario: str, contrasena: str):
        usuario = self.__repositorio.buscar_por_nombre(nombre_usuario)
        if usuario and usuario.verificar_contrasena(contrasena, self._hashear_contrasena):
            return usuario
        return None

    def obtener_todos_los_usuarios(self):
        return self.__repositorio.obtener_todos()

    def cambiar_rol(self, id_usuario: int, nuevo_rol: str) -> bool:
        if nuevo_rol not in ["administrador", "estandar"]:
            return False
        return self.__repositorio.actualizar_rol(id_usuario, nuevo_rol)

    def eliminar_usuario(self, id_usuario: int) -> bool:
        return self.__repositorio.eliminar_por_id(id_usuario)
