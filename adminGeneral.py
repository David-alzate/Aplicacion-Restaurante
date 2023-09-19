import psycopg2
from usuario import*


# clase administrador General que hereda los atributos de usuario
class adminGeneral(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo,rol):
        super().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)

# Métodos 

    # Método para crear usuario
    def crearUsuario(conexion, nombre, apellido, correo, telefono, direccion, password, id, rol):
        # Convertir el rol a minúsculas para ingresarlo en asi en la base de datos
        rol = rol.lower()
        # Lista de roles permitidos
        roles_permitidos = ["administrador", "mesero", "cocinero"]
        
        # Evaluamos si el rol ingresado esta dentro de la lista de roles permitidos 
        if rol not in roles_permitidos:
            print("Rol no válido. Los roles permitidos son:", roles_permitidos)
            return False
        # Hacemos la consulta en SQL para ingresar el usuario a la base de datos
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido, correo, telefono, direccion, password, id, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, correo, telefono, direccion, password, id, rol))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario:", e)
            return False
    
    # Metodo Para Modificar Un usuario ya creado
    def modificarUsuario(conexion, id, campoModificar, nuevoValor):
        # Hacemos la consulta SQL para modificar el campo deseado
        try:
            with conexion.cursor() as cursor:
                # Lista de campos validos para modificar
                camposValidos = ["nombre", "apellido", "correo", "telefono", "direccion", "password", "rol"]
                # Evaluamos que el campo ingresado si este en la lista 
                if campoModificar not in camposValidos:
                    print("Campo no válido.")
                    return False

                # Validar el rol si el campoModificar es 'rol'
                if campoModificar == "rol":
                    nuevoValor = nuevoValor.lower()  # Convertir el valor a minúsculas
                    roles_permitidos = ["administrador", "mesero", "cocinero"]
                    if nuevoValor not in roles_permitidos:
                        print("Rol no válido. Los roles permitidos son:", roles_permitidos)
                        return False
                 # Hacemos la consulta SQL para modificar el campo
                consulta = f"UPDATE usuarios SET {campoModificar} = %s WHERE id = %s"
                cursor.execute(consulta, (nuevoValor, id))
                conexion.commit()
                print(f"El campo '{campoModificar}' se actualizó con éxito.")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

# Método para Consultar un usuario por su id
    def consultarUsuario(conexion, id):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
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

# Método para consultar Todos los usuarios de la base de datos
    def consultarUsuarios(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos de todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios;")
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(usuario)
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método Eliminar usuario por su id 
    def eliminarUsuario(conexion, id):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuarios WHERE id =" + str(id)
                cursor.execute(consulta)
                print("Usuario eliminado con exito")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

# Método para eliminar todos los usuarios de la base de datos 
    def eliminarUsuarios(conexion):
        # Hacemos la consulta SQL para eliminar todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios;")
                conexion.commit()
                print("Todos los usuarios han sido eliminados exitosamente.")
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar usuarios: ", e)
    

    



    
       
