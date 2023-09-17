from usuario import*

# Clase mesero que hereda los atributos de usuario 
class mesero(usuario):
    def __init__(self, nombre, apellido, telefono, direccion, contraseña, id, correo, rol):
        super().__init__(nombre, apellido, telefono, direccion, contraseña, id, correo, rol)

    