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
        self.btnRegresar.hide()

        # coneccion botones

        # Login Administrador 
        self.btnAdministrador.clicked.connect(lambda: self.pgLgAdmin())
        # CRUD Usuarios
        self.btnUsuariosAdmin.clicked.connect(lambda: self.pgMostrarUsuAdmin())
        self.btnMostrarUsuarioAdmin1.clicked.connect(lambda: self.pgMostrarUsuAdmin())
        self.btnCrearUsuarioAdmin1.clicked.connect(lambda: self.pgCrearUsuAdmin())
        self.btnEditarUsuarioAdmin1.clicked.connect(lambda: self.pgEditarUsuAdmin())
        self.btnEliminarUsuarioAdmin1.clicked.connect(lambda: self.pgEliminarUsuAdmin())
        self.btnCerrarSesionAdmin1.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarUsuarioAdmin1_2.clicked.connect(lambda: self.pgMostrarUsuAdmin())
        self.btnCrearUsuarioAdmin1_2.clicked.connect(lambda: self.pgCrearUsuAdmin())
        self.btnEditarUsuarioAdmin1_2.clicked.connect(lambda: self.pgEditarUsuAdmin())
        self.btnEliminarUsuarioAdmin1_2.clicked.connect(lambda: self.pgEliminarUsuAdmin())
        self.btnCerrarSesionAdmin1_2.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarUsuarioAdmin1_3.clicked.connect(lambda: self.pgMostrarUsuAdmin())
        self.btnCrearUsuarioAdmin1_3.clicked.connect(lambda: self.pgCrearUsuAdmin())
        self.btnEditarUsuarioAdmin1_3.clicked.connect(lambda: self.pgEditarUsuAdmin())
        self.btnEliminarUsuarioAdmin1_3.clicked.connect(lambda: self.pgEliminarUsuAdmin())
        self.btnCerrarSesionAdmin1_3.clicked.connect(lambda: self.pgLgAdmin())
        
        self.btnMostrarUsuarioAdmin1_4.clicked.connect(lambda: self.pgMostrarUsuAdmin())
        self.btnCrearUsuarioAdmin1_4.clicked.connect(lambda: self.pgCrearUsuAdmin())
        self.btnEditarUsuarioAdmin1_4.clicked.connect(lambda: self.pgEditarUsuAdmin())
        self.btnEliminarUsuarioAdmin1_4.clicked.connect(lambda: self.pgEliminarUsuAdmin())
        self.btnCerrarSesionAdmin1_4.clicked.connect(lambda: self.pgLgAdmin())

        #CRUD Locales
        self.btnLocalesAdmin.clicked.connect(lambda: self.pgMostrarLcAdmin())
        self.btnMostrarLocalAdmin1.clicked.connect(lambda: self.pgMostrarLcAdmin())
        self.btnCrearLocalAdmin1.clicked.connect(lambda: self.pgCrearLcAdmin())
        self.btnEditarLocalAdmin1.clicked.connect(lambda: self.pgEditarLcAdmin())
        self.btnEliminarLocalAdmin1.clicked.connect(lambda: self.pgEliminarLcAdmin())
        self.btnCerrarSesionAdmin1_5.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarLocalAdmin1_2.clicked.connect(lambda: self.pgMostrarLcAdmin())
        self.btnCrearLocalAdmin1_2.clicked.connect(lambda: self.pgCrearLcAdmin())
        self.btnEditarLocalAdmin1_2.clicked.connect(lambda: self.pgEditarLcAdmin())
        self.btnEliminarLocalAdmin1_2.clicked.connect(lambda: self.pgEliminarLcAdmin())
        self.btnCerrarSesionAdmin1_6.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarLocalAdmin1_3.clicked.connect(lambda: self.pgMostrarLcAdmin())
        self.btnCrearLocalAdmin1_3.clicked.connect(lambda: self.pgCrearLcAdmin())
        self.btnEditarLocalAdmin1_3.clicked.connect(lambda: self.pgEditarLcAdmin())
        self.btnEliminarLocalAdmin1_3.clicked.connect(lambda: self.pgEliminarLcAdmin())
        self.btnCerrarSesionAdmin1_7.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarLocalAdmin1_4.clicked.connect(lambda: self.pgMostrarLcAdmin())
        self.btnCrearLocalAdmin1_4.clicked.connect(lambda: self.pgCrearLcAdmin())
        self.btnEditarLocalAdmin1_4.clicked.connect(lambda: self.pgEditarLcAdmin())
        self.btnEliminarLocalAdmin1_4.clicked.connect(lambda: self.pgEliminarLcAdmin())
        self.btnCerrarSesionAdmin1_8.clicked.connect(lambda: self.pgLgAdmin())

        # CRUD Productos
        self.btnProductosAdmin.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnMostrarProductoAdmin1.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_9.clicked.connect(lambda: self.pgLgAdmin())

        self.btnProductosAdmin.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnMostrarProductoAdmin1_2.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_2.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_2.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_2.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_10.clicked.connect(lambda: self.pgLgAdmin())

        self.btnProductosAdmin.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnMostrarProductoAdmin1_3.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_3.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_3.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_3.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_11.clicked.connect(lambda: self.pgLgAdmin())

        self.btnProductosAdmin.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnMostrarProductoAdmin1_4.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_4.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_4.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_4.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_12.clicked.connect(lambda: self.pgLgAdmin())
        
        
        

        self.btnMesero.clicked.connect(lambda: self.pgLgMesero())
        self.btnCocinero.clicked.connect(lambda: self.pgLgCocinero())
        self.btnRegresar.clicked.connect(lambda: self.pgAnterior())
        self.btnIngresarAdmin.clicked.connect(self.login)
        self.btnCerrarSesionAdmin.clicked.connect(lambda: self.pgLgAdmin())

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

    # Metodo para regresar
    def pgAnterior(self):
         if self.stackedWidget.currentWidget() == self.pgLoginAdmin:
              self.stackedWidget.setCurrentWidget(self.pgPrincipal)
              self.usuarioAdmin.setText("")
              self.contrasenaAdmin.setText("")
              self.labelInfoLgAdmin.setText("")
              self.btnRegresar.hide()
         if self.stackedWidget.currentWidget() == self.pgLoginMesero:
               self.stackedWidget.setCurrentWidget(self.pgPrincipal)
               self.usuarioMesero.setText("")
               self.contrasenaMesero.setText("")
               self.btnRegresar.hide()
         if self.stackedWidget.currentWidget() == self.pgLoginCocinero:
               self.stackedWidget.setCurrentWidget(self.pgPrincipal)
               self.usuarioCocinero.setText("")
               self.contrasenaCocinero.setText("")
               self.btnRegresar.hide()
         if self.stackedWidget.currentWidget() == self.pgPrincipalAdmin:
              self.pgLgAdmin()
         if self.stackedWidget.currentWidget() == self.pgMostrarUsuarioAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgCrearUsuarioAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEditarUsuarioAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEliminarUsuarioAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgMostrarLocalAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgCrearLocalAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEditarLocalAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEliminarLocalAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgMostrarProductoAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgCrearProductoAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEditarProductoAdmin:
               self.pgAdmin()
         if self.stackedWidget.currentWidget() == self.pgEliminarProductoAdmin:
               self.pgAdmin()
          

    # Metodos para cambiar de ventana  
    # Administrador
    def pgLgAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginAdmin)
         self.usuarioAdmin.setText("")
         self.contrasenaAdmin.setText("")
         self.labelInfoLgAdmin.setText("")
         self.btnRegresar.show()
    # Pg Principal Administrador
    def pgAdmin(self):
        self.stackedWidget.setCurrentWidget(self.pgPrincipalAdmin)
        self.btnRegresar.show()
      
    # Cambiar a la ventana de crud usuarios
    def pgMostrarUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgMostrarUsuarioAdmin)
    def pgCrearUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgCrearUsuarioAdmin)
    def pgEditarUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEditarUsuarioAdmin)
    def pgEliminarUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEliminarUsuarioAdmin)

    # cambiar a la ventana de crud locales
    def pgMostrarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgMostrarLocalAdmin)
    def pgCrearLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgCrearLocalAdmin)
    def pgEditarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEditarLocalAdmin)
    def pgEliminarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEliminarLocalAdmin)

    # cambiar a la ventana de crud productos
    def pgMostrarPdAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgMostrarProductoAdmin)
    def pgCrearPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgCrearProductoAdmin)
    def pgEditarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEditarProductoAdmin)
    def pgEliminarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEliminarProductoAdmin)
     

      
      
   

    def pgLgMesero(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginMesero)
         self.btnRegresar.show()
    def pgLgCocinero(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginCocinero)
         self.btnRegresar.show()
    
        

    # Método para logrearse
    def login(self):
        # Agregamos los datos ingresados en los QlineEdit a id y contraseña
        id = self.usuarioAdmin.text()
        password = self.contrasenaAdmin.text()
        
        # llamamos el método iniciar sesión de login para verificar el inicio de sesión
        if login.iniciarSesion(conexion.conectar(),id , password):
            self.pgAdmin()
        else:
            self.labelInfoLgAdmin.setText("Inicio de sesión fallido")

        

    
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



# if (adminGeneral.crearUsuario(conexion.conectar(), "David", "Alzate", "Alzatedavid0126@gmail.com", "3127054715", "Calle 15", "1", "1", "administrador")):
#      print("USUARIO CREADO EXITOSAMENTE")
# else:
#      print("ERROR DE CREACION")
