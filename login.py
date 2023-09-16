import psycopg2
from usuario import *


class login(usuario):
    def __init__(self,contraseña, id):
        super().__init__(contraseña, id)
    

    def iniciarSesion(conexion, id, contraseña):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
                usuario = cursor.fetchone()
                if usuario:
                    # Comprobar si la contraseña coincide
                    if contraseña == usuario[5]:   # 5 es el índice de la columna 'contraseña' en la base de datos 
                        print("Inicio de sesión exitoso.")
                        return True
                    else:
                        print("Contraseña incorrecta.")
                        return False
                else:
                    print("El usuario no existe.")
                    return False
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
            return False

        
    def cerrarSesion(self):
        pass
        
