import sqlite3
import sys
import FuncionesSQL as funciones
from Pantallaproyectofinal import *
from PyQt5.QtWidgets import QTableWidgetItem
import os

class main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.datosTotal = funciones.Cancion()

        self.ui.bt_refrescar.clicked.connect(self.MostrarTabla)
        self.ui.bt_agregar.clicked.connect(self.InsertarCanciones)
        self.ui.bt_buscar.clicked.connect(self.ConsultorCanciones)
        self.ui.bt_actualizar.clicked.connect(self.ModificadorCanciones)

		
        self.ui.tabla_canciones.setColumnWidth(0,98)
        self.ui.tabla_canciones.setColumnWidth(1,100)
        self.ui.tabla_canciones.setColumnWidth(2,98)
        self.ui.tabla_canciones.setColumnWidth(3,98)
        self.ui.tabla_canciones.setColumnWidth(4,98)


        self.ui.tabla_buscar.setColumnWidth(0,98)
        self.ui.tabla_buscar.setColumnWidth(1,100)
        self.ui.tabla_buscar.setColumnWidth(2,98)
        self.ui.tabla_buscar.setColumnWidth(3,98)
        self.ui.tabla_buscar.setColumnWidth(4,98)
        self.MostrarTabla()

    def MostrarTabla(self):
        datos = self.datosTotal.ConsultarCanciones()
        i = len(datos)
        self.ui.tabla_canciones.setRowCount(i)
        tablerow=0
        for row in datos:
            self.ui.tabla_canciones.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tabla_canciones.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_canciones.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_canciones.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_canciones.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1
        self.ui.tabla_canciones.setSortingEnabled(True)


    def InsertarCanciones(self):
        codigo=self.ui.codigoA.text()
        nombre=self.ui.nombreA.text()
        genero=self.ui.generoA.text()
        album=self.ui.albumA.text()
        interprete=self.ui.interpreteA.text()

        self.datosTotal.AñadirCanciones(codigo,nombre,genero,album,interprete)
        self.ui.codigoA.clear()
        self.ui.nombreA.clear()
        self.ui.generoA.clear()
        self.ui.albumA.clear()
        self.ui.interpreteA.clear()

    def ModificadorCanciones(self):
        id_cancion = self.ui.id_cancion.text()
        id_cancion = str("'" + id_cancion + "'")
        nombreXX = self.datosTotal.ConsultaCancion(id_cancion)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            codigoM = self.ui.codigo_actualizar.text()
            nombreM = self.ui.nombre_actualizar.text()
            generoM = self.ui.genero_actualizar.text()
            albumM = self.ui.album_actualizar.text()
            interpreteM = self.ui.interprete_actualizar.text()
            act = self.datosTotal.ModificarCanciones(codigoM,nombreM , generoM, albumM, interpreteM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.codigo_actualizar.clear()
                self.ui.nombre_actualizar.clear()
                self.ui.genero_actualizar.clear()
                self.ui.album_actualizar.clear()
                self.ui.interprete_actualizar.clear()
                self.ui.id_cancion.clear()
            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")



    def ConsultorCanciones(self):
        nombre_cancion = self.ui.codigoB.text()
        nombre_cancion = str("'" + nombre_cancion + "'")
        datosB = self.datosTotal.ConsultaCancion(nombre_cancion)
        i = len(datosB)
        self.ui.tabla_buscar.setRowCount(i)
        tablerow = 0
        for row in datosB:
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



