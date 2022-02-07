import sqlite3
import smtplib, ssl #libreria para el envio de correo electronico y ssl para conexion segura
import FuncionesSQL as funciones
import FuncionesMenu as FMenus
import os

database = sqlite3.connect("labasededatospooparcial.db")

lector = database.cursor()
# Creacion de las tablas necesarias
try:
    
    lector.execute("CREATE TABLE CANCIONES (CODIGO CHAR(6) PRIMARY KEY,NOMBRE VARCHAR(30) not null,GENERO VARCHAR(20)not null,ALBUM VARCHAR(30)not null, INTERPRETE VARCHAR(25)not null)ON DELETE CASCADE ON UPDATE CASCADE)")
except:
    pass

try:
    
    lector.execute("CREATE TABLE CLIENTES (CEDULA CHAR(10) PRIMARY KEY,NOMBRE VARCHAR(25)not null,APELLIDO VARCHAR(25)not null, PAIS VARCHAR(20), CIUDAD VARCHAR(20),CELULAR CHAR(10),FECHA INTEGER(7),NTARJETA CHAR(10)not null,ESTADO VARCHAR (8)not null)")
    
                 
except:
    pass

try:
    
    lector.execute("CREATE TABLE PLANES (CODIGO CHAR(4) PRIMARY KEY, NOMBRE VARCHAR(30)not null, VALOR INTEGER(6)not null, CANTIDAD INTEGER(6)not null)ON DELETE CASCADE ON UPDATE CASCADE)")
except:
    pass


try:
    #la tabla lista es una tabla que posee dos llaves foraneas como llave primaria compuesta.
    lector.execute("CREATE TABLE LISTA (IDCLIENTE CHAR(10), IDCANCION CHAR(6),CONSTRAINT ID PRIMARY KEY (IDCLIENTE,IDCANCION),CONSTRAINT FK_CLIENTE FOREIGN KEY (IDCLIENTE)REFERENCES CLIENTES(CEDULA),CONSTRAINT FK_CANCION FOREIGN KEY (IDCANCION)REFERENCES CANCIONES(CODIGO))")
except:
    pass
try:
    lector.execute("CREATE TABLE PLANESCLIENTE (IDCEDULA CHAR(10) PRIMARY KEY,IDPLAN CHAR(4),CONSTRAINT FK_CLIENTE FOREIGN KEY (IDCEDULA)REFERENCES CLIENTES(CEDULA),CONSTRAINT FK_PLAN FOREIGN KEY (IDPLAN)REFERENCES PLANES(CODIGO))")
except:
    pass

condition = True
os.system('cls')
while condition ==  True:

    opcion =FMenus.Menu() #llama a la primera funcion de menu que usaremos 

    if (opcion == 1):
        objCancion = funciones.Cancion(database)
        opcion1 = FMenus.MenuOpcionesCanciones() #el menu opciones tiene las mismas 4 opciones para cada una de las tablas (añadir,borrar,modificar,consultar)

        if (opcion1 == 1):
            #objCancion.AñadirCanciones(objCancion.IngresarDatosCancion())
            objCancion.SetCodigo()
            objCancion.SetNombre()
            objCancion.SetGenero()
            objCancion.SetAlbum()
            objCancion.SetInterprete()
            objCancion.AñadirCanciones(objCancion.TuplaCancion())
        elif (opcion1 == 2):
            objCancion.SetCodigo()
            objCancion.ModificarCanciones()
        elif (opcion1 == 3):
                objCancion.ConsultarCanciones()
        elif (opcion1 == 4):
                pass
        else:
                print("Opcion no valida.1")

    if (opcion == 2):
        objCliente = funciones.Cliente(database)
        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                #objCliente.AñadirClientes(objCliente.IngresarDatosCliente())
            objCliente.SetCedula()
            objCliente.SetNombre()
            objCliente.SetApellido()
            objCliente.SetPais()
            objCliente.SetCiudad()
            objCliente.SetCelular()
            objCliente.SetFecha()
            objCliente.SetTarjeta()
            objCliente.SetEstado()
            objCliente.SetPlan()
            objCliente.AñadirClientes(objCliente.TuplaCliente())
        elif (opcion1 == 2):
            objCliente.SetCedula()
            objCliente.BorrarClientes()
        elif (opcion1 == 3):
            objCliente.SetCedula()
            objCliente.ModificarClientes()
        elif (opcion1 == 4):
            objCliente.ConsultarClientes()
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.2")

    if (opcion == 3):
        objPlan = funciones.Plan(database)
        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
            objPlan.SetCodigo()
            objPlan.SetNombre()
            objPlan.SetValor()
            objPlan.SetCantidad()
            objPlan.AñadirPlanes(objPlan.TuplaPlan())
        elif (opcion1 == 2):
            objPlan.SetCodigo()
            objPlan.BorrarPlanes()
        elif (opcion1 == 3):
            objPlan.SetCodigo()
            objPlan.ModificarPlanes()
        elif (opcion1 == 4):
            objPlan.ConsultarPlanes()
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.3")

    if (opcion == 4):
        objLista = funciones.Lista(database)
        opcion1 = FMenus.MenuLista() #la lista tiene un menu diferente sin la opcion modificar puesto que solo admite añadir,borrar y consultar.

        if (opcion1 == 1):
            objLista.SetCedula()
            objLista.SetCodigo()
            objLista.AñadirCancionLista()
        elif (opcion1 == 2):
            objLista.SetCedula()
            objLista.SetCodigo()
            objLista.BorrarCancionesLista()
        elif (opcion1 == 3):
            objLista.ConsultarLista()
        elif (opcion1 == 4):
            objLista.SetCedula()
            objLista.ReproducirCancion()
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.4")

    elif (opcion == 5):
        objPlanCliente = funciones.PlanesPorCliente(database)
        opcion1 = FMenus.MenuPlanesCliente() #la lista tiene un menu diferente sin la opcion modificar puesto que solo admite añadir,borrar y consultar.
        if (opcion1 == 1):
            objPlanCliente.SetCedula()
            objPlanCliente.AsignarPlan()
        elif (opcion1 == 2):
            objPlanCliente.ConsultarPlan()
        elif (opcion1 == 3):
                pass
    elif (opcion == 6):
        objTablaGrafica = funciones.mywindow(database)
        objTablaGrafica.loaddata()
        pass
    elif (opcion == 7):
        condition =(FMenus.Salir)

    else:
        print("")
        
database.commit()
database.close()
