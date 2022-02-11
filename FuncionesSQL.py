#Importamos sqlite3 para poder trabajar con bases de Datos de manera mas efectiva.
import sqlite3
import os




class Cancion: #clase que contiene los metodos de cancion
    def __init__(self):
        self.database = sqlite3.connect("labasededatospooparcial.db")#se carga la bd
        

    def AñadirCanciones(self,codigo,nombre,genero,album,interprete):#Funcion para añadir canciones a la tabla canciones
        lector =self.database.cursor()#se llama un cursor para manipular la bd
        lector.execute("INSERT INTO CANCIONES(CODIGO, NOMBRE, GENERO, ALBUM, INTERPRETE) ('{}', '{}','{}', '{}','{}')".format(codigo,nombre,genero,album,interprete,))
        self.database.commit() #actualiza los cambios en la bd
        lector.close()

    def ModificarCanciones(self,codigo,nombre,genero,album,interprete):# funcion que permite elegir que atributo de una cancion existente desea cambiar
        lector =self.database.cursor()
        lector.execute("UPDATE CANCIONES SET NOMBRE = ?,GENERO = ?,ALBUM = ?,SET INTERPRETE = ? WHERE CODIGO = ? ".format(nombre,genero,album,interprete,codigo,))
        fila =lector.rowcount# obtiene la cantidad de filas y las retorna
        self.database.commit()
        lector.close()
        return fila
        
    def ConsultarCanciones(self):# funcion para seleccionar de canciones
        lector =self.database.cursor()
        lector.execute("SELECT * FROM CANCIONES")
        cod = lector.fetchall()#guarda la direccion donde apunta en la bd
        return cod
    def ConsultaCancion(self,nombre_cancion):#funcion para ver si la cancion esta en la bd
        lector =self.database.cursor()
        lector.execute("SELECT * FROM CANCIONES WHERE NOMBRE = ?",(nombre_cancion,))
        nombre = lector.fetchall()
        lector.close()
        return nombre
            
    
