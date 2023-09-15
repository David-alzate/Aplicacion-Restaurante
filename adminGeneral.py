import psycopg2
from usuario import*

class adminGeneral(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, contraseña, id, correo,rol):
        super().__init__(nombre, apellido, telefono, direccion, contraseña, id, correo, rol)

    def crearUsuario(conexion, nombre, apellido, correo, telefono, direccion, contraseña, id, rol):
        # Convertir el rol a minúsculas
        rol = rol.lower()
        # Lista de roles permitidos
        roles_permitidos = ["administrador", "mesero", "cocinero"]

        if rol not in roles_permitidos:
            print("Rol no válido. Los roles permitidos son:", roles_permitidos)
            return False

        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido, correo, telefono, direccion, contraseña, id, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, correo, telefono, direccion, contraseña, id, rol))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario:", e)
            return False
        
    def modificarUsuario(conexion, id, campo_a_modificar, nuevo_valor):
        try:
            with conexion.cursor() as cursor:
                # Validar el campo_a_modificar
                campos_validos = ["nombre", "apellido", "correo", "telefono", "direccion", "contraseña", "rol"]
                if campo_a_modificar not in campos_validos:
                    print("Campo no válido.")
                    return False

                # Validar el rol si el campo_a_modificar es 'rol'
                if campo_a_modificar == "rol":
                    nuevo_valor = nuevo_valor.lower()  # Convertir el valor a minúsculas
                    roles_permitidos = ["administrador", "mesero", "cocinero"]
                    if nuevo_valor not in roles_permitidos:
                        print("Rol no válido. Los roles permitidos son:", roles_permitidos)
                        return False

                consulta = f"UPDATE usuarios SET {campo_a_modificar} = %s WHERE id = %s"
                cursor.execute(consulta, (nuevo_valor, id))
                conexion.commit()
                print(f"El campo '{campo_a_modificar}' se actualizó con éxito.")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)
        
    def consultarUsuario(conexion, id):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id="+str(id))
                usuario = cursor.fetchone()
                if usuario:
                    print(usuario)
                else:
                    print("El usuario no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarUsuarios(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios;")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(usuario)
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def eliminarUsuario(conexion, id):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuarios WHERE id =" + str(id)
                cursor.execute(consulta)
                print("Usuario eliminado con exito")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

    def eliminarUsuarios(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios;")
                conexion.commit()
                print("Todos los usuarios han sido eliminados exitosamente.")
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar usuarios: ", e)
    

    



    
       
