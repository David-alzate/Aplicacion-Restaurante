from database import *
from adminGeneral import*
from usuario import*
from login import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

# Realizamos la conexión a la base de datos
conexion = Basedatos("localhost","postgres","000")

# clase de la GUI para realizar el login 
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaPrincipal.ui",self)
        self.boton.clicked.connect(self.login)  # Al presionar el botón de la ventana llamar al método login

# Método para logrearse
    def login(self):
        # Agregamos los datos ingresados en los QlineEdit a id y contraseña
        id = self.a.text()
        password = self.b.text()
        
        # llamamos el método iniciar sesión de login para verificar el inicio de sesión
        login.iniciarSesion(conexion.conectar(),id , password)   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit((app.exec_()))



# if (adminGeneral.crearUsuario(conexion.conectar(), "luis", "ospina", "lector@gmail.com", "3127054715", "cll 15", "123", "104003185", "Cocinero")):
#      print("USUARIO CREADO EXITOSAMENTE")
# else:
#      print("ERROR DE CREACION")
