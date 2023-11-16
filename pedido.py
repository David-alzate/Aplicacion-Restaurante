# Clase pedido
class pedido:
    def __init__(self,id_pedido, deseosCliente,fechaEmision,nombreMesero, nombreEstablecimiento, estado, numeroMesa, nombreProducto, precio, cantidad):
        self.id_pedido=id_pedido
        self.deseosCliente = deseosCliente
        self.fechaEmision = fechaEmision
        self.nombreMesero = nombreMesero
        self.nombreEstablecimiento = nombreEstablecimiento
        self.estado = estado
        self.numeroMesa = numeroMesa
        self.nombreProducto = nombreProducto
        self.preico = precio
        self.cantidad = cantidad

    