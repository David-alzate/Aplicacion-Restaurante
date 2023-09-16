from database import *
from adminGeneral import*
from usuario import*
from login import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

conexion = Basedatos("localhost","postgres","000")

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaPrincipal.ui",self)
        self.boton.clicked.connect(self.login)

    def login(self):
        id = self.a.text()
        contraseña = self.b.text()
        
        login.iniciarSesion(conexion.conectar(),id , contraseña)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit((app.exec_()))


# login.iniciarSesion(conexion.conectar(),"1040031815","1040031815")



# if (adminGeneral.crearUsuario(conexion.conectar(), "luis", "ospina", "lector@gmail.com", "3127054715", "cll 15", "123", "1040031815", "Cocinero")):
#     print("USUARIO CREADO EXITOSAMENTE")
# else:
#     print("ERROR DE CREACION")

# adminGeneral.eliminarUsuarios(conexion.conectar())