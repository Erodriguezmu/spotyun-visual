#Importamos sqlite3 para poder trabajar con bases de Datos de manera mas efectiva.
import sqlite3
import FuncionesMenu as FMenus
import os
import smtplib
from pygame import mixer
from PyQt5.QtWidgets import QTableWidgetItem
from QTable import *
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,150)
        self.ui.tableWidget.setColumnWidth(2,100)
        self.ui.tableWidget.setColumnWidth(3,150)
        self.ui.tableWidget.setColumnWidth(4,150)
        self.ui.tableWidget.setHorizontalHeaderLabels(["codigo","nombre","genero","album","interprete"])
        self.loaddata()

    def loaddata(self):
        connection=sqlite3.connect("labasededatospooparcial.db")
        #row=0
        curs= connection.cursor()
        sqlquery= "SELECT * FROM CANCIONES"
        self.ui.tableWidget.setRowCount(10)
        tablerow =0
        for row in curs.execute(sqlquery):
            self.ui.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow+=1   
        #self.ui.tableWidget.sortByColumn(0, QtCore.Qt.AscendingOrder)  # sort by the first column
        self.ui.tableWidget.setSortingEnabled(True)
app = QtWidgets.QApplication([])
win = mywindow()
win.show()
sys.exit(app.exec())

