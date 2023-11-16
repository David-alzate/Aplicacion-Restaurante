import psycopg2
from database import*
from usuario import*
from pedido import*


# Clase mesero que hereda los atributos de usuario 
class Mesero(usuario,pedido):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo, rol, id_pedido, deseosCliente,fechaEmision,nombreMesero, nombreEstablecimiento, estado, numeroMesa, nombreProducto, precio, cantidad):
        usuario().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)
        pedido().__init__(id_pedido, deseosCliente,fechaEmision,nombreMesero, nombreEstablecimiento, estado, numeroMesa, nombreProducto, precio, cantidad)
    
    
    def crearPedido(conexion, deseosCliente, fechaEmision, nombreMesero, numeroMesa):
        try:
            with conexion.cursor() as cursor:
                estado = False
                consulta = "INSERT INTO pedido (deseosCliente, fechaEmision, nombreMesero, estado, numeroMesa) VALUES (%s, %s, %s, %s, %s) RETURNING id_pedido;"
                cursor.execute(consulta, (deseosCliente, fechaEmision, nombreMesero, estado, numeroMesa))
                id_pedido = cursor.fetchone()[0]
            conexion.commit()
            return True, id_pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el pedido: ", e)
            return False, None
    
    def modificarPedido(conexion, id_pedido, deseosCliente, fechaEmision, nombreMesero, numeroMesa):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE pedido SET deseosCliente = %s, fechaEmision = %s, nombreMesero = %s, numeroMesa = %s WHERE id_pedido = %s;"
                cursor.execute(consulta, (deseosCliente, fechaEmision, nombreMesero, numeroMesa, id_pedido))
            conexion.commit()
            return True, "Pedido modificado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al modificar el pedido: ", e)
            return False
            
    def eliminarPedido(conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                # Eliminar productos asociados al pedido en la tabla producto_pedido
                consulta_producto_pedido = "DELETE FROM producto_pedido WHERE id_pedido = %s;"
                cursor.execute(consulta_producto_pedido, (id_pedido,))

                # Luego, eliminar el pedido en la tabla pedido
                consulta_pedido = "DELETE FROM pedido WHERE id_pedido = %s;"
                cursor.execute(consulta_pedido, (id_pedido,))
            
            conexion.commit()
            return True, "Pedido eliminado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al eliminar el pedido: ", e)
            return False
    
    def agregarProducto(conexion, nombreProducto, cantidad, id_pedido):
        try:
            with conexion.cursor() as cursor:
                estado = False
                consulta = "INSERT INTO producto_pedido (nombreProducto, cantidad, id_pedido, estado) VALUES (%s, %s, %s, %s);"
                cursor.execute(consulta, (nombreProducto, cantidad, id_pedido, estado))
            conexion.commit()
            return True, "Producto agregado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al agregar el producto: ", e)
            return False
        
    def consultarProducto_pedido(conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM producto_pedido WHERE id_pedido = %s;", (id_pedido,))
                producto_pedido = cursor.fetchall()
                return producto_pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    # consultar todos los productos_pedido con estado false
    def consultarProductos_pedido(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM producto_pedido WHERE estado = false;")
                productos_pedido = cursor.fetchall()
                return productos_pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
    
    def modificarProducto_pedido(conexion, id_producto_pedido, nombreProducto, cantidad):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE producto_pedido SET nombreProducto = %s, cantidad = %s WHERE id_producto_pedido = %s;"
                cursor.execute(consulta, (nombreProducto, cantidad, id_producto_pedido))
            conexion.commit()
            return True, "Producto modificado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al modificar el producto: ", e)
            return False
        
    #consultar pedidos con estado false
    def consultarPedidos(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pedido WHERE estado = false;")
                pedidos = cursor.fetchall()
                return pedidos
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
     
    #consultar pedidos con estado true
    def consultarPedidosListos(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pedido WHERE estado = true;")
                pedidos = cursor.fetchall()
                return pedidos
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
     
    def consultarProductos(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM productos_pedido p1 JOIN productos p2 ON p1.id_producto = p2.id_producto WHERE p2.estado = true;")
                productos = cursor.fetchall()
                return productos
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarPedido(conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pedido WHERE id_pedido = %s;", (id_pedido,))
                pedido = cursor.fetchone()
                return pedido
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        
     
    def consultarMeseros(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre FROM usuarios WHERE rol='mesero';")
                meseros = cursor.fetchall()
                return meseros
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
    

    
