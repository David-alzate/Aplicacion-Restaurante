import psycopg2
from usuario import*

# Clase cocinero que hereda los atributos de usuario 
class cocinero(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo, rol):
        super().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)

    #aceptar ppedido, cambiar estado de tabla pedido y tabla producto_pedido
    def aceptarPedido(conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                # Cambiar estado del pedido a True
                consulta_pedido = "UPDATE pedido SET estado = True WHERE id_pedido = %s;"
                cursor.execute(consulta_pedido, (id_pedido,))

                # Cambiar estado de los productos asociados al pedido a True
                consulta_producto_pedido = "UPDATE producto_pedido SET estado = True WHERE id_pedido = %s;"
                cursor.execute(consulta_producto_pedido, (id_pedido,))
            
            conexion.commit()
            return True, "Pedido aceptado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al aceptar el pedido: ", e)
            return False
    
    #rechazar pedido, borrar de tabla pedido y tabla producto_pedido
    def rechazarPedido(conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                # Eliminar productos asociados al pedido en la tabla producto_pedido
                consulta_producto_pedido = "DELETE FROM producto_pedido WHERE id_pedido = %s;"
                cursor.execute(consulta_producto_pedido, (id_pedido,))

                # Luego, eliminar el pedido en la tabla pedido
                consulta_pedido = "DELETE FROM pedido WHERE id_pedido = %s;"
                cursor.execute(consulta_pedido, (id_pedido,))
            
            conexion.commit()
            return True, "Pedido rechazado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al rechazar el pedido: ", e)
            return False
