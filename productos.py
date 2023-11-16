#clase producto
from local import *

class producto(local):
    def __init__(self,nombreProducto,precio,nombreEstablecimiento):
        super().__init__(nombreEstablecimiento)
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.nombreProducto = nombreProducto

