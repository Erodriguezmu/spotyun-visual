#Importamos sqlite3 para poder trabajar con bases de Datos de manera mas efectiva.
import sqlite3
import os
import smtplib
from pygame import mixer


class Cancion:
    def __init__(self):
        self.database = sqlite3.connect("labasededatospooparcial.db")
        self.__codigo=None
        self.__nombre=None
        self.__genero=None
        self.__album=None
        self.__interprete=None

    def AñadirCanciones(self,codigo,nombre,genero,album,interprete):#Funcion para añadir canciones a la tabla canciones
        lector =self.database.cursor()
        lector.execute("INSERT INTO CANCIONES(CODIGO, NOMBRE, GENERO, ALBUM, INTERPRETE) ('{}', '{}','{}', '{}','{}')".format(codigo,nombre,genero,album,interprete,))
        self.database.commit()
        lector.close()

    def ModificarCanciones(self,codigo,nombre,genero,album,interprete):# funcion que permite elegir que atributo de una cancion existente desea cambiar
        lector =self.database.cursor()
        lector.execute("UPDATE CANCIONES SET NOMBRE = ?,GENERO = ?,ALBUM = ?,SET INTERPRETE = ? WHERE CODIGO = ? ".format(codigo,nombre,genero,album,interprete,))
        fila =lector.rowcount
        self.db.commit()
        lector.close()
        return fila
        
    def ConsultarCanciones(self):# se cumplen dos opciones de consulta
        lector =self.database.cursor()
        lector.execute("SELECT * FROM CANCIONES")
        cod = lector.fetchall()
        return cod
    def ConsultaCancion(self,nombre_cancion):# se cumplen dos opciones de consulta
        lector =self.database.cursor()
        lector.execute("SELECT * FROM CANCIONES WHERE NOMBRE = ?",(nombre_cancion,))
        nombre = lector.fetchall()
        lector.close()
        return nombre
            
    
