from usuario import*

# Clase cocinero que hereda los atributos de usuario 
class cocinero(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, password, id, correo, rol):
        super().__init__(nombre, apellido, telefono, direccion, password, id, correo, rol)

    