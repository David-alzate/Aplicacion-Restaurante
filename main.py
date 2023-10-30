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

        self.btnMostrarProductoAdmin1.clicked.connect(lambda: self.cargarDatosTablaProductos())
        self.btnCrearProductoAdmin.clicked.connect(self.agregarProducto)
        

        # login Mesero
        self.btnMesero.clicked.connect(lambda: self.pgLgMesero())
        self.btnIngresarMesero.clicked.connect(self.loginMesero)


        self.btnCocinero.clicked.connect(lambda: self.pgLgCocinero())
        self.btnRegresar.clicked.connect(lambda: self.pgAnterior())
        
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

        # Ancho de tablas - Configura el redimensionamiento de las columnas
        self.tableUsuariosAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableEliminarUsuarioAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableLocalesAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableLocalesAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.tableEliminarLocalesAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableEliminarLocalesAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        self.tableProductosAdmin.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableProductosAdmin.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

      
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

    def cargarDatosTablaProductos(self):
            # Obtener los datos de la base de datos
            conexion_db = conexion.conectar()
            locales = adminGeneral.consultarProductos(conexion_db)
            conexion_db.close()
      
            # Ocultar la cabecera vertical que muestra los números de fila
            self.tableProductosAdmin.verticalHeader().setVisible(False)
      
            # Establecer los títulos de las columnas
            self.tableProductosAdmin.setColumnCount(3)
            self.tableProductosAdmin.setHorizontalHeaderLabels(["ID", "Precio", "Nombre Producto"])
                  
            # Limpiar la tabla antes de agregar nuevos datos
            self.tableProductosAdmin.setRowCount(0)
            
            if locales:
                  # Recorrer los datos de los locales y agregarlos a la tabla
                  for local in locales:
                        rowPosition = self.tableProductosAdmin.rowCount()
                        self.tableProductosAdmin.insertRow(rowPosition)
                   
                        # Insertar los datos en las celdas
                        self.tableProductosAdmin.setItem(rowPosition, 0, QTableWidgetItem(str(local[0])))
                        self.tableProductosAdmin.setItem(rowPosition, 1, QTableWidgetItem(str(local[1])))
                        self.tableProductosAdmin.setItem(rowPosition, 2, QTableWidgetItem(local[2]))
            else:
                  self.labelInfoMostrarLocalesAdmin.setText("No hay locales disponibles en la base de datos")
    
    def pgCrearPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgCrearProductoAdmin)

    def agregarProducto(self):
            # obtener los datos de los lineEdit
            nombre = self.nombreCrearProductoAdmin.text()
            precio = self.precioCrearProductoAdmin.text()
            
            # crear producto
            conexion_db = conexion.conectar()
            try:
                  resultado, mensaje = adminGeneral.crearProducto(conexion_db, precio, nombre)
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
    def pgEditarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEditarProductoAdmin)
    def pgEliminarPdAdmin(self):
          self.stackedWidget.setCurrentWidget(self.pgEliminarProductoAdmin)
     
    
      
      
   

    def pgLgMesero(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginMesero)
         self.btnRegresar.show()

    def pgMesero(self):
        self.stackedWidget.setCurrentWidget(self.pgPrincipalMesero)
        self.btnRegresar.show()

    def pgLgCocinero(self):
         self.stackedWidget.setCurrentWidget(self.pgLoginCocinero)
         self.btnRegresar.show()
    
        

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



