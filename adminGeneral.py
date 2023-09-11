import psycopg2
from usuario import*

class adminGeneral:
    def __init__(self, argumento):
        self.argumento = argumento

    def crearUsuario(conexion, nombre, apellido,correo,telefono,direccion,contraseña,id):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido, correo, telefono, direccion, contraseña , id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, correo,telefono,direccion,contraseña,id))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario:     ", e)
            return False
