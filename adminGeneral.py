import psycopg2
from usuario import*
from productos import*
from local import*


# clase administrador General que hereda los atributos de usuario
class adminGeneral(usuario,producto,local):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo,rol,id_producto,precio,nombreProducto,
                 id_local,nombre_establecimiento):
        usuario().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)
        producto().__init__(id_producto,precio,nombreProducto)
        local().__init__(id_local,nombre_establecimiento)

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
                return True
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
                return True
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
            return True
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
            return True
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
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar usuarios: ", e)
    

# metodo para crear un producto 
    def crearProducto(conexion,precio,nombreProducto):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO producto(precio,nombreProducto) VALUES (%s, %s);"
                cursor.execute(consulta,(precio,nombreProducto))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear producto:", e)
            return False


# metodo para consultar producto
    def consultarProducto(conexion, id_producto):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM producto WHERE id_producto="+str(id_producto))
                producto = cursor.fetchone()
                if producto:
                    print(producto)
                else:
                    print("El producto no existe")
                return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    # Metodo Para Modificar Un producto ya creado
    def modificarProducto(conexion, id_producto, campoModificar, nuevoValor):
        # Hacemos la consulta SQL para modificar el campo deseado
        try:
            with conexion.cursor() as cursor:
                # Lista de campos validos para modificar
                camposValidos = ["precio","nombreProducto"]
                # Evaluamos que el campo ingresado si este en la lista 
                if campoModificar not in camposValidos:
                    print("Campo no válido.")
                    return False
                 # Hacemos la consulta SQL para modificar el campo
                consulta = f"UPDATE producto SET {campoModificar} = %s WHERE id_producto = %s"
                cursor.execute(consulta, (nuevoValor, id_producto))
                conexion.commit()
                print(f"El campo '{campoModificar}' se actualizó con éxito.")
                return True
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

# Método para consultar Todos los productos de la base de datos
    def consultarProductos(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos de todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM producto;")
                producto = cursor.fetchall()
                for producto in producto:
                    print(producto)
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
    
# Método para consultar producto por nombre
    def consultarProductoPorNombre(conexion, nombreProducto):
        try:
            with conexion.cursor() as cursor:
                # Utiliza un marcador de posición en la consulta SQL y pasa el valor como parámetro en el método execute
                cursor.execute("SELECT * FROM producto WHERE nombreProducto = %s", (nombreProducto,))
                producto = cursor.fetchall()
                if producto:
                    print(producto)
                else:
                    print("El producto no existe")
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método Eliminar producto por su id 
    def eliminarProducto(conexion, id_producto):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM producto WHERE id_producto =" + str(id_producto)
                cursor.execute(consulta)
                print("producto eliminado con exito")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
    
    def eliminarProductoPorNombre(conexion, nombreproducto):
        try:
            with conexion.cursor() as cursor:
                # Usamos comillas simples alrededor del valor para asegurarnos de que sea tratado como una cadena
                consulta = "DELETE FROM producto WHERE nombreproducto = %s"
                cursor.execute(consulta, (nombreproducto,))
                print("producto eliminado con éxito")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

# Método para eliminar todos los productos de la base de datos 
    def eliminarProductos(conexion):
        # Hacemos la consulta SQL para eliminar todos los productos de la tabla producto
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM producto;")
                conexion.commit()
                print("Todos los productos han sido eliminados exitosamente.")
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar productos: ", e) 

# metodo para crear un local 
    def crearLocal(conexion,nombre_establecimiento):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO local(nombre_establecimiento) VALUES (%s);"
                cursor.execute(consulta, (nombre_establecimiento,))

            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear producto:", e)
            return False
        
# metodo para consultar local
    def consultarLocal(conexion, id_local):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM local WHERE id_local="+str(id_local))
                local = cursor.fetchone()
                if local:
                    print(local)
                else:
                    print("El local no existe")
                return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    # Metodo Para Modificar Un Local ya creado
    def modificarLocal(conexion, id_local, campoModificar, nuevoValor):
        # Hacemos la consulta SQL para modificar el campo deseado
        try:
            with conexion.cursor() as cursor:
                # Lista de campos validos para modificar
                camposValidos = ["nombre_establecimiento"]
                # Evaluamos que el campo ingresado si este en la lista 
                if campoModificar not in camposValidos:
                    print("Campo no válido.")
                    return False
                 # Hacemos la consulta SQL para modificar el campo
                consulta = f"UPDATE local SET {campoModificar} = %s WHERE id_local = %s"
                cursor.execute(consulta, (nuevoValor, id_local))
                conexion.commit()
                print(f"El campo '{campoModificar}' se actualizó con éxito.")
                return True
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)
    
# Método para consultar local por nombre
    def consultarLocalPorNombre(conexion, nombre_establecimiento):
        try:
            with conexion.cursor() as cursor:
                # Utiliza un marcador de posición en la consulta SQL y pasa el valor como parámetro en el método execute
                cursor.execute("SELECT * FROM local WHERE nombre_establecimiento = %s", (nombre_establecimiento,))
                local = cursor.fetchall()
                if local:
                    print(local)
                else:
                    print("El local no existe")
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método para consultar Todos los locales de la base de datos
    def consultarLocales(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos de todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM local;")
                local = cursor.fetchall()
                for local in local:
                    print(local)
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método Eliminar local por su id 
    def eliminarLocal(conexion, id_local):
        # Hacemos la consulta SQL para eliminar el local 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM local WHERE id_local =" + str(id_local)
                cursor.execute(consulta)
                print("local eliminado con exito")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
    


    def eliminarLocalPorNombre(conexion, nombre_establecimiento):
        try:
            with conexion.cursor() as cursor:
                # Usamos comillas simples alrededor del valor para asegurarnos de que sea tratado como una cadena
                consulta = "DELETE FROM local WHERE nombre_establecimiento = %s"
                cursor.execute(consulta, (nombre_establecimiento,))
                print("Local eliminado con éxito")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)



# Método para eliminar todos los locales de la base de datos 
    def eliminarLocales(conexion):
        # Hacemos la consulta SQL para eliminar todos los locales de la tabla local
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM local;")
                conexion.commit()
                print("Todos los Locales han sido eliminados exitosamente.")
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar locales: ", e) 