import psycopg2
from database import*
# Clase para el reporte de ventas 
class ReporteVentas:
    def __init__(self,id_pedido, fechaEmision, nombreMesero, numeroMesa, valorTotal):
        self.id_pedido = id_pedido
        self.fechaEmision = fechaEmision
        self.nombreMesero = nombreMesero
        self.numeroMesa = numeroMesa
        self.valorTotal = valorTotal
    
    # reporte de ventas, agregar a tabla reporte_ventas 
    def generarReporteVentas(conexion,id_pedido, fechaEmision, nombreMesero, numeroMesa, valorTotal):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO reporte_ventas (id_pedido, fechaEmision, nombreMesero, numeroMesa, valorTotal) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(consulta, (id_pedido, fechaEmision, nombreMesero, numeroMesa, valorTotal))
            conexion.commit()
            return True, "Reporte de ventas agregado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al agregar el reporte de ventas: ", e)

    def consultarReporteVentas(conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM reporte_ventas;")
                reporte_ventas = cursor.fetchall()
            conexion.commit()
            return reporte_ventas
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar el reporte de ventas: ", e)
            return False, None

    
conexion = Basedatos("localhost","postgres","000")
reporte = ReporteVentas.consultarReporteVentas(conexion.conectar())