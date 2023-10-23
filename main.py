from database import *
from adminGeneral import*
from usuario import*
from login import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtWidgets
import os

# Realizamos la conexión a la base de datos
conexion = Basedatos("localhost","postgres","000")

# clase de la GUI para realizar el login 
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaPrincipal.ui",self)

        #Control de barra de titulos
        self.btnNormalizar.hide()
        self.btnCerrar.clicked.connect(lambda: self.close())
        self.btnMaximizar.clicked.connect(self.crontrolBtMaximizar)
        self.btnNormalizar.clicked.connect(self.crontrolBtNormalizar)
        self.btnMinimizar.clicked.connect(self.crontrolBtMinimizar)

        # Eliminar Barra de titulo y opacidad
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Redimensionar ventana
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # Mover Ventana 
        self.frameSuperior.mouseMoveEvent = self.moverVentana
        

    # Método para logrearse
    def login(self):
        # Agregamos los datos ingresados en los QlineEdit a id y contraseña
        id = self.a.text()
        password = self.b.text()
        
        # llamamos el método iniciar sesión de login para verificar el inicio de sesión
        login.iniciarSesion(conexion.conectar(),id , password)

    
    # Control de barra de titulo
    def crontrolBtMinimizar(self):
       self.showMinimized()

    def crontrolBtNormalizar(self):
       self.showNormal()
       self.btnNormalizar.hide()
       self.btnMaximizar.show()
      
    def crontrolBtMaximizar(self):
       self.showMaximized()
       self.btnMaximizar.hide()  
       self.btnNormalizar.show()
    
    # Redimensionar ventana 
    def resizeEvent(self, event):
       rect = self.rect()
       self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana 
    def mousePressEvent(self, event):
       self.clickPosition = event.globalPos()

    def moverVentana(self, event):
       if self.isMaximized() == False:
          if event.buttons() == QtCore.Qt.LeftButton:
             self.move(self.pos() + event.globalPos() - self.clickPosition)
             self.clickPosition = event.globalPos()
             event.accept()
       if event.globalPos().y() <= 10:
          self.showMaximized()
          self.btnMaximizar.hide()
          self.btnNormalizar.show()
       else:
          self.showNormal()
          self.btnNormalizar.hide()
          self.btnMaximizar.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit((app.exec_()))



# if (adminGeneral.crearUsuario(conexion.conectar(), "luis", "ospina", "lector@gmail.com", "3127054715", "cll 15", "123", "104003185", "Cocinero")):
#      print("USUARIO CREADO EXITOSAMENTE")
# else:
#      print("ERROR DE CREACION")