class Cancion:
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
        self.__codigo=None
        self.__nombre=None
        self.__genero=None
        self.__album=None
        self.__interprete=None
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def SetCodigo(self):
        self.__codigo = input("Digite el codigo de la cancion: ")
    def SetNombre(self):
        self.__nombre = input("Digite el nombre de la cancion: ")
    def SetGenero(self):
        self.__genero = input("Digite el genero de la cancion: ")
    def SetAlbum(self):
        self.__album = input("Digite el album de la cancion: ")
    def SetInterprete(self):
        self.__interprete = input("Digite el interprete de la cancion: ")
    def TuplaCancion(self):
        nueva_cancion = (self.__codigo,self.__nombre,self.__genero,self.__album,self.__interprete) #se crea esta tupla con todos las caracteristicas de la cancion ingresada
        return nueva_cancion


    
    """def IngresarDatosCancion(self):
         self.codigo = input("Digite el codigo de la nueva cancion: ")
         self.nombre = input("Digite el nombre de la nueva cancion: ")
         self.genero = input("Digite el genero de la nueva cancion: ")
         self.album = input("Digite el album de la nueva cancion: ")
         self.interprete = input("Digite el interprete de la nueva cancion: ")
         nueva_cancion = (self.codigo,self.nombre,self.genero,self.album,self.interprete) #se crea esta tupla con todos las caracteristicas de la cancion ingresada
         return nueva_cancion
    """
        
    def AñadirCanciones(self,nueva_cancion):#Funcion para añadir canciones a la tabla canciones
        while True:
            try:
               
                self.cursor.execute("INSERT INTO CANCIONES(CODIGO, NOMBRE, GENERO, ALBUM, INTERPRETE) VALUES(?,?,?,?,?)",nueva_cancion)
                self.db.commit()
                break
            except: #se activa cuando ingresa datos erroneos o intenta ingresar una cancion que ya existe.
                print("Ocurrido un error, por favor digite denuevo.")
                break
        os.system('cls')
    def ModificarCanciones(self):# funcion que permite elegir que atributo de una cancion existente desea cambiar
        self.cursor.execute("SELECT * FROM CANCIONES WHERE CODIGO = ?",(self.__codigo,))
        y = self.cursor.fetchall()
        x = 0
        w = 5 #el tamaño de w esta determinado por la cantidad de atributos que tiene la tabla canciones
        k = 0
        for i in range(len(y)): #separa por | las canciones mostradas
            for j in y[i]:
                if (k == w):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        print("")
        FMenus.MenuCanciones() #muestra las opciones que puede modificar de la tabla
        while True:
            try:
                a = input("¿Que desea modificar de la cancion?") #tiene que poner uno de los campos mostrados para avanzar
                break
            except:
                print("Opcion no valida, digite denuevo.")
                break
        if (a == '1'):
            self.__nombre = input("Digite el nuevo nombre: ")
            self.cursor.execute("UPDATE CANCIONES SET NOMBRE = ? WHERE CODIGO = ? ",(self.__nombre,self.__codigo,))
        if (a == '2'):
            self.__genero = input("Digite el nuevo genero: ")
            self.cursor.execute("UPDATE CANCIONES SET GENERO = ? WHERE CODIGO = ? ",(self.__genero,self.__codigo,))
            
        if (a == '3'):
            self.__album = input("Digite el nuevo album: ")
            self.cursor.execute("UPDATE CANCIONES SET ALBUM = ? WHERE CODIGO = ? ",(self.__album,self.__codigo,))
        
        if (a == '4'):
            self.__interprete = input("Digite el nuevo interprete: ")
            self.cursor.execute("UPDATE CANCIONES SET INTERPRETE = ? WHERE CODIGO = ? ",(self.__interprete,self.__codigo,))
        if (a == '5'):
            pass
        self.db.commit()
        os.system('cls')        
    def ConsultarCanciones(self):# se cumplen dos opciones de consulta
        print(''' 
        1.) Consulta de todo el modulo. 
        2.) Consulta especifica por uno de los campos.
        ''')      #el primer tipo de consulta muestra todas las canciones guardadas dependiendo del orden que elija el usuario
        print("") #la segunda opcion permite buscar uno de los registros dependiendo de la opcion elegida
        m=int(input("Elija el tipo de consulta que desea realizar:"))
        if(m == 1):
            Lista.Mostrar(self,"CANCIONES")# la funcion mostrar imprime los atributos de la tabla para facilitar la comprension de los datos mostrados
        if(m == 2):
            
            print("")
            print('''
            1.) codigo
            2.) nombre
            3.) genero
            4.) album
            5.) interprete
            ''')
            print("")
            d = []
            a = int(input("Digite la opcion de busqueda: "))
            if(a == 1):
                self.__codigo = input("Digite el codigo de la cancion: ")
                self.cursor.execute("SELECT * FROM CANCIONES WHERE CODIGO = ?",(self.__codigo,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CANCIONES")

            if (a == 2):
                self.__nombre = input("Digite el nombre de la cancion: ")
                self.cursor.execute("SELECT * FROM CANCIONES WHERE NOMBRE = ?",(self.__nombre,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CANCIONES")

            if (a == 3):
                self.__genero = input("Digite el genero de la cancion: ")
                self.cursor.execute("SELECT * FROM CANCIONES WHERE GENERO = ?",(self.__genero,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CANCIONES")

            if (a == 4):
                self.__album = input("Digite el album de la cancion: ")
                self.cursor.execute("SELECT * FROM CANCIONES WHERE ALBUM = ?",(self.__album,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CANCIONES")

            if (a == 5):
                self.__interprete = input("Digite el interprete de la cancion: ")
                self.cursor.execute("SELECT * FROM CANCIONES WHERE INTERPRETE = ?",(self.__interprete,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CANCIONES")

            b = 7 #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            k = 0
            for i in range(len(d)):
                for j in d[i]:
                    if (k == b):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
            wait = input()
            os.system('cls')

    
########################################################################
class Cliente:
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
        self.__cedula=None
        self.__nombre=None
        self.__apellido=None
        self.__pais=None
        self.__ciudad=None
        self.__celular=None
        self.__fecha=None
        self.__tarjeta=None
        self.__estado=None
        self.__plan=None

        pass
    def SetCedula(self):
        self.__cedula = input("Digite la cedula del cliente: ")
    def SetNombre(self):
        self.__nombre = input("Digite el nombre del nuevo/a cliente: ")
    def SetApellido(self):
        self.__apellido = input("Digite el apellido del nuevo/a cliente: ")
    def SetPais(self):
        self.__pais = input("Digite el pais del nuevo/a cliente: ")
    def SetCiudad(self):
        self.__ciudad = input("Digite la ciudad del nuevo/a cliente: ")
    def SetCelular(self):
        self.__celular = input("Digite el numero celular del nuevo/a cliente: ")
    def SetFecha(self):
        self.__fecha = input("Digite la fecha de pago (ddmmaa): ")
    def SetTarjeta(self):
        self.__tarjeta = input("Digite el numero de tarjeta de credito del nuevo/a cliente: ")
    def SetEstado(self):
        self.__estado = "pagado"
    def SetPlan(self):
        self.__plan = input("Digite el codigo del plan al que se suscribe este nuevo/a cliente: ")
    def TuplaCliente(self):
        nuevo_cliente = (self.__cedula,self.__nombre,self.__apellido,self.__pais,self.__ciudad,self.__celular,self.__fecha,self.__tarjeta,self.__estado,self.__plan) #se crea esta tupla con todos las caracteristicas del cliente ingresado
        return nuevo_cliente

    def AñadirClientes(self,nuevo_cliente): #añade clientes, es necesario poner los 8 datos
        while True:
            try:
                self.cursor.execute("INSERT INTO CLIENTES(CEDULA, NOMBRE, APELLIDO, PAIS, CIUDAD,  CELULAR,  FECHA,  NTARJETA, ESTADO,IDPLAN) VALUES(?,?,?,?,?,?,?,?,?,?)",nuevo_cliente)
                self.db.commit()
                break
            except:
                print("Ocurrido un error, por favor digite denuevo.")
                break
        os.system('cls')

    def BorrarClientes(self): # borra un cliente luego de ingresar su cedula.

        while True:
            try:
                self.cursor.execute("DELETE FROM CLIENTES WHERE CEDULA = ?",(self.__cedula,))
                break
            except:
                print("Cedula no existente.")
                break
        self.db.commit()
        os.system('cls')


    def ModificarClientes(self): #ingresa la cedula y luego pregunta que atributo del cliente desea modificar.
        
        self.cursor.execute("SELECT * FROM CLIENTES WHERE CEDULA = ?",(self.__cedula,))
        y = self.cursor.fetchall()
        x = 0
        w = 10 #el tamaño de w esta determinado por la cantidad de atributos que tiene la tabla clientes
        k = 0
        for i in range(len(y)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            for j in y[i]:
                if (k == w):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        print("")
        FMenus.MenuClientes()
        while True:
            try:
                a = input("¿Que desea modificar del cliente?")
                break
            except:
                print("Opcion no valida, digite denuevo.")
                break
        if (a == '1'):
            self.__nombre = input("Digite el nuevo nombre: ")
            self.cursor.execute("UPDATE CLIENTES SET NOMBRE = ? WHERE CEDULA = ? ",(self.__nombre,self.__cedula,))
        if (a == '2'):
            self.__apellido = input("Digite el nuevo apellido: ")
            self.cursor.execute("UPDATE CLIENTES SET APELLIDO = ? WHERE CEDULA = ? ",(self.__apellido,self.__cedula,))        
        if (a == '3'):
            self.__pais = input("Digite el nuevo pais: ")
            self.cursor.execute("UPDATE CLIENTES SET PAIS = ? WHERE CEDULA = ? ",(self.__pais,self.__cedula,))    
        if (a == '4'):
            self.__ciudad = input("Digite el nuevo ciudad: ")
            self.cursor.execute("UPDATE CLIENTES SET CIUDAD = ? WHERE CEDULA = ? ",(self.__ciudad,self.__cedula,))
        if (a == '5'):
            self.__celular = input("Digite el nuevo numero celular: ")
            self.cursor.execute("UPDATE CLIENTES SET  CELULAR = ? WHERE CEDULA = ? ",(self.__celular,self.__cedula,))
        if (a == '6'):
            self.__fecha = int(input("Digite la nuevo fecha de pago (ddmmaa):  "))
            self.cursor.execute("UPDATE CLIENTES SET FECHA = ? WHERE CEDULA = ? ",(self.__fecha,self.__cedula,))
        if (a == '7'):
            self.__tarjeta = input("Digite el nuevo tarjeta de credito: ")
            self.cursor.execute("UPDATE CLIENTES SET NTARJETA = ? WHERE CEDULA = ? ",(self.__tarjeta,self.__cedula,))
        if (a == '8'):
            self.__estado = input("digite el estado de pago del cliente [pagado/no pagado]: ")
            self.cursor.execute("UPDATE CLIENTES SET ESTADO = ? WHERE CEDULA = ? ",(self.__estado,self.__cedula,))
        if (a == '9'):
            pass
        self.db.commit()
        os.system('cls')

    def ConsultarClientes(self): #consultar clientes dependiendo de la opcion de busqueda.
        print('''
        1.) Consulta de todo el modulo.
        2.) Consulta especifica por uno de los campos.
        ''')    #el primer tipo de consulta muestra todas los guardados dependiendo del orden que elija el usuario
        print("") #la segunda opcion permite buscar uno de los registros dependiendo de la opcion elegida
        m=int(input("Elija el tipo de consulta que desea realizar:"))
        if(m == 1):
            Lista.Mostrar(self,"CLIENTES")
        if(m == 2):
            print("")
            print('''
            1.) cedula
            2.) nombre
            3.) apellido
            4.) pais
            5.) ciudad
            6.) # celular
            7.) fecha pago (ddmmaa)
            8.) Tarjeta credito
            9.) estado cuenta
            10.)plan
            ''')
            print("")
            d = []
            a = int(input("Digite la opcion de busqueda: "))
            if(a == 1):
                self.__cedula = input("Digite la cedula del/a cliente: ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE CEDULA = ?",(self.__cedula,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if (a == 2):
                self.__nombre = input("Digite el nombre del/a cliente: ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE NOMBRE = ?",(self.__nombre,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if (a == 3):
                self.__apellido = input("Digite el apellido del/a cliente: ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE APELLIDO = ?",(self.__apellido,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if (a == 4):
                self.__pais = int(input("Digite el pais del/a cliente: "))
                self.cursor.execute("SELECT * FROM CLIENTES WHERE PAIS = ?",(self.__pais,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if (a == 5):
                self.__ciudad = int(input("Digite la ciudad del/a cliente: "))
                self.cursor.execute("SELECT * FROM CLIENTES WHERE CIUDAD = ?",(self.__ciudad,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if(a == 6):
                self.__celular = int(input("Digite el numero celular del/a cliente: "))
                self.cursor.execute("SELECT * FROM CLIENTES WHERE CELULAR = ?",(self.__celular,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if(a == 7):
                self.__fecha = int(input("Digite la fecha del/a cliente(ddmmaa): "))
                self.cursor.execute("SELECT * FROM CLIENTES WHERE FECHA = ?",(self.__fecha,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if(a == 8):
                self.__tarjeta = input("Digite el numero de tarjeta del/a cliente: ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE TARJETA = ?",(self.__tarjeta,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            if(a == 9):
                self.__estado = input("Digite el estado de la cuenta del/a cliente [pagado/no pagado]: ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE ESTADO = ?",(self.__estado,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")
            if(a == 10):
                self.__plan = input("Digite el plan de la cuenta del/a cliente : ")
                self.cursor.execute("SELECT * FROM CLIENTES WHERE ESTADO = ?",(self.__plan,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("CLIENTES")

            b = 7
            k = 0
            for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
                for j in d[i]:
                    if (k == b):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
        wait = input()
        os.system('cls')

#####################################################################################
class Plan:
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
        self.__codigo =None
        self.__nombre =None
        self.__valor =None
        self.__cantidad =None
        pass
    def SetCodigo(self):
        self.__codigo = input("Digite el codigo del nuevo plan: ")
    def SetNombre(self):
        self.__nombre = input("Digite el nombre del nuevo plan: ")
    def SetValor(self):
        self.__valor = input("Digite el valor del nuevo plan: ")
    def SetCantidad(self):
        self.__cantidad = input("Digite el la cantidad de canciones disponibles en del nuevo plan: ")
    def TuplaPlan(self):
        nuevo_plan = (self.__codigo,self.__nombre,self.__valor,self.__cantidad) #se crea esta tupla con todos las caracteristicas del plan
        return nuevo_plan
    
    def AñadirPlanes(self,nuevo_plan): #funcion para añadir planes disponibles para clientes.
        while True:
            try:
                
                self.cursor.execute("INSERT INTO PLANES(CODIGO, NOMBRE, VALOR, CANTIDAD) VALUES(?,?,?,?)",nuevo_plan)
                self.db.commit()
                break
            except:
                print("Ocurrido un error, por favor digite denuevo.")
                break
        os.system('cls')

    def BorrarPlanes(self):
        while True:
            try:
                self.cursor.execute("DELETE FROM PLANES WHERE CODIGO = ?",(self.__codigo,))
                break
            except:
                print("Codigo no existente.")
                break
        self.db.commit()
        os.system('cls')

    def ModificarPlanes(self):
        self.cursor.execute("SELECT * FROM PLANES WHERE CODIGO = ?",(self.__codigo,))
        y = self.cursor.fetchall()
        x = 0
        w = 4
        k = 0
        for i in range(len(y)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            for j in y[i]:
                if (k == w):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        print("")
        FMenus.MenuPlanes()
        while True:
            try:
                a = input("¿Que desea modificar del plan?")
                break
            except:
                print("Opcion no valida, digite denuevo.")
                break
        if (a == '1'):
            self.__nombre = input("Digite el nuevo nombre  del plan: ")
            self.cursor.execute("UPDATE PLANES SET NOMBRE = ? WHERE CODIGO = ? ",(self.__nombre,self.__codigo,))
        if (a == '2'):
            self.__valor = int(input("Digite el valor nuevo  del plan: "))
            self.cursor.execute("UPDATE PLANES SET VALOR = ? WHERE CODIGO = ? ",(self.__valor,self.__codigo,))
            
        if (a == '3'):
            self.__cantidad = int(input("Digite ela nueva cantidad de canciones del plan: "))
            self.cursor.execute("UPDATE PLANES SET CANTIDAD = ? WHERE CODIGO = ? ",(self.__cantidad,self.__codigo,))
        
        if (a == '4'):
            pass
        self.db.commit()
        os.system('cls')

    def ConsultarPlanes(self):# se cumplen dos opciones de consulta
        print('''
        1.) Consulta de todo el modulo.
        2.) Consulta especifica por uno de los campos.
        ''')#el primer tipo de consulta muestra todas las canciones guardadas dependiendo del orden que elija el usuario
        print("")#la segunda opcion permite buscar uno de los registros dependiendo de la opcion elegida
        m=int(input("Elija el tipo de consulta que desea realizar:"))
        if(m == 1):
            Lista.Mostrar(self,"PLANES")# la funcion mostrar imprime los atributos de la tabla para facilitar la comprension de los datos mostrados
        if(m == 2):
            print("")
            print('''
            1.) Codigo
            2.) Nombre
            3.) Valor
            4.) Cantidad 
            ''')
            print("")
            d = []
            a = int(input("Digite la opcion de busqueda: "))
            if(a == 1):
                self.__codigo = input("Digite el codigo del plan: ")
                self.cursor.execute("SELECT * FROM PLANES WHERE CODIGO = ?",(self.__codigo,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANES")

            if (a == 2):
                self.__nombre = input("Digite el nombre del plan: ")
                self.cursor.execute("SELECT * FROM PLANES WHERE NOMBRE = ?",(self.__nombre,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANES")

            if (a == 3):
                self.__valor = int(input("Digite el valor del plan: "))
                self.cursor.execute("SELECT * FROM PLANES WHERE VALOR = ?",(self.__valor,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANES")

            if (a == 4):
                self.__cantidad = int(input("Digite el cantidad del plan: "))
                self.cursor.execute("SELECT * FROM PLANES WHERE CANTIDAD = ?",(self.__cantidad,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANES")

            b = 6
            k = 0
            for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
                for j in d[i]:
                    if (k == b):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
        wait = input()
        os.system('cls')
    
#####################################################################

class Lista(Cliente,Cancion):
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
        self.__cedula=None
        self.__codigo=None
        pass
    def SetCedula(self):
        self.__cedula = input("Digite la cedula del cliente: ")
    def SetCodigo(self):
        self.__codigo = input("Digite el codigo del plan: ")

    def Mostrar(self,tabla): # esta funcion recibe una tabla y la muestra en el orden que seleccione
        print("")
        b = 0
        c = "0"
        if (tabla == "CANCIONES"):
            b = 5
            print("")
            print('''
            1.) codigo
            2.) nombre
            3.) genero
            4.) album
            5.) interprete
            ''')
            d = input("Digite el orden que deseaa: ")
            if (d == '1'):
                c = "CODIGO"
            if (d == '2'):
                c = "NOMBRE"
            if (d == '3'):
                c = "GENERO"
            if (d == '4'):
                c = "ALBUM"
            if (d == '5'):
                c = "INTERPRETE"
            FMenus.ImprimirTabla(tabla)
            self.cursor.execute("SELECT * FROM CANCIONES ORDER BY %s"%(c))
            
        elif (tabla == "CLIENTES"):
            b = 10
            print('''
            1.) cedula
            2.) nombre
            3.) apellido
            4.) pais
            5.) ciudad
            6.) # celular
            7.) fecha pago (ddmmaa)
            8.) Tarjeta credito
            9.) estado cuenta
            10.) id del plan
            ''')
            print("")
            d = input("Digite el orden que desea:")
            if (d == '1'):
                c = "CEDULA"
            if (d == '2'):
                c = "NOMBRE"
            if (d == '3'):
                c = "APELLIDO"
            if (d == '4'):
                c = "PAIS"
            if (d == '5'):
                c = "CIUDAD"
            if (d == '6'):
                c = "CELULAR"
            if (d == '7'):
                c = "FECHA"
            if (d == '8'):
                c = "NTARJETA"
            if (d == '9'):
                c = "ESTADO"
            if (d == '10'):
                c = "IDPLAN"
            FMenus.ImprimirTabla(tabla)
            self.cursor.execute("SELECT * FROM CLIENTES ORDER BY %s"%(c))
        elif (tabla == "PLANES"):
            b = 4
            print('''
            1.) Codigo
            2.) Nombre
            3.) Valor
            4.) Cantidad 
            ''')
            print("")
            d = input("Digite el orden que desea:")
            if (d == '1'):
                c = "CODIGO"
            if (d == '2'):
                c = "NOMBRE"
            if (d == '3'):
                c = "VALOR"
            if (d == '4'):
                c = "CANTIDAD"
            FMenus.ImprimirTabla(tabla)
            self.cursor.execute("SELECT * FROM PLANES ORDER BY %s"%(c))
        elif (tabla == "LISTA"):
            b = 2
            print('''
            1.) idcliente
            2.) idcancion
            ''')
            print("")
            d = input("Digite el orden que desea:")
            if (d == '1'):
                c = "IDCLIENTE"
            if (d == '2'):
                c = "IDCANCION"
            
            FMenus.ImprimirTabla(tabla)
            self.cursor.execute("SELECT * FROM LISTA ORDER BY %s"%(c))
        elif (tabla == "PLANESCLIENTE"):
            b = 2
            print('''
            1.) idcliente
            2.) idplan
            ''')
            print("")
            d = input("Digite el orden que desea:")
            if (d == '1'):
                c = "IDCEDULA"
            if (d == '2'):
                c = "IDPLAN"
            
            FMenus.ImprimirTabla(tabla)
            self.cursor.execute("SELECT * FROM PLANESCLIENTE ORDER BY %s"%(c))
            
        a = self.cursor.fetchall()
        k = 0
        for i in range(len(a)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            for j in a[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
            
        wait = input()
        os.system('cls')
    
    
    def AñadirCancionLista(self):#añade canciones a la tabla canciones cliente, con el id del cliente y el id de la cancion que son la llave compuesta
        while True:       
            self.cursor.execute("SELECT * FROM CLIENTES WHERE CEDULA = ?",(self.__cedula,))
            if (len(self.cursor.fetchall()) == 0):
                print("Cliente no encontrado")
                break
            else:
                while True:
            
                    self.cursor.execute("SELECT * FROM CANCIONES WHERE CODIGO = ?",(self.__codigo,))
                    if(len(self.cursor.fetchall())==0):
                        print("Cancion no encontrada")
                        break
                    else:
                        while True:
                            try: 
                                nueva_CanCliente = (self.__cedula,self.__codigo)
                                self.cursor.execute("INSERT INTO LISTA(IDCLIENTE, IDCANCION) VALUES(?,?)",nueva_CanCliente)
                                self.db.commit()
                                EnvioCorreo(self.cursor,self.db,self.__cedula)
                                break
                            except:
                                print("ha ocurrido un error, intentelo de nuevo.")
                                break
                        break
                break
        os.system('cls')
                
    def BorrarCancionesLista(self): #borra canciones de la lista luego de insertar el id de la cancion, luego de ingresar cliente
        while True:
            try:
                self.cursor.execute("DELETE FROM LISTA WHERE IDCLIENTE = ? AND IDCANCION = ?",(self.__cedula,self.__codigo))
                break #asi no borra todos los registros que tenga la cancion sino la que corresponde a ese cliente
            except:
                print("Codigo no existente1.")
                break
        self.db.commit()
        EnvioCorreo(self.cursor,self.db,self.__cedula)
        os.system('cls')

    def ConsultarLista(self):# se cumplen dos opciones de consulta
        print('''
        1.) Consulta de todo el modulo.
        2.) Consulta especifica por uno de los campos.
        ''')#el primer tipo de consulta muestra todas las canciones guardadas dependiendo del orden que elija el usuario
        print("")#la segunda opcion permite buscar uno de los registros dependiendo de la opcion elegida
        m=int(input("Elija el tipo de consulta que desea realizar:"))
        if(m == 1):
            Lista.Mostrar(self,"LISTA")
        if(m == 2):
            print("")
            print('''
            1.) idcliente
            2.) idcancion 
            ''')
            print("")
            d = []
            a = int(input("Digite la opcion de busqueda: "))
            if(a == 1):
                self.__cedula = input("Digite la id del cliente : ")
                self.cursor.execute("SELECT IDCLIENTE,IDCANCION,NOMBRE,INTERPRETE FROM LISTA JOIN CANCIONES ON LISTA.IDCANCION=CANCIONES.CODIGO WHERE IDCLIENTE = ?",(self.__cedula,))
                d = self.cursor.fetchall()#se requirio usar join para consultar ambas tablas y poder extraer tambien el nombre de la cancion y el interprete
                FMenus.ImprimirTabla("LISTA")

            if (a == 2):
                self.__codigo = input("Digite el id de la cancion: ")
                self.cursor.execute("SELECT IDCLIENTE,IDCANCION,NOMBRE,INTERPRETE FROM LISTA JOIN CANCIONES ON LISTA.IDCANCION=CANCIONES.CODIGO WHERE IDCANCION = ?",(self.__codigo,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("LISTA")

            b = 4
            k = 0
            for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
                for j in d[i]:
                    if (k == b):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
        wait = input()
        os.system('cls')

    def ReproducirCancion(self):
        mixer.init()
        d = []
        self.cursor.execute("SELECT IDCLIENTE,IDCANCION,NOMBRE,INTERPRETE FROM LISTA JOIN CANCIONES ON LISTA.IDCANCION=CANCIONES.CODIGO WHERE IDCLIENTE = ?",(self.__cedula,))
        d = self.cursor.fetchall()#se requirio usar join para consultar ambas tablas y poder extraer tambien el nombre de la cancion y el interprete
        FMenus.ImprimirTabla("LISTA")
        b = 4
        k = 0
        for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        rep=input("Digite el nombre de la cancion que desea escuchar: ")
        mixer.music.load(r'%s.mp3'%(rep))
        mixer.music.play()
        
    def EnvioCorreo(self,cliente):
        esp=" "
        separador="|"
        Flinea="\n"
        message=''
        self.cursor.execute("SELECT IDCLIENTE,IDCANCION,NOMBRE,INTERPRETE FROM LISTA JOIN CANCIONES ON LISTA.IDCANCION=CANCIONES.CODIGO WHERE IDCLIENTE = ?",(cliente,))
        d = self.cursor.fetchall()
        b = 4
        k = 0
        for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
            for j in d[i]:
                if (k == b):
                    k = 0
                    message = message+Flinea
                message=message+separador+esp
                message=message+j+esp
                message=message+separador+esp
                k=k+1
        
        subject = 'Tu Lista de Canciones'
        message = 'Subject: {}\n\n{}'.format(subject,message)

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('sqlitebasedatos@gmail.com', 'parcial2021')

        server.sendmail('sqlitebasedatos@gmail.com','paulavalentinabarrero@gmail.com', message)

        server.quit()

        print("Correo enviado con éxito")


class PlanesPorCliente(Cliente,Cancion):
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
        self.__cedula=None
        self.__plan=None
    def SetCedula(self):
        self.__cedula = input("Digite la cedula del cliente: ")
    def SetPlan(self):
        self.__plan = input("Digite el codigo del plan : ")
    def AsignarPlan(self):
        self.cursor.execute("SELECT * FROM PLANESCLIENTE WHERE IDCEDULA = ?",(self.__cedula,))
        Lista.Mostrar(self,"PLANES")
        self.__plan = input("Digite el codigo del plan: ")
        self.cursor.execute("UPDATE PLANESCLIENTE SET IDPLAN = ? WHERE IDCEDULA = ? ",(self.__plan,self.__cedula,))
        self.db.commit()
        os.system('cls')
                    
    def ConsultarPlan(self):
        print('''
        1.) Consulta de todo el modulo.
        2.) Consulta especifica por uno de los campos.
        ''')#el primer tipo de consulta muestra todas las canciones guardadas dependiendo del orden que elija el usuario
        print("")#la segunda opcion permite buscar uno de los registros dependiendo de la opcion elegida
        m=int(input("Elija el tipo de consulta que desea realizar:"))
        if(m == 1):
            Lista.Mostrar(self,"PLANESCLIENTE")# la funcion mostrar imprime los atributos de la tabla para facilitar la comprension de los datos mostrados
        if(m == 2):
            print("")
            print('''
            1.) Cedula
            2.) plan 
            ''')
            print("")
            d = []
            a = int(input("Digite la opcion de busqueda: "))
            if(a == 1):
                self.__cedula = input("Digite la cedula del cliente: ")
                self.cursor.execute("SELECT * FROM PLANESCLIENTE WHERE IDCEDULA = ?",(self.__cedula,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANESCLIENTE")

            if (a == 2):
                self.__plan = input("Digite el codigo del plan : ")
                self.cursor.execute("SELECT * FROM PLANESCLIENTE WHERE IDPLAN = ?",(self.__plan,))
                d = self.cursor.fetchall()
                FMenus.ImprimirTabla("PLANESCLIENTE")


            b = 4
            k = 0
            for i in range(len(d)): #esta operacion sirve para poner | entre los valores mostrados y separarlos para que sea visualmente mas entendible
                for j in d[i]:
                    if (k == b):
                        k = 0
                        print("")
                    print("|",end=" ")
                    print(j,end=" ")
                    print("|",end=" ")
                    k = k + 1
        wait = input()
        os.system('cls')




        
    
    
