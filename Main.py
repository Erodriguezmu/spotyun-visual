import sqlite3
import sys
import FuncionesSQL as funciones
from Pantallaproyectofinal import *
from PyQt5.QtWidgets import QTableWidgetItem
import os

class main(QtWidgets.QMainWindow): #clase que contiene los metodos que conectan a las funciones de sql con los labels de la interfaz grafica
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form() #Form es el nombre de la ventana del widget principal
        self.ui.setupUi(self)
        self.datosTotal = funciones.Cancion() #guarda en datosTotal los valores de la tabla cancion
        #se conecta las funciones de FuncionesSQL con los botones en la interfaz grafica
        self.ui.bt_refrescar.clicked.connect(self.MostrarTabla)
        self.ui.bt_agregar.clicked.connect(self.InsertarCanciones)
        self.ui.bt_buscar.clicked.connect(self.ConsultorCanciones)
        self.ui.bt_actualizar.clicked.connect(self.ModificadorCanciones)

	#determina el ancho de cada columna de la tabla canciones que esta en la base de datos
        self.ui.tabla_canciones.setColumnWidth(0,98)
        self.ui.tabla_canciones.setColumnWidth(1,100)
        self.ui.tabla_canciones.setColumnWidth(2,98)
        self.ui.tabla_canciones.setColumnWidth(3,98)
        self.ui.tabla_canciones.setColumnWidth(4,98)

        #aunque no sea funcional ahora, determina el ancho de la tabla buscar
        self.ui.tabla_buscar.setColumnWidth(0,98)
        self.ui.tabla_buscar.setColumnWidth(1,100)
        self.ui.tabla_buscar.setColumnWidth(2,98)
        self.ui.tabla_buscar.setColumnWidth(3,98)
        self.ui.tabla_buscar.setColumnWidth(4,98)
        self.MostrarTabla()

    def MostrarTabla(self): #funcion que carga la informacion de la tabla en el QTableWidget
        datos = self.datosTotal.ConsultarCanciones()
        i = len(datos) #obtiene la cantidad de registros en la tabla cancion
        self.ui.tabla_canciones.setRowCount(i)
        tablerow=0
        for row in datos: #llena cada uno de los campos en el QTablelabel llamado tabla_canciones
            self.ui.tabla_canciones.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tabla_canciones.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_canciones.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_canciones.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_canciones.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1
        self.ui.tabla_canciones.setSortingEnabled(True)#activa la funcion de ordenar automaticamente con dar click en el encabezado

        #las siguientes funciones no funcionan aun en el programa pero se explicara en comentarios el funcionamiento esperado
    def InsertarCanciones(self):
        codigo=self.ui.codigoA.text()#carga los datos ingresados en los cuadros de texto en cada variable
        nombre=self.ui.nombreA.text()
        genero=self.ui.generoA.text()
        album=self.ui.albumA.text()
        interprete=self.ui.interpreteA.text()
        #se añaden los datos obtenidos a la base de datos
        self.datosTotal.AñadirCanciones(codigo,nombre,genero,album,interprete)
        self.ui.codigoA.clear()# se limpia cada uno de los cuadros de texto en la interfaz grafica.
        self.ui.nombreA.clear()
        self.ui.generoA.clear()
        self.ui.albumA.clear()
        self.ui.interpreteA.clear()

    def ModificadorCanciones(self):
        id_cancion = self.ui.id_cancion.text()
        id_cancion = str("'" + id_cancion + "'")
        nombreXX = self.datosTotal.ConsultaCancion(id_cancion)#busca en consultar cancion y guarda el dato en nombre

        if nombreXX != None: #si existe en la base de datos entonces actualizara los campos ingresados en los cuadros de texto
            self.ui.id_buscar.setText("ACTUALIZAR")
            codigoM = self.ui.codigo_actualizar.text()#se cargan en variables los datos de los cuadros de texto
            nombreM = self.ui.nombre_actualizar.text()
            generoM = self.ui.genero_actualizar.text()
            albumM = self.ui.album_actualizar.text()
            interpreteM = self.ui.interprete_actualizar.text()
            act = self.datosTotal.ModificarCanciones(codigoM,nombreM , generoM, albumM, interpreteM)
            #se llama la funcion modificar canciones y dependiendo de su retorno puede indicar el estado de la modificacion
            if act == 1:# logro actualizar
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.codigo_actualizar.clear()
                self.ui.nombre_actualizar.clear()
                self.ui.genero_actualizar.clear()
                self.ui.album_actualizar.clear()
                self.ui.interprete_actualizar.clear()
                self.ui.id_cancion.clear()
            elif act == 0:# posible error por campo incorrecto
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else: #si no existe el campo a actualizar
            self.ui.id_buscar.setText("NO EXISTE")



    def ConsultorCanciones(self): #consulta la cancion por el nombre
        nombre_cancion = self.ui.codigoB.text()#guarda el nombre ingresado
        nombre_cancion = str("'" + nombre_cancion + "'")
        datosB = self.datosTotal.ConsultaCancion(nombre_cancion)#envia el dato a consultar en la base de datos
        i = len(datosB)#mide la longitud de datos que coinciden con la busqueda
        self.ui.tabla_buscar.setRowCount(i)
        tablerow = 0
        for row in datosB: #se llena la tabla con los datos encontrados
            self.ui.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1





    
app = QtWidgets.QApplication([])
win = main()
win.show()
sys.exit(app.exec())



