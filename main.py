from database import *
from usuario import*
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class EjemploGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaPrincipal.ui",self)
        self.boton.clicked.connect(self.mostrarBoton)

    def mostrarBoton(self):
        print("Hola Mundo ")
        a = float(self.a.text())
        b = float(self.b.text())
        print(str(float(a)*float(b)))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = EjemploGUI()
    gui.show()
    sys.exit((app.exec_()))




conexion = Basedatos("localhost","postgres","000")
conexion.conectar()


if (usuario.crearUsuario(conexion.conectar(), "luis", "ospina", "lector@gmail.com", "3127054715", "cll 15", "123", "1040031815")):
    print("USUARIO CREADO EXITOSAMENTE")
else:
    print("ERROR DE CREACION")

print("Hola David Alzate")