import psycopg2
from usuario import*

class adminGeneral(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, contraseña, id, correo):
        super().__init__(nombre, apellido, telefono, direccion, contraseña, id, correo)
