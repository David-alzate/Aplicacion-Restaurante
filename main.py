from database import *
from usuario import*

conexion = Basedatos("localhost","postgres","000")
conexion.conectar()


if (usuario.crearUsuario(conexion.conectar(), "luis", "ospina", "lector@gmail.com", "3127054715", "cll 15", "123", "1040031815")):
    print("USUARIO CREADO EXITOSAMENTE")
else:
    print("ERROR DE CREACION")

print("Hola David Alzate")