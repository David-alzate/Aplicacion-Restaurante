from database import *
from adminGeneral import*
from mesero import*
from cocinero import*
from reporteVentas import*
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
        # QLine Passwords
        self.contrasenaAdmin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenaMesero.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenaCocinero.setEchoMode(QtWidgets.QLineEdit.Password)

        # Login Administrador 
        self.btnAdministrador.clicked.connect(lambda: self.pgLgAdmin())
        self.btnIngresarAdmin.clicked.connect(self.loginAdmin)
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

        self.btnCrearUsuarioAdmin.clicked.connect(self.agregarUsuario)
        self.btnBuscarUsuarioAdmin.clicked.connect(self.buscarUsuario)
        self.btnGuardarCambiosModificarUsuarioAdmin.clicked.connect(self.editarUsuario)
        self.btnBorrarCrearUsuarioAdmin.clicked.connect(lambda: self.borrarCrearUsuarioAdmin())
        self.btnEliminarUsuarioAdmin1_4.clicked.connect(lambda: self.CargarDatosTablaborrarUsuario())
        self.btnEliminarUsuarioAdmin.clicked.connect(self.borrarUsuario)
        self.btnActualizarTablaUsuariosAdmin.clicked.connect(lambda: self.cargarDatosTablaUsuarios())
        self.btnActualizarTablaEliminarUsuarioAdmin.clicked.connect(lambda: self.CargarDatosTablaborrarUsuario())

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

        self.btnMostrarLocalAdmin1.clicked.connect(self.cargarDatosTablaLocales)
        self.btnCrearLocalAdmin.clicked.connect(self.agregarLocal)
        self.btnBuscarLocalAdmin.clicked.connect(self.buscarLocal)
        self.guardarCambiosEditarLocalAdmin.clicked.connect(self.editarLocal)
        self.btnEliminarLocalAdmin1_4.clicked.connect(lambda: self.cargarDatosTablaLocales())
        self.btnEliminarLocalPorId.clicked.connect(self.borrarLocalPorId)
        self.btnEliminarLocalPorNombre.clicked.connect(self.borrarLocalPorNombre)
        self.btnActualizarTablaLocalesAdmin.clicked.connect(lambda: self.cargarDatosTablaLocales())
        

        # CRUD Productos
        self.btnProductosAdmin.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnMostrarProductoAdmin1.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_9.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarProductoAdmin1_2.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_2.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_2.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_2.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_10.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarProductoAdmin1_3.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_3.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_3.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_3.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_11.clicked.connect(lambda: self.pgLgAdmin())

        self.btnMostrarProductoAdmin1_4.clicked.connect(lambda: self.pgMostrarPdAdmin())
        self.btnCrearProductoAdmin1_4.clicked.connect(lambda: self.pgCrearPdAdmin())
        self.btnEditarProductoAdmin1_4.clicked.connect(lambda: self.pgEditarPdAdmin())
        self.btnEliminarProductoAdmin1_4.clicked.connect(lambda: self.pgEliminarPdAdmin())
        self.btnCerrarSesionAdmin1_12.clicked.connect(lambda: self.pgLgAdmin())
        
        self.btnMostrarProductoAdmin1.clicked.connect(lambda: self.cargarDatosTablaProductos())
        self.btnCrearProductoAdmin.clicked.connect(self.agregarProducto)
        self.btnBuscarProductoAdmin.clicked.connect(self.buscarProductoPorNombre)
        self.btnGuardarCambiosEditarProductoAdmin.clicked.connect(self.editarProducto)
        self.btnEliminarProductoAdmin1_4.clicked.connect(lambda: self.cargarDatosTablaEliminarProductos())
        self.btnEliminarProductoPorNombre.clicked.connect(self.eliminarProductoPorNombre)

        self.btnEliminarPedidoMesero.clicked.connect(self.eliminarPdMesero)
        self.btnEliminarPedidoMesero.clicked.connect(lambda: self.cargarDatosTablaEliminarProductos())
        self.btnReporteVentasAdmin.clicked.connect(self.pgReporteVentasAdmin)
        self.btnActualizarTableProductosAdmin.clicked.connect(lambda: self.cargarDatosTablaProductos())
        

        # login Mesero
        self.btnMesero.clicked.connect(lambda: self.pgLgMesero())
        self.btnIngresarMesero.clicked.connect(self.loginMesero)

        # Crud Pedidos

        self.btnPedidosPendientesMesero1.clicked.connect(lambda: self.pgMostrarPdMesero())
        self.btnCrearPedidosMesero1.clicked.connect(lambda: self.pgCrearPdMesero())
        self.btnEditarPedidosMesero1.clicked.connect(lambda: self.pgEditarPdMesero())
        self.btnEliminarPedidosMesero1.clicked.connect(lambda: self.pgEliminarPdMesero())
        self.btnPedidosListosMesero1.clicked.connect(lambda: self.pgMostrarPdListosMesero())
        self.btnCerrarSesionAdmin1_13.clicked.connect(lambda: self.pgLgMesero())

        self.btnPedidosPendientesMesero1_2.clicked.connect(lambda: self.pgMostrarPdMesero())
        self.btnCrearPedidosMesero1_2.clicked.connect(lambda: self.pgCrearPdMesero())
        self.btnEditarPedidosMesero1_2.clicked.connect(lambda: self.pgEditarPdMesero())
        self.btnEliminarPedidosMesero1_2.clicked.connect(lambda: self.pgEliminarPdMesero())
        self.btnPedidosListosMesero1_2.clicked.connect(lambda: self.pgMostrarPdListosMesero())
        self.btnCerrarSesionAdmin1_14.clicked.connect(lambda: self.pgLgMesero())

        self.btnPedidosPendientesMesero1_3.clicked.connect(lambda: self.pgMostrarPdMesero())
        self.btnCrearPedidosMesero1_3.clicked.connect(lambda: self.pgCrearPdMesero())
        self.btnEditarPedidosMesero1_3.clicked.connect(lambda: self.pgEditarPdMesero())
        self.btnEliminarPedidosMesero1_3.clicked.connect(lambda: self.pgEliminarPdMesero())
        self.btnPedidosListosMesero1_3.clicked.connect(lambda: self.pgMostrarPdListosMesero())
        self.btnCerrarSesionAdmin1_15.clicked.connect(lambda: self.pgLgMesero())

        self.btnPedidosPendientesMesero1_4.clicked.connect(lambda: self.pgMostrarPdMesero())
        self.btnCrearPedidosMesero1_4.clicked.connect(lambda: self.pgCrearPdMesero())
        self.btnEditarPedidosMesero1_4.clicked.connect(lambda: self.pgEditarPdMesero())
        self.btnEliminarPedidosMesero1_4.clicked.connect(lambda: self.pgEliminarPdMesero())
        self.btnPedidosListosMesero1_4.clicked.connect(lambda: self.pgMostrarPdListosMesero())
        self.btnCerrarSesionAdmin1_16.clicked.connect(lambda: self.pgLgMesero())

        self.btnPedidosPendientesMesero1_5.clicked.connect(lambda: self.pgMostrarPdMesero())
        self.btnCrearPedidosMesero1_5.clicked.connect(lambda: self.pgCrearPdMesero())
        self.btnEditarPedidosMesero1_5.clicked.connect(lambda: self.pgEditarPdMesero())
        self.btnEliminarPedidosMesero1_5.clicked.connect(lambda: self.pgEliminarPdMesero())
        self.btnPedidosListosMesero1_5.clicked.connect(lambda: self.pgMostrarPdListosMesero())
        self.btnCerrarSesionAdmin1_17.clicked.connect(lambda: self.pgLgMesero())

        self.btnGenerarPedidoMesero.clicked.connect(self.agregarPedido)
        self.comboBoxNombreEstablecimientoCrearPedidoMesero.currentTextChanged.connect(self.cargardatoscomboBoxProductosCrearPedidoMesero)
        self.btnAgregarProductosAPedidoMesero.clicked.connect(self.agregarProductoAPedido)
        self.btnBuscarPedidoMesero.clicked.connect(self.buscarPedido)
        self.btnGuardarCambiosEditarPedidoMesero.clicked.connect(self.editarPedido)
        self.btnBuscarPedidoMesero.clicked.connect(self.cargardatostableProductos_pedidoEditarMesero)

        self.comboBoxNombreEstablecimientoEditarPedidoMesero.currentTextChanged.connect(self.cargardatoscomboBoxProductosEditarPedidoMesero)
        self.btnGuardarCambiosEditarPedidoMesero_2.clicked.connect(self.editarProductoPedido)
        self.btnGuardarCambiosEditarPedidoMesero_2.clicked.connect(self.cargardatostableProductos_pedidoEditarMesero)
        self.btnFacturarPedidoMesero.clicked.connect(self.facturarPedido)

        #Cocinero
        self.btnCocinero.clicked.connect(lambda: self.pgLgCocinero())
        self.btnIngresarCocinero.clicked.connect(self.loginCocinero)
        self.btnRegresar.clicked.connect(lambda: self.pgAnterior())
        self.btnPedidosPendientesCocinero.clicked.connect(lambda: self.cargarDatostablaProductos_pedidoCocinero())

        self.btnAceptarPedidoCocinero.clicked.connect(self.aceptarPedidoCocinero)
        self.btnRechazarPedidoCocinero.clicked.connect(self.rechazarPedidoCocinero)
        
        self.btnCerrarSesionAdmin.clicked.connect(lambda: self.pgLgAdmin())
        self.btnActualizarTablaPedidosPendientes.clicked.connect(lambda: self.cargarDatosTablaPedidos())
        self.btnActualizarPedidosListos.clicked.connect(lambda: self.cargardatosTablaPedidosListos())
        self.btnActualizarReporteVentasAdmin.clicked.connect(lambda: self.cargarDatosTablaReporteVentasAdmin())
        self.btnActualizarPedidosPendientesCocinero.clicked.connect(lambda: self.cargarDatostablaProductos_pedidoCocinero())
        self.btnCerrarSesionAdmin1_18.clicked.connect(lambda: self.pgLgCocinero())

        len(self.contrasenaCrearUsuarioAdmin.text() ) < 10

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

        # Ancho de tablas - Configura el redimensionamiento de las columnas
        self.tableUsuariosAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableEliminarUsuarioAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableLocalesAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableLocalesAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.tableEliminarLocalesAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableEliminarLocalesAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.tableProductosAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableProductosAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.tableEliminarProductosAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableEliminarProductosAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        
        self.tablePedidosMesero.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.tableProductosPedidoEditarMesero.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableEliminarPedidoMesero.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableProductosPedidoCocinero.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tablePedidosListosMesero.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableReporteVentasAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        
        

      
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
         if self.stackedWidget.currentWidget() == self.pgMostrarPedidosMesero:
               self.pgLgMesero()
         if self.stackedWidget.currentWidget() == self.pgCrearPedidosMesero:
               self.pgLgMesero()
         if self.stackedWidget.currentWidget() == self.pgEditarPedidosMesero:
                self.pgLgMesero()
         if self.stackedWidget.currentWidget() == self.pgEliminarPedidosMesero:
                self.pgLgMesero()
         if self.stackedWidget.currentWidget() == self.pgMostrarPedidosListosMesero:
                  self.pgLgMesero()
         if self.stackedWidget.currentWidget() == self.pageCocinero:
                self.pgLgCocinero()
         if self.stackedWidget.currentWidget() == self.pageReporteVentasAdmin:
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
         self.cargarDatosTablaUsuarios()

    def cargarDatosTablaUsuarios(self):
         # Obtener los datos de la base de datos
         conexion_db = conexion.conectar()
         usuarios = adminGeneral.consultarUsuarios(conexion_db)
         conexion_db.close()

         # Ocultar la cabecera vertical que muestra los números de fila
         self.tableUsuariosAdmin.verticalHeader().setVisible(False)

         # Establecer los títulos de las columnas
         self.tableUsuariosAdmin.setColumnCount(8)
         self.tableUsuariosAdmin.setHorizontalHeaderLabels(["Nombre", "Apellido", "Correo", "Teléfono", "Dirección", "ID","Contraseña", "Rol"])
            
         # Limpiar la tabla antes de agregar nuevos datos
         self.tableUsuariosAdmin.setRowCount(0)
         
         if usuarios:
            # Recorrer los datos de los usuarios y agregarlos a la tabla
            for usuario in usuarios:
                  rowPosition = self.tableUsuariosAdmin.rowCount()
                  self.tableUsuariosAdmin.insertRow(rowPosition)
                
                  # Insertar los datos en las celdas
                  self.tableUsuariosAdmin.setItem(rowPosition, 0, QTableWidgetItem(usuario[0]))  # Nombre
                  self.tableUsuariosAdmin.setItem(rowPosition, 1, QTableWidgetItem(usuario[1]))  # Apellido
                  self.tableUsuariosAdmin.setItem(rowPosition, 2, QTableWidgetItem(usuario[2]))  # Correo
                  self.tableUsuariosAdmin.setItem(rowPosition, 3, QTableWidgetItem(usuario[3]))  # Teléfono
                  self.tableUsuariosAdmin.setItem(rowPosition, 4, QTableWidgetItem(usuario[4]))  # Dirección
                  self.tableUsuariosAdmin.setItem(rowPosition, 5, QTableWidgetItem(str(usuario[5])))  # ID
                  self.tableUsuariosAdmin.setItem(rowPosition, 6, QTableWidgetItem(str(usuario[6])))  # Contraseña
                  self.tableUsuariosAdmin.setItem(rowPosition, 7, QTableWidgetItem(usuario[7]))  # Rol
         else:
             # Si no hay tareas, puedes mostrar un mensaje o tomar la acción adecuada
             self.labelInfoMostrarUsuariosAdmin.setText("No hay tareas disponibles en la base de datos")

    def pgCrearUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgCrearUsuarioAdmin)
         #Limpiar los lineEdit
         self.labelInfoCrearUsuarioAdmin.setText("")
    
    def borrarCrearUsuarioAdmin(self):
            
            
            self.nombreCrearUsuarioAdmin.setText("")
            self.apellidoCrearUsuarioAdmin.setText("")
            self.correoCrearUsuarioAdmin.setText("")
            self.telefonoCrearUsuarioAdmin.setText("")
            self.direccionCrearUsuarioAdmin.setText("")
            self.idCrearUsuarioAdmin.setText("")
            self.contrasenaCrearUsuarioAdmin.setText("")
            self.rolCrearUsuarioAdmin.setText("")
            self.labelInfoCrearUsuarioAdmin.setText("")

    def agregarUsuario(self):
         # obtener los datos de los lineEdit
         nombre = self.nombreCrearUsuarioAdmin.text()
         apellido = self.apellidoCrearUsuarioAdmin.text()
         correo = self.correoCrearUsuarioAdmin.text()
         telefono = self.telefonoCrearUsuarioAdmin.text()
         direccion = self.direccionCrearUsuarioAdmin.text()
         password = self.contrasenaCrearUsuarioAdmin.text()
         id = self.idCrearUsuarioAdmin.text()
         rol = self.rolCrearUsuarioAdmin.text()

  
         # crear usuario 
         conexion_db = conexion.conectar()
         try:
            if len(password) > 10:
                   resultado = False
                   mensaje = "La contraseña no puede tener mas de 10 caracteres"
            else:
                  resultado, mensaje = adminGeneral.crearUsuario(conexion_db, nombre, apellido, correo, telefono, direccion,password, id,  rol)
         except:
            resultado = False
            mensaje = "Ocurrió un error al crear el usuario"
         conexion_db.close()

         #Limpiar los lineEdit
         self.nombreCrearUsuarioAdmin.setText("")
         self.apellidoCrearUsuarioAdmin.setText("")
         self.correoCrearUsuarioAdmin.setText("")
         self.telefonoCrearUsuarioAdmin.setText("")
         self.direccionCrearUsuarioAdmin.setText("")
         self.idCrearUsuarioAdmin.setText("")
         self.contrasenaCrearUsuarioAdmin.setText("")
         self.rolCrearUsuarioAdmin.setText("")

         try:
            if resultado:
                  self.labelInfoCrearUsuarioAdmin.setText(mensaje)
            else:
                  self.labelInfoCrearUsuarioAdmin.setText(mensaje)
         except:
                  self.labelInfoCrearUsuarioAdmin.setText("Ocurrió un error al crear el usuario")         
         
    def pgEditarUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEditarUsuarioAdmin)
         self.labelInfoEditarUsuarioAdmin.setText("")
         self.nombreEditarUsuarioAdmin.setText("")
         self.apellidoEditarUsuarioAdmin.setText("")
         self.correoEditarUsuarioAdmin.setText("")
         self.telefonoEditarUsuarioAdmin.setText("")
         self.direccionEditarUsuarioAdmin.setText("")
         self.contrasenaEditarUsuarioAdmin.setText("")
         self.rolEditarUsuarioAdmin.setText("")
         self.labelBuscarUsuarioIdAdmin.setText("")

    def buscarUsuario(self):
            # Obtener el id del usuario a buscar
            id = self.labelBuscarUsuarioIdAdmin.text()
      
            # Buscar el usuario en la base de datos
            conexion_db = conexion.conectar()
            usuario = adminGeneral.consultarUsuario(conexion_db, id)
            conexion_db.close()
      
            # Si el usuario existe, mostrar los datos en los lineEdit
            if usuario:
                  self.nombreEditarUsuarioAdmin.setText(usuario[0])
                  self.apellidoEditarUsuarioAdmin.setText(usuario[1])
                  self.correoEditarUsuarioAdmin.setText(usuario[2])
                  self.telefonoEditarUsuarioAdmin.setText(usuario[3])
                  self.direccionEditarUsuarioAdmin.setText(usuario[4])
                  self.contrasenaEditarUsuarioAdmin.setText(str(usuario[6]))
                  self.rolEditarUsuarioAdmin.setText(usuario[7])
                  self.labelInfoEditarUsuarioAdmin.setText("") 
            else:
                  self.nombreEditarUsuarioAdmin.setText("")
                  self.apellidoEditarUsuarioAdmin.setText("")
                  self.correoEditarUsuarioAdmin.setText("")
                  self.telefonoEditarUsuarioAdmin.setText("")
                  self.direccionEditarUsuarioAdmin.setText("")
                  self.contrasenaEditarUsuarioAdmin.setText("")
                  self.rolEditarUsuarioAdmin.setText("")
                  self.labelInfoEditarUsuarioAdmin.setText("No se encontró el usuario")   

    def editarUsuario(self):
         # obtener los datos de los lineEdit
         nombre = self.nombreEditarUsuarioAdmin.text()
         apellido = self.apellidoEditarUsuarioAdmin.text()
         correo = self.correoEditarUsuarioAdmin.text()
         telefono = self.telefonoEditarUsuarioAdmin.text()
         direccion = self.direccionEditarUsuarioAdmin.text()
         id = self.labelBuscarUsuarioIdAdmin.text()
         password = self.contrasenaEditarUsuarioAdmin.text()
         rol = self.rolEditarUsuarioAdmin.text()
         
          # Modificar usuario 
         conexion_db = conexion.conectar()
         try:
            resultado, mensaje = adminGeneral.modificarUsuario(conexion_db,id, nombre, apellido, correo, telefono, direccion,password, rol)
         except:
            resultado = False
            mensaje = "Ocurrió un error al crear el usuario"
         conexion_db.close()

         #Limpiar los lineEdit
         self.nombreEditarUsuarioAdmin.setText("")
         self.apellidoEditarUsuarioAdmin.setText("")
         self.correoEditarUsuarioAdmin.setText("")
         self.telefonoEditarUsuarioAdmin.setText("")
         self.direccionEditarUsuarioAdmin.setText("")
         self.contrasenaEditarUsuarioAdmin.setText("")
         self.rolEditarUsuarioAdmin.setText("")
         

         try:
            if resultado:
                  self.labelInfoEditarUsuarioAdmin.setText(mensaje)
            else:
                  self.labelInfoEditarUsuarioAdmin.setText(mensaje)
         except:
                  self.labelInfoEditarUsuarioAdmin.setText("ocurrio un error al modificar usuario")  

    def pgEliminarUsuAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEliminarUsuarioAdmin)
         self.CargarDatosTablaborrarUsuario()
    
    def CargarDatosTablaborrarUsuario(self):
         # Obtener los datos de la base de datos
         conexion_db = conexion.conectar()
         usuarios = adminGeneral.consultarUsuarios(conexion_db)
         conexion_db.close()

         # Ocultar la cabecera vertical que muestra los números de fila
         self.tableEliminarUsuarioAdmin.verticalHeader().setVisible(False)

         # Establecer los títulos de las columnas
         self.tableEliminarUsuarioAdmin.setColumnCount(8)
         self.tableEliminarUsuarioAdmin.setHorizontalHeaderLabels(["Nombre", "Apellido", "Correo", "Teléfono", "Dirección", "ID","Contraseña", "Rol"])
            
         # Limpiar la tabla antes de agregar nuevos datos
         self.tableEliminarUsuarioAdmin.setRowCount(0)
         
         if usuarios:
            # Recorrer los datos de los usuarios y agregarlos a la tabla
            for usuario in usuarios:
                  rowPosition = self.tableEliminarUsuarioAdmin.rowCount()
                  self.tableEliminarUsuarioAdmin.insertRow(rowPosition)
                
                  # Insertar los datos en las celdas
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 0, QTableWidgetItem(usuario[0]))  # Nombre
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 1, QTableWidgetItem(usuario[1]))  # Apellido
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 2, QTableWidgetItem(usuario[2]))  # Correo
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 3, QTableWidgetItem(usuario[3]))  # Teléfono
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 4, QTableWidgetItem(usuario[4]))  # Dirección
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 5, QTableWidgetItem(str(usuario[5])))  # ID
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 6, QTableWidgetItem(str(usuario[6])))  # Contraseña
                  self.tableEliminarUsuarioAdmin.setItem(rowPosition, 7, QTableWidgetItem(usuario[7]))  # Rol
         else:
             # Si no hay tareas, puedes mostrar un mensaje o tomar la acción adecuada
             self.labelInfoEliminarUsuariosAdmin.setText("No hay tareas disponibles en la base de datos")
         
    def borrarUsuario(self):
         
    
         id = self.idEliminarUsuarioAdmin.text()

         # Eliminar usuario
         conexion_db = conexion.conectar()
         resultado, mensaje = adminGeneral.eliminarUsuario(conexion_db, id)
         conexion_db.close()

         # Mostrar mensaje de éxito o error
         if resultado:
               self.labelInfoEliminarUsuariosAdmin.setText(mensaje)
               self.CargarDatosTablaborrarUsuario()
         else:
               self.labelInfoEliminarUsuariosAdmin.setText("Ocurrió un error al eliminar el usuario")

         # Limpiar el lineEdit
         self.idEliminarUsuarioAdmin.setText("")


    # cambiar a la ventana de crud locales
    def pgMostrarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgMostrarLocalAdmin)
         self.labelInfoMostrarLocalesAdmin.setText("")
         self.cargarDatosTablaLocales()


    def cargarDatosTablaLocales(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            locales = adminGeneral.consultarLocales(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableLocalesAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableLocalesAdmin.setColumnCount(2)
            self.tableLocalesAdmin.setHorizontalHeaderLabels(["ID", "Nombre Establecimiento"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableLocalesAdmin.setRowCount(0)
            
            if locales:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for local in locales:
                        rowPosition = self.tableLocalesAdmin.rowCount()
                        self.tableLocalesAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableLocalesAdmin.setItem(rowPosition, 0, QTableWidgetItem(str(local[0])))
                        self.tableLocalesAdmin.setItem(rowPosition, 1, QTableWidgetItem(local[1]))
            else:
                  self.labelInfoMostrarLocalesAdmin.setText("No hay locales disponibles en la base de datos")

    def pgCrearLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgCrearLocalAdmin)
         self.labelInfoCrearLocalAdmin.setText("")

    def agregarLocal(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreCrearLocalAdmin.text()
            
            # crear local
            conexion_db = conexion.conectar()
            try:
                  resultado, mensaje = adminGeneral.crearLocal(conexion_db, nombre)
            except:
                  resultado = False
                  mensaje = "Ocurrió un error al crear el local"
            conexion_db.close()
      
            #Limpiar los lineEdit
            self.nombreCrearLocalAdmin.setText("")    
      
            try:
                  if resultado:
                        self.labelInfoCrearLocalAdmin.setText(mensaje)
                  else:
                        self.labelInfoCrearLocalAdmin.setText(mensaje)
            except:
                        self.labelInfoCrearLocalAdmin.setText("Ocurrió un error al crear el local")
    def pgEditarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEditarLocalAdmin)
         self.labelInfoEditarLocalAdmin.setText("")

    def buscarLocal(self):
            # Obtener el nombre del local a buscar
            nombre = self.labelBuscarLocalIdAdmin.text()
      
            # Buscar el local en la base de datos
            conexion_db = conexion.conectar()
            local = adminGeneral.consultarLocalPorNombre(conexion_db, nombre)
            conexion_db.close()
            print(local)
      
            # Si el local existe, mostrar los datos en los lineEdit
            if local:
                  self.ididEditarLocalAdmin.setText(str(local[0][0]))
                  self.nombreEditarLocalAdmin.setText(local[0][1])
                  self.labelInfoEditarLocalAdmin.setText("") 
            else:
                  self.nombreEditarLocalAdmin.setText("")
                  self.labelInfoEditarLocalAdmin.setText("No se encontro el local")
    
    def editarLocal(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreEditarLocalAdmin.text()
            id = self.ididEditarLocalAdmin.text()
            
             # Modificar local 
            conexion_db = conexion.conectar()
            try:
                  resultado, mensaje = adminGeneral.modificarLocal(conexion_db,id, nombre)
            except:
                  resultado = False
                  mensaje = "Ocurrió un error al modificar el local"
            conexion_db.close()
      
            #Limpiar los lineEdit
            self.nombreEditarLocalAdmin.setText("")
            self.ididEditarLocalAdmin.setText("")
            
      
            try:
                  if resultado:
                        self.labelInfoEditarLocalAdmin.setText(mensaje)
                  else:
                        self.labelInfoEditarLocalAdmin.setText(mensaje)
            except:
                        self.labelInfoEditarLocalAdmin.setText("ocurrio un error al modificar local")

    def pgEliminarLcAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgEliminarLocalAdmin)
         self.cargarDatosTablaEliminarLocalesLocales()
         self.labelInfoEliminarLocalAdmin.setText("")

    def cargarDatosTablaEliminarLocalesLocales(self):
         # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            locales = adminGeneral.consultarLocales(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableEliminarLocalesAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableEliminarLocalesAdmin.setColumnCount(2)
            self.tableEliminarLocalesAdmin.setHorizontalHeaderLabels(["ID", "Nombre Establecimiento"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableEliminarLocalesAdmin.setRowCount(0)
            
            if locales:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for local in locales:
                        rowPosition = self.tableEliminarLocalesAdmin.rowCount()
                        self.tableEliminarLocalesAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableEliminarLocalesAdmin.setItem(rowPosition, 0, QTableWidgetItem(str(local[0])))
                        self.tableEliminarLocalesAdmin.setItem(rowPosition, 1, QTableWidgetItem(local[1]))
            else:
                  self.labelInfoMostrarLocalesAdmin.setText("No hay locales disponibles en la base de datos")
            
    def borrarLocalPorId(self):
            # obtener los datos de los lineEdit
            id = self.idEliminarLocalAdmin.text()
            
            # Eliminar local
            conexion_db = conexion.conectar()
            resultado, mensaje = adminGeneral.eliminarLocal(conexion_db, id)
            conexion_db.close()
      
            # Mostrar mensaje de éxito o error
            if resultado:
                  self.labelInfoEliminarLocalAdmin.setText(mensaje)
                  self.cargarDatosTablaEliminarLocalesLocales()
            else:
                  self.labelInfoEliminarLocalAdmin.setText("Ocurrió un error al eliminar el local")
      
            # Limpiar el lineEdit
            self.idEliminarLocalAdmin.setText("")

    def borrarLocalPorNombre(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreEliminarLocalAdmin.text()
            
            # Eliminar local
            conexion_db = conexion.conectar()
            resultado, mensaje = adminGeneral.eliminarLocalPorNombre(conexion_db, nombre)
            conexion_db.close()
      
            # Mostrar mensaje de éxito o error
            if resultado:
                  self.labelInfoEliminarLocalAdmin.setText(mensaje)
                  self.cargarDatosTablaEliminarLocalesLocales()
            else:
                  self.labelInfoEliminarLocalAdmin.setText("Ocurrió un error al eliminar el local")
      
            # Limpiar el lineEdit
            self.nombreEliminarLocalAdmin.setText("")

    # cambiar a la ventana de crud productos    
    def pgMostrarPdAdmin(self):
         self.stackedWidget.setCurrentWidget(self.pgMostrarProductoAdmin)
         self.cargarDatosTablaProductos()
         self.labelInfoMostrarProductosAdmin.setText("")

    def cargarDatosTablaProductos(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            productos = adminGeneral.consultarProductos(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableProductosAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableProductosAdmin.setColumnCount(3)
            self.tableProductosAdmin.setHorizontalHeaderLabels(["Nombre", "Precio", "Nombre Establecimiento"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableProductosAdmin.setRowCount(0)
            
            if productos:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for producto in productos:
                        rowPosition = self.tableProductosAdmin.rowCount()
                        self.tableProductosAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableProductosAdmin.setItem(rowPosition, 0, QTableWidgetItem(producto[0]))
                        self.tableProductosAdmin.setItem(rowPosition, 1, QTableWidgetItem(str(producto[1])))
                        self.tableProductosAdmin.setItem(rowPosition, 2, QTableWidgetItem(producto[2]))

            else:
                  self.labelInfoMostrarProductosAdmin.setText("No hay productos disponibles en la base de datos")
    
    def pgCrearPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgCrearProductoAdmin)
          self.cargarDatosComboBoxCrearPdAdmin()
          self.labelInfoCrearProductoAdmin.setText("")

    def agregarProducto(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreCrearProductoAdmin.text()
            precio = self.precioCrearProductoAdmin.text()
            nombreEstablecimiento = self.nombreEstablecimientoCrearProductoAdmin.currentText()
            
            # crear producto
            conexion_db = conexion.conectar()   
            try:
                  resultado, mensaje = adminGeneral.crearProducto(conexion_db,nombre, precio, nombreEstablecimiento)
            except:
                  resultado = False
                  mensaje = "Ocurrió un error al crear el producto"
            conexion_db.close()
      
            #Limpiar los lineEdit
            self.nombreCrearProductoAdmin.setText("")    
            self.precioCrearProductoAdmin.setText("")    
      
            try:
                  if resultado:
                        self.labelInfoCrearProductoAdmin.setText(mensaje)
                  else:
                        self.labelInfoCrearProductoAdmin.setText(mensaje)
            except:
                        self.labelInfoCrearProductoAdmin.setText("Ocurrió un error al crear el producto")
    
    def cargarDatosComboBoxCrearPdAdmin(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            locales = adminGeneral.consultarLocales(conexion_db)
            conexion_db.close()
      
            # Limpiar el comboBox antes de agregar nuevos datos
            self.nombreEstablecimientoCrearProductoAdmin.clear()
            
            if locales:
                  # Recorrer los datos de los locales y agregarlos al comboBox
                  for local in locales:
                        self.nombreEstablecimientoCrearProductoAdmin.addItem(local[1])
            else:
                  self.labelInfoCrearProductoAdmin.setText("No hay Productos disponibles en la base de datos")
    
    def pgEditarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEditarProductoAdmin)
          self.cargarDatosComboBoxEditarPdAdmin()
          self.labelInfoEditarProductoAdmin.setText("")


    def cargarDatosComboBoxEditarPdAdmin(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            locales = adminGeneral.consultarLocales(conexion_db)
            conexion_db.close()
      
            # Limpiar el comboBox antes de agregar nuevos datos
            self.nombreEstablecimientoCrearProductoAdmin_2.clear()
            
            if locales:
                  # Recorrer los datos de los locales y agregarlos al comboBox
                  for local in locales:
                        self.nombreEstablecimientoCrearProductoAdmin_2.addItem(local[1])
            else:
                  self.labelInfoCrearProductoAdmin.setText("No hay Productos disponibles en la base de datos")

    def buscarProductoPorNombre(self):
            # Obtener el nombre del producto a buscar
            nombre = self.labelBuscarProductoNombreAdmin.text()
      
            # Buscar el producto en la base de datos
            conexion_db = conexion.conectar()
            producto = adminGeneral.consultarProductoPorNombre(conexion_db, nombre)
            conexion_db.close()
      
            # Si el producto existe, mostrar los datos en los lineEdit
            if producto:
                  self.nombreEditarProductoAdmin.setText(producto[0][0])
                  self.precioEditarProductoAdmin.setText(str(producto[0][1]))
                  self.nombreEstablecimientoCrearProductoAdmin_2.setCurrentText(producto[0][2])
                  
                  self.labelInfoEditarProductoAdmin.setText("") 
            else:
                  self.nombreEditarProductoAdmin.setText("")
                  self.labelInfoEditarProductoAdmin.setText("No se encontro el producto")
    
    def editarProducto(self):
            # obtener los datos de los lineEdit
            nombreproducto = self.nombreEditarProductoAdmin.text()
            precio = self.precioEditarProductoAdmin.text()
            nombreEstablecimiento = self.nombreEstablecimientoCrearProductoAdmin_2.currentText()
            
             # Modificar producto 
            conexion_db = conexion.conectar()
            try:
                  resultado, mensaje = adminGeneral.modificarProducto(conexion_db, precio, nombreEstablecimiento, nombreproducto)
            except:
                  resultado = False
                  mensaje = "Ocurrió un error al modificar el producto"
            conexion_db.close()
      
            #Limpiar los lineEdit
            self.nombreEditarProductoAdmin.setText("")
            self.precioEditarProductoAdmin.setText("")
            
      
            try:
                  if resultado:
                        self.labelInfoEditarProductoAdmin.setText(mensaje)
                  else:
                        self.labelInfoEditarProductoAdmin.setText(mensaje)
            except:
                        self.labelInfoEditarProductoAdmin.setText("ocurrio un error al modificar producto")
          
    def pgEliminarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEliminarProductoAdmin)
          self.cargarDatosTablaEliminarProductos()
          self.labelInfoEliminarProductoAdmin.setText("")

    def cargarDatosTablaEliminarProductos(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            productos = adminGeneral.consultarProductos(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableEliminarProductosAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableEliminarProductosAdmin.setColumnCount(3)
            self.tableEliminarProductosAdmin.setHorizontalHeaderLabels(["Nombre", "Precio", "Nombre Establecimiento"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableEliminarProductosAdmin.setRowCount(0)
            
            if productos:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for producto in productos:
                        rowPosition = self.tableEliminarProductosAdmin.rowCount()
                        self.tableEliminarProductosAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableEliminarProductosAdmin.setItem(rowPosition, 0, QTableWidgetItem(producto[0]))
                        self.tableEliminarProductosAdmin.setItem(rowPosition, 1, QTableWidgetItem(str(producto[1])))
                        self.tableEliminarProductosAdmin.setItem(rowPosition, 2, QTableWidgetItem(producto[2]))

            else:
                  self.labelInfoMostrarLocalesAdmin.setText("No hay locales disponibles en la base de datos")
     
      
    def eliminarProductoPorNombre(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreEliminarProductoAdmin.text()
            
            # Eliminar producto
            conexion_db = conexion.conectar()
            resultado, mensaje = adminGeneral.eliminarProductoPorNombre(conexion_db, nombre)
            conexion_db.close()
      
            # Mostrar mensaje de éxito o error
            if resultado:
                  self.labelInfoEliminarProductoAdmin.setText(mensaje)
                  self.cargarDatosTablaEliminarProductos()
            else:
                  self.labelInfoEliminarProductoAdmin.setText("Ocurrió un error al eliminar el producto")
      
            # Limpiar el lineEdit
            self.nombreEliminarProductoAdmin.setText("")
    
    def pgReporteVentasAdmin(self):
              self.stackedWidget.setCurrentWidget(self.pageReporteVentasAdmin)
              self.labelInfoReporteVentasAdmin.setText("")
              self.btnRegresar.show()
              self.cargarDatosTablaReporteVentasAdmin()
     
    def cargarDatosTablaReporteVentasAdmin(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            ventas = ReporteVentas.consultarReporteVentas(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableReporteVentasAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableReporteVentasAdmin.setColumnCount(6)
            self.tableReporteVentasAdmin.setHorizontalHeaderLabels(["ID Reporte", "ID Pedido", "Fecha","Nombre Mesero", "Numero Mesa", "Total"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableReporteVentasAdmin.setRowCount(0)
            
            if ventas:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for venta in ventas:
                        rowPosition = self.tableReporteVentasAdmin.rowCount()
                        self.tableReporteVentasAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableReporteVentasAdmin.setItem(rowPosition, 0, QTableWidgetItem(str(venta[0])))
                        self.tableReporteVentasAdmin.setItem(rowPosition, 1, QTableWidgetItem(str(venta[1])))
                        self.tableReporteVentasAdmin.setItem(rowPosition, 2, QTableWidgetItem(str(venta[2])))
                        self.tableReporteVentasAdmin.setItem(rowPosition, 3, QTableWidgetItem(venta[3]))
                        self.tableReporteVentasAdmin.setItem(rowPosition, 4, QTableWidgetItem(str(venta[4])))
                        self.tableReporteVentasAdmin.setItem(rowPosition, 5, QTableWidgetItem(str(venta[5])))
                        

            else:
                  self.labelInfoReporteVentasAdmin.setText("No hay ventas disponibles en la base de datos")

          
      
      

    def pgLgMesero(self):     
         self.stackedWidget.setCurrentWidget(self.pgLoginMesero)
         self.usuarioMesero.setText("")
         self.contrasenaMesero.setText("")
         self.btnRegresar.show()

    def pgMesero(self):
        self.stackedWidget.setCurrentWidget(self.pgMostrarPedidosMesero)
        self.cargarDatosTablaPedidos()
        self.btnRegresar.show()

    def pgMostrarPdMesero(self):
            self.stackedWidget.setCurrentWidget(self.pgMostrarPedidosMesero)
            self.cargarDatosTablaPedidos()

    def cargarDatosTablaPedidos(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            pedidos = Mesero.consultarPedidos(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tablePedidosMesero.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tablePedidosMesero.setColumnCount(5)
            self.tablePedidosMesero.setHorizontalHeaderLabels(["ID", "Deseos del Cliente", "Fecha de Emisión", "Nombre del Mesero", "Mesa"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tablePedidosMesero.setRowCount(0)
            
            if pedidos:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for pedido in pedidos:
                        rowPosition = self.tablePedidosMesero.rowCount()
                        self.tablePedidosMesero.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tablePedidosMesero.setItem(rowPosition, 0, QTableWidgetItem(str(pedido[0])))
                        self.tablePedidosMesero.setItem(rowPosition, 1, QTableWidgetItem(pedido[1]))
                        self.tablePedidosMesero.setItem(rowPosition, 2, QTableWidgetItem(str(pedido[2])))
                        self.tablePedidosMesero.setItem(rowPosition, 3, QTableWidgetItem(pedido[3]))
                        self.tablePedidosMesero.setItem(rowPosition, 4, QTableWidgetItem(str(pedido[5])))

            else:
                  self.labelInfoMostrarPedidosMesero.setText("No hay pedidos disponibles en la base de datos")

    def pgCrearPdMesero(self):
            self.stackedWidget.setCurrentWidget(self.pgCrearPedidosMesero)
            self.cargardatosComboBoxNombreMesero()
            self.fechaEmisionCrearPedidoMesero.setDate(QtCore.QDate.currentDate())
            self.cargardatoscomboBoxNombreEstablecimientoCrearPedidoMesero()
            self.cargardatoscomboBoxProductosCrearPedidoMesero()
            
    def  agregarPedido(self):
          deseosCliente = self.deseosClienteCrearPedidoMesero.text()
          fechaEmision = self.fechaEmisionCrearPedidoMesero.date().toPyDate()
          nombreMesero = self.comboBoxnombreMeseroCrearPedidoMesero.currentText()
          mesa = self.mesaCrearPedidoMesero.text()

          conexion_db = conexion.conectar()
          try:
                resultado, id_pedido = Mesero.crearPedido(conexion_db, deseosCliente, fechaEmision, nombreMesero, mesa)
          except:
                  resultado = False
                  id_pedido = None
          conexion_db.close()

          #limpiar los lineEdit
          self.deseosClienteCrearPedidoMesero.setText("")
          self.fechaEmisionCrearPedidoMesero.setDate(QtCore.QDate.currentDate())
          self.comboBoxnombreMeseroCrearPedidoMesero.setCurrentText("")
          self.mesaCrearPedidoMesero.setText("")

          try:
                if resultado:
                      self.labelInfoCrearPedidoMesero.setText("Pedido creado con éxito")
                      self.idDePedidoMesero.setText(str(id_pedido))
                else:
                      self.labelInfoCrearPedidoMesero.setText("Ocurrió un error al crear el pedido")
            
          except:
                  self.labelInfoCrearPedidoMesero.setText("Ocurrió un error al crear el pedido")
                
    def cargardatosComboBoxNombreMesero(self):
                # Obtener los datos de la base de datos
                  conexion_db = conexion.conectar()
                  meseros = Mesero.consultarMeseros(conexion_db)
                  conexion_db.close()
            
                  # Limpiar el comboBox antes de agregar nuevos datos
                  self.comboBoxnombreMeseroCrearPedidoMesero.clear()
                  
                  if meseros:
                        # Recorrer los datos de los locales y agregarlos al comboBox
                        for mesero in meseros:
                              self.comboBoxnombreMeseroCrearPedidoMesero.addItem(mesero[0])
                  else:
                        self.labelInfoCrearPedidoMesero.setText("No hay meseros disponibles en la base de datos")        
    
    def cargardatoscomboBoxNombreEstablecimientoCrearPedidoMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    locales = adminGeneral.consultarLocales(conexion_db)
                    conexion_db.close()
                  
                    # Limpiar el comboBox antes de agregar nuevos datos
                    self.comboBoxNombreEstablecimientoCrearPedidoMesero.clear()
                    
                    if locales:
                              # Recorrer los datos de los locales y agregarlos al comboBox
                              for local in locales:
                                self.comboBoxNombreEstablecimientoCrearPedidoMesero.addItem(local[1])
                    else:
                              self.labelInfoCrearPedidoMesero.setText("No hay locales disponibles en la base de datos")
    
    def cargardatoscomboBoxProductosCrearPedidoMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    nombreEstablecimiento = self.comboBoxNombreEstablecimientoCrearPedidoMesero.currentText()
                    productos = adminGeneral.consultarProductoPorNombreEstablecimiento(conexion_db, nombreEstablecimiento)
                    conexion_db.close()
                  
                    # Limpiar el comboBox antes de agregar nuevos datos
                    self.comboBoxProductosCrearPedidoMesero.clear()
                    
                    if productos:
                              # Recorrer los datos de los locales y agregarlos al comboBox
                              for producto in productos:
                                self.comboBoxProductosCrearPedidoMesero.addItem(producto[0])
                    else:
                              pass

    def agregarProductoAPedido(self):
          id_pedido = self.idDePedidoMesero_2.text()
          nombreProducto = self.comboBoxProductosCrearPedidoMesero.currentText()
          cantidad = self.cantidadCrearPedidoMesero.text()

          conexion_db = conexion.conectar()
          try:
                resultado, mensaje = Mesero.agregarProducto(conexion_db, nombreProducto, cantidad, id_pedido)
          except:
                  resultado = False
                  mensaje = "Ocurrió un error al agregar el producto al pedido"
          conexion_db.close()

          #limpiar los lineEdit
          self.cantidadCrearPedidoMesero.setText("")

          try:
                if resultado:
                      self.labelInfoCrearPedidoMesero.setText(mensaje)
                else:
                      self.labelInfoCrearPedidoMesero.setText(mensaje)
            
          except:
                  self.labelInfoCrearPedidoMesero.setText("Ocurrió un error al agregar el producto al pedido")     
      
    def pgEditarPdMesero(self):
            self.stackedWidget.setCurrentWidget(self.pgEditarPedidosMesero)
            self.cargarDatosComboBoxEditarNombreMesero()
            self.labelInfoEditarPedidoMesero.setText("")
            self.cargardatoscomboBoxNombreEstablecimientoEditarPedidoMesero()
            self.idProductoEditarMesero.setText("")

    def buscarPedido(self):
              id = self.idDePedidoMesero_3.text()
      
              conexion_db = conexion.conectar()
              pedido = Mesero.consultarPedido(conexion_db, id)
              conexion_db.close()
      
              if pedido:
                  self.deseosClienteEditarPedidoMesero.setText(str(pedido[1]))
                  self.fechaEmisionEditarPedidoMesero.setDate(QtCore.QDate.fromString(str(pedido[2]), "yyyy-MM-dd"))
                  self.comboBoxnombreMeseroEditarPedidoMesero.setCurrentText(pedido[3])
                  self.mesaEditarPedidoMesero.setText(str(pedido[5]))
                  self.labelInfoEditarPedidoMesero.setText("")
              else:
                  self.deseosClienteEditarPedidoMesero.setText("")
                  self.fechaEmisionEditarPedidoMesero.setDate(QtCore.QDate.currentDate())
                  self.comboBoxnombreMeseroEditarPedidoMesero.setCurrentText("")
                  self.mesaEditarPedidoMesero.setText("")
                  self.labelInfoEditarPedidoMesero.setText("No se encontro el pedido")

    def cargarDatosComboBoxEditarNombreMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    meseros = Mesero.consultarMeseros(conexion_db)
                    conexion_db.close()
                  
                    # Limpiar el comboBox antes de agregar nuevos datos
                    self.comboBoxnombreMeseroEditarPedidoMesero.clear()
                    
                    if meseros:
                              # Recorrer los datos de los locales y agregarlos al comboBox
                              for mesero in meseros:
                                self.comboBoxnombreMeseroEditarPedidoMesero.addItem(mesero[0])
                    else:
                              self.labelInfoEditarPedidoMesero.setText("No hay meseros disponibles en la base de datos")

    def editarPedido(self):
              id = self.idDePedidoMesero_3.text()
              deseosCliente = self.deseosClienteEditarPedidoMesero.text()
              fechaEmision = self.fechaEmisionEditarPedidoMesero.date().toPyDate()
              nombreMesero = self.comboBoxnombreMeseroEditarPedidoMesero.currentText()
              mesa = self.mesaEditarPedidoMesero.text()
      
              conexion_db = conexion.conectar()
              try:
                  resultado, mensaje = Mesero.modificarPedido(conexion_db, id, deseosCliente, fechaEmision, nombreMesero, mesa)
              except:
                    resultado = False
                    mensaje = "Ocurrió un error al modificar el pedido"
              conexion_db.close()
      
              #limpiar los lineEdit
              self.deseosClienteEditarPedidoMesero.setText("")
              self.fechaEmisionEditarPedidoMesero.setDate(QtCore.QDate.currentDate())
              self.comboBoxnombreMeseroEditarPedidoMesero.setCurrentText("")
              self.mesaEditarPedidoMesero.setText("")
      
              try:
                  if resultado:
                          self.labelInfoEditarPedidoMesero.setText(mensaje)
                  else:
                          self.labelInfoEditarPedidoMesero.setText(mensaje)
                  
              except:
                    self.labelInfoEditarPedidoMesero.setText("Ocurrió un error al modificar el pedido")

    def cargardatoscomboBoxNombreEstablecimientoEditarPedidoMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    locales = adminGeneral.consultarLocales(conexion_db)
                    conexion_db.close()
                  
                    # Limpiar el comboBox antes de agregar nuevos datos
                    self.comboBoxNombreEstablecimientoEditarPedidoMesero.clear()
                    
                    if locales:
                              # Recorrer los datos de los locales y agregarlos al comboBox
                              for local in locales:
                                self.comboBoxNombreEstablecimientoEditarPedidoMesero.addItem(local[1])
                    else:
                              self.labelInfoEditarPedidoMesero.setText("No hay locales disponibles en la base de datos")
    def cargardatoscomboBoxProductosEditarPedidoMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    nombreEstablecimiento = self.comboBoxNombreEstablecimientoEditarPedidoMesero.currentText()
                    productos = adminGeneral.consultarProductoPorNombreEstablecimiento(conexion_db, nombreEstablecimiento)
                    conexion_db.close()
                  
                    # Limpiar el comboBox antes de agregar nuevos datos
                    self.comboBoxProductosEditarPedidoMesero.clear()
                    
                    if productos:
                              # Recorrer los datos de los locales y agregarlos al comboBox
                              for producto in productos:
                                self.comboBoxProductosEditarPedidoMesero.addItem(producto[0])
                    else:
                              pass

    def cargardatostableProductos_pedidoEditarMesero(self):
                  id = self.idDePedidoMesero_3.text()
            
                  conexion_db = conexion.conectar()
                  productos = Mesero.consultarProducto_pedido(conexion_db, id)
                  conexion_db.close()
            
                  # Ocultar la cabecera vertical que muestra los números de fila
                  self.tableProductosPedidoEditarMesero.verticalHeader().setVisible(False)
            
                  # Establecer los títulos de las columnas
                  self.tableProductosPedidoEditarMesero.setColumnCount(3)
                  self.tableProductosPedidoEditarMesero.setHorizontalHeaderLabels(["ID Producto", "Nombre" , "Cantidad"])
                        
                  # Limpiar la tabla antes de agregar nuevos datos
                  self.tableProductosPedidoEditarMesero.setRowCount(0)
                  
                  if productos:
                        # Recorrer los datos de los locales y agregarlos a la tabla
                        for producto in productos:
                              rowPosition = self.tableProductosPedidoEditarMesero.rowCount()
                              self.tableProductosPedidoEditarMesero.insertRow(rowPosition)
                         
                              # Insertar los datos en las celdas
                              self.tableProductosPedidoEditarMesero.setItem(rowPosition, 0, QTableWidgetItem(str(producto[0])))
                              self.tableProductosPedidoEditarMesero.setItem(rowPosition, 1, QTableWidgetItem(str(producto[1])))
                              self.tableProductosPedidoEditarMesero.setItem(rowPosition, 2, QTableWidgetItem(str(producto[2])))
                  else:
                        self.labelInfoEditarPedidoMesero_2.setText("No hay productos disponibles en la base de datos")

    def editarProductoPedido(self):
                  id_producto = self.idProductoEditarMesero.text()
                  nombreProducto = self.comboBoxProductosEditarPedidoMesero.currentText()
                  cantidad = self.cantidadEditarPedidoMesero.text()
            
                  conexion_db = conexion.conectar()
                  try:
                        resultado, mensaje = Mesero.modificarProducto_pedido(conexion_db, id_producto, nombreProducto, cantidad)
                  except:
                        resultado = False
                        mensaje = "Ocurrió un error al modificar el producto del pedido"
                  conexion_db.close()
            
                  #limpiar los lineEdit
                  self.cantidadEditarPedidoMesero.setText("")
            
                  try:
                        if resultado:
                              self.labelInfoEditarPedidoMesero_2.setText(mensaje)
                        else:
                              self.labelInfoEditarPedidoMesero_2.setText(mensaje)
                        
                  except:
                        self.labelInfoEditarPedidoMesero_2.setText("Ocurrió un error al modificar el producto del pedido")
    def pgEliminarPdMesero(self):
            self.stackedWidget.setCurrentWidget(self.pgEliminarPedidosMesero)
            self.cargardatostableEliminarPedidoMesero()

    def eliminarPdMesero(self):
            id = self.idDePedidoMesero_4.text()
            
            # Eliminar local
            conexion_db = conexion.conectar()
            resultado, mensaje = Mesero.eliminarPedido(conexion_db, id)
            conexion_db.close()
      
            # Mostrar mensaje de éxito o error
            if resultado:
                  self.labelInfoEliminarPedidoMesero.setText(mensaje)
                  self.cargardatostableEliminarPedidoMesero()
            else:
                  self.labelInfoEliminarPedidoMesero.setText("Ocurrió un error al eliminar el pedido")
      
            # Limpiar el lineEdit
            self.idDePedidoMesero_4.setText("")

    def cargardatostableEliminarPedidoMesero(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    pedidos = Mesero.consultarPedidos(conexion_db)
                    conexion_db.close()
              
                    # Ocultar la cabecera vertical que muestra los números de fila
                    self.tableEliminarPedidoMesero.verticalHeader().setVisible(False)
              
                    # Establecer los títulos de las columnas
                    self.tableEliminarPedidoMesero.setColumnCount(5)
                    self.tableEliminarPedidoMesero.setHorizontalHeaderLabels(["ID", "Deseos del Cliente", "Fecha de Emisión", "Nombre del Mesero", "Mesa"])
                          
                    # Limpiar la tabla antes de agregar nuevos datos
                    self.tableEliminarPedidoMesero.setRowCount(0)
                    
                    if pedidos:
                              # Recorrer los datos de los locales y agregarlos a la tabla
                              for pedido in pedidos:
                                    rowPosition = self.tableEliminarPedidoMesero.rowCount()
                                    self.tableEliminarPedidoMesero.insertRow(rowPosition)
                               
                                    # Insertar los datos en las celdas
                                    self.tableEliminarPedidoMesero.setItem(rowPosition, 0, QTableWidgetItem(str(pedido[0])))
                                    self.tableEliminarPedidoMesero.setItem(rowPosition, 1, QTableWidgetItem(pedido[1]))
                                    self.tableEliminarPedidoMesero.setItem(rowPosition, 2, QTableWidgetItem(str(pedido[2])))
                                    self.tableEliminarPedidoMesero.setItem(rowPosition, 3, QTableWidgetItem(pedido[3]))
                                    self.tableEliminarPedidoMesero.setItem(rowPosition, 4, QTableWidgetItem(str(pedido[5])))

                    else:
                              self.labelInfoEliminarPedidoMesero.setText("No hay pedidos disponibles en la base de datos")
    
    def pgMostrarPdListosMesero(self):
            self.stackedWidget.setCurrentWidget(self.pgMostrarPedidosListosMesero)
            self.cargardatosTablaPedidosListos()
    
    def cargardatosTablaPedidosListos(self):
                  # Obtener los datos de la base de datos
                    conexion_db = conexion.conectar()
                    pedidos = Mesero.consultarPedidosListos(conexion_db)
                    conexion_db.close()
              
                    # Ocultar la cabecera vertical que muestra los números de fila
                    self.tablePedidosListosMesero.verticalHeader().setVisible(False)
              
                    # Establecer los títulos de las columnas
                    self.tablePedidosListosMesero.setColumnCount(5)
                    self.tablePedidosListosMesero.setHorizontalHeaderLabels(["ID", "Deseos del Cliente", "Fecha de Emisión", "Nombre del Mesero", "Mesa"])
                          
                    # Limpiar la tabla antes de agregar nuevos datos
                    self.tablePedidosListosMesero.setRowCount(0)
                    
                    if pedidos:
                              # Recorrer los datos de los locales y agregarlos a la tabla
                              for pedido in pedidos:
                                    rowPosition = self.tablePedidosListosMesero.rowCount()
                                    self.tablePedidosListosMesero.insertRow(rowPosition)
                               
                                    # Insertar los datos en las celdas
                                    self.tablePedidosListosMesero.setItem(rowPosition, 0, QTableWidgetItem(str(pedido[0])))
                                    self.tablePedidosListosMesero.setItem(rowPosition, 1, QTableWidgetItem(pedido[1]))
                                    self.tablePedidosListosMesero.setItem(rowPosition, 2, QTableWidgetItem(str(pedido[2])))
                                    self.tablePedidosListosMesero.setItem(rowPosition, 3, QTableWidgetItem(pedido[3]))
                                    self.tablePedidosListosMesero.setItem(rowPosition, 4, QTableWidgetItem(str(pedido[5])))

                    else:
                              self.labelInfoMostrarPedidosListosMesero.setText("No hay pedidos disponibles en la base de datos")
          
    def facturarPedido(self):
                  id = self.idDePedidoMesero_5.text()
                  valorTotal = self.valorTotalFacturarPedidoMesero.text()
                  conexion_db = conexion.conectar()
                  id_pedido, deseosCliente, fechaEmision, nombreMesero, estado, numeroMesa = Mesero.consultarPedido(conexion_db, id)
                  resultado, mensaje = ReporteVentas.generarReporteVentas(conexion_db, id_pedido, fechaEmision, nombreMesero, numeroMesa, valorTotal)
                  conexion_db.close()
            
                  # Mostrar mensaje de éxito o error
                  if resultado:
                        self.labelInfoMostrarPedidosListosMesero.setText(mensaje)
                        Mesero.eliminarPedido(conexion.conectar(), id)
                        self.cargardatosTablaPedidosListos()
                        
                  else:
                        self.labelInfoMostrarPedidosListosMesero.setText("Ocurrió un error al facturar el pedido")
            
                  # Limpiar el lineEdit
                  self.idDePedidoMesero_5.setText("")


    def pgLgCocinero(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginCocinero)
         self.btnRegresar.show()
      
    def pgCocinero(self):
         self.stackedWidget.setCurrentWidget(self.pageCocinero)
         self.btnRegresar.show()
         self.cargarDatostablaProductos_pedidoCocinero()
    
    def pgMostrarPedidosPendientesConinero(self):
            self.stackedWidget.setCurrentWidget(self.pgMostrarPedidosPendientesCocinero)
            self.cargarDatostablaProductos_pedidoCocinero()

    def cargarDatostablaProductos_pedidoCocinero(self):
                  conexion_db = conexion.conectar()
                  productos = Mesero.consultarProductos_pedido(conexion_db)
                  conexion_db.close()
            
                  # Ocultar la cabecera vertical que muestra los números de fila
                  self.tableProductosPedidoCocinero.verticalHeader().setVisible(False)
            
                  # Establecer los títulos de las columnas
                  self.tableProductosPedidoCocinero.setColumnCount(3)
                  self.tableProductosPedidoCocinero.setHorizontalHeaderLabels(["ID Pedido", "Nombre" , "Cantidad"])
                        
                  # Limpiar la tabla antes de agregar nuevos datos
                  self.tableProductosPedidoCocinero.setRowCount(0)
                  
                  if productos:
                        # Recorrer los datos de los locales y agregarlos a la tabla
                        for producto in productos:
                              rowPosition = self.tableProductosPedidoCocinero.rowCount()
                              self.tableProductosPedidoCocinero.insertRow(rowPosition)
                         
                              # Insertar los datos en las celdas
                              self.tableProductosPedidoCocinero.setItem(rowPosition, 0, QTableWidgetItem(str(producto[3])))
                              self.tableProductosPedidoCocinero.setItem(rowPosition, 1, QTableWidgetItem(str(producto[1])))
                              self.tableProductosPedidoCocinero.setItem(rowPosition, 2, QTableWidgetItem(str(producto[2])))
                  else:
                        self.labelInfoMostrarPedidosPendientesCocinero.setText("No hay productos disponibles en la base de datos")
    
    def aceptarPedidoCocinero(self):
                  id = self.idDePedidoCocinero.text()
                  conexion_db = conexion.conectar()
                  resultado, mensaje = cocinero.aceptarPedido(conexion_db, id)
                  conexion_db.close()
            
                  # Mostrar mensaje de éxito o error
                  if resultado:
                        self.labelInfoMostrarPedidosPendientesCocinero.setText(mensaje)
                        self.cargarDatostablaProductos_pedidoCocinero()
                  else:
                        self.labelInfoMostrarPedidosPendientesCocinero.setText("Ocurrió un error al aceptar el pedido")
            
                  # Limpiar el lineEdit
                  self.idDePedidoCocinero.setText("")
      
    def rechazarPedidoCocinero(self):
                  id = self.idDePedidoCocinero_2.text()
                  conexion_db = conexion.conectar()
                  resultado, mensaje = cocinero.rechazarPedido(conexion_db, id)
                  conexion_db.close()
            
                  # Mostrar mensaje de éxito o error
                  if resultado:
                        self.labelInfoMostrarPedidosPendientesCocinero.setText(mensaje)
                        self.cargarDatostablaProductos_pedidoCocinero()
                  else:
                        self.labelInfoMostrarPedidosPendientesCocinero.setText("Ocurrió un error al rechazar el pedido")
            
                  # Limpiar el lineEdit
                  self.idDePedidoCocinero.setText("")
    # Métodos para logrearse
    def loginAdmin(self):
        # Agregamos los datos ingresados en los QlineEdit a id y contraseña
        conexion_db = conexion.conectar()
        id = self.usuarioAdmin.text()
        password = self.contrasenaAdmin.text()
        rol = adminGeneral.consultarRol(conexion_db, id)
        usuario = adminGeneral.comprobarUsuario(conexion_db, id)
        try:
            if usuario:
                  if rol[0] == "administrador":
                        resultado, mensaje = login.iniciarSesion(conexion_db, id, password)
                        if resultado:
                              self.pgAdmin()
                        else:
                              self.labelInfoLgAdmin.setText(mensaje)
                  else:
                        self.labelInfoLgAdmin.setText("Login incorrecto")
            else:
                  self.labelInfoLgAdmin.setText("Usuario no existe")
        except:
             pass
        
    def loginMesero(self):
            # Agregamos los datos ingresados en los QlineEdit a id y contraseña
            conexion_db = conexion.conectar()
            id = self.usuarioMesero.text()
            password = self.contrasenaMesero.text()
            rol = adminGeneral.consultarRol(conexion_db, id)
            usuario = adminGeneral.comprobarUsuario(conexion_db, id)

            try:
                  if usuario:
                        if rol[0] == "mesero":
                              resultado, mensaje = login.iniciarSesion(conexion_db, id, password)
                              if resultado:
                                    self.pgMesero()
                              else:
                                    print("aqui")
                                    self.labelInfoLgMesero.setText(mensaje)
                        else:
                              self.labelInfoLgMesero.setText("Login incorrecto")
                  else:
                        self.labelInfoLgMesero.setText("Usuario no existe")
            except:
                   pass
        

       
    def loginCocinero(self):
            # Agregamos los datos ingresados en los QlineEdit a id y contraseña
            conexion_db = conexion.conectar()
            id = self.usuarioCocinero.text()
            password = self.contrasenaCocinero.text()
            rol = adminGeneral.consultarRol(conexion_db, id)
            usuario = adminGeneral.comprobarUsuario(conexion_db, id)

            try:
                  if usuario:
                        if rol[0] == "cocinero":
                              resultado, mensaje = login.iniciarSesion(conexion_db, id, password)
                              if resultado:
                                    self.pgCocinero()
                              else:
                                    self.labelInfoLgCocinero.setText(mensaje)
                        else:
                              self.labelInfoLgCocinero.setText("Login incorrecto")
                  else:
                        self.labelInfoLgCocinero.setText("Usuario no existe")
            except:
                   pass

             
            

    
            

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



