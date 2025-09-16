# usuario.py

class Usuario:
    """
    Representa a un usuario del sistema.
    """
    def __init__(self, id_usuario: int, nombre_usuario: str, email: str, contrasena_hash: str, rol: str):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.contrasena_hash = contrasena_hash  # hash SHA-256 en hex
        self.rol = rol  # 'administrador' o 'estandar'

    def verificar_contrasena(self, contrasena: str, hashear_func) -> bool:
        """
        Compara el hash guardado con el hash de la contraseña ingresada.
        hashear_func es la función que hashéa (la provee servicios.py).
        """
        return self.contrasena_hash == hashear_func(contrasena)

    def __repr__(self) -> str:
        return f"Usuario(id={self.id_usuario}, nombre='{self.nombre_usuario}', rol='{self.rol}')"
