import psycopg2
from usuario import*
from productos import*
from local import*


# clase administrador General que hereda los atributos de usuario
class adminGeneral(usuario,producto,local):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo,rol,id_producto,precio,nombreProducto,
                 idLocal,nombreEstablecimiento):
        usuario().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)
        producto().__init__(id_producto,precio,nombreProducto)
        local().__init__(idLocal,nombreEstablecimiento)

# Métodos adminGeneral.py

    def crearUsuario(conexion, nombre, apellido, correo, telefono, direccion, password, id, rol):
        # Convertir el rol a minúsculas para ingresarlo así en la base de datos
        rol = rol.lower()
        # Lista de roles permitidos
        roles_permitidos = ["administrador", "mesero", "cocinero"]
    
        # Evaluamos si el rol ingresado está dentro de la lista de roles permitidos 
        if rol not in roles_permitidos:
            mensaje = "Rol no válido"
            print(mensaje)
            return False, mensaje
        # Hacemos la consulta en SQL para ingresar el usuario a la base de datos
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuarios(nombre, apellido, correo, telefono, direccion, password, id, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, correo, telefono, direccion, password, id, rol))
            conexion.commit()
            return True, "Usuario creado exitosamente"
        except psycopg2.Error as e:
            mensaje = "Ocurrió un error al crear el usuario: " + str(e)
            print(mensaje)
            return False

    
    # Modificar usuario
    def modificarUsuario(conexion, id, nombre, apellido, correo, telefono, direccion, password, rol):
        # Convertir el rol a minúsculas para ingresarlo así en la base de datos
        rol = rol.lower()
        # Lista de roles permitidos
        roles_permitidos = ["administrador", "mesero", "cocinero"]
    
        # Evaluamos si el rol ingresado está dentro de la lista de roles permitidos 
        if rol not in roles_permitidos:
            mensaje = "Rol no válido"
            print(mensaje)
            return False, mensaje
        # Hacemos la consulta en SQL para ingresar el usuario a la base de datos
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE usuarios SET nombre = %s, apellido = %s, correo = %s, telefono = %s, direccion = %s, password = %s, rol = %s WHERE id = %s;"
                cursor.execute(consulta, (nombre, apellido, correo, telefono, direccion, password, rol, id))
            conexion.commit()
            return True, "Usuario actualizado exitosamente"
        except psycopg2.Error as e:
            mensaje = "Ocurrió un error al actualizar el usuario: " + str(e)
            print(mensaje)
            return False

# Método para Consultar un usuario por su id
    def consultarUsuario(conexion, id):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id="+str(id))
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
                else:
                    print("El usuario no existe")
                return False
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método para consultar Todos los usuarios de la base de datos
    def consultarUsuarios(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos de todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios;")
                usuarios = cursor.fetchall()
                return usuarios  # Devuelve la lista de usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método Eliminar usuario por su id 
    def eliminarUsuario(conexion, id):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuarios WHERE id =" + str(id)
                cursor.execute(consulta)
                mensaje = "Usuario eliminado con exito"
                conexion.commit()
                return True, mensaje
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
                return True, "Producto creado exitosamente"
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
                return producto  # Devuelve la lista de usuarios
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
            return True, "Local creado exitosamente"
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
    def modificarLocal(conexion, idLocal, nombreEstablecimiento):
        # Hacemos la consulta SQL para modificar el campo deseado
        try:
            with conexion.cursor() as cursor:
                # Hacemos la consulta SQL para modificar el campo
                consulta = "UPDATE local SET nombre_establecimiento = %s WHERE id_local = %s"
                cursor.execute(consulta, (nombreEstablecimiento, idLocal))
                conexion.commit()
                mensaje = ("se actualizó con éxito.")
                return True, mensaje
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
                    return local
                else:
                    print("El local no existe")
                return False
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método para consultar Todos los locales de la base de datos
    def consultarLocales(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos de todos los usuarios de la tabla usuarios 
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM local;")
                locales = cursor.fetchall()
                return locales
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

# Método Eliminar local por su id retornar true si se elimino y 
    def eliminarLocal(conexion, id_local):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM local WHERE id_local =" + str(id_local)
                cursor.execute(consulta)
                mensaje = "Local eliminado con exito"
            conexion.commit()
            return True, mensaje
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
    
    


    def eliminarLocalPorNombre(conexion, nombre_establecimiento):
        try:
            with conexion.cursor() as cursor:
                # Usamos comillas simples alrededor del valor para asegurarnos de que sea tratado como una cadena
                consulta = "DELETE FROM local WHERE nombre_establecimiento = %s"
                cursor.execute(consulta, (nombre_establecimiento,))
                mensaje = "Local eliminado con éxito"
            conexion.commit()
            return True, mensaje
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

    # Metodo para consultar el rol de un usuario
    def consultarRol(conexion, id):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT rol FROM usuarios WHERE id="+str(id))
                rol = cursor.fetchone()
                if rol:
                    return rol
                else:
                    men = "El usuario no existe"
                return False, men
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        
    # Metodo para comprobar si el usuario existe
    def comprobarUsuario(conexion, id):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id="+str(id))
                usuario = cursor.fetchone()
                # Verificar que el usuario exista
                if usuario:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
            return False


