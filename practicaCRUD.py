from tkinter import *
import sqlite3 #importamos el modulo "sqlite3" para manipular bd sqlite
from tkinter import messagebox #importamos "messagebox" para crear ventanas emergentes

raiz=Tk()#creamos la variable "raiz" y con la clase "Tk" creamos la ventana

raiz.title("Practica CRUD")#le damos un titulo a la ventana

#variables asociadas a los "entry o inputs" que almacenan los valores digitados en los input como cadena de texto
IDUser=StringVar()
NombreUser=StringVar()
ApellidoUser=StringVar()
ContrasenaUser=StringVar()
DireccionUser=StringVar()

#----------------------------FUNCIONES------------------------
def basededatos():
    miConexion=sqlite3.connect("practicaCRUD")
    #creamos variable "miConexion" para establecer conexion con una base de datos sqlite
    #si la base de datos no existe se creara una
    miCursor=miConexion.cursor()
    #creamos variable "miCursor" para crear un cursor y asi poder manipular la base de datos    
    try:
    #intentara ejecutar la siguiente instruccion    
        miCursor.execute('''
            CREATE TABLE Usuarios(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre_User VARCHAR(50),
            Apellido_User VARCHAR(50),
            Contrasena VARCHAR(50),
            Direccion VARCHAR(50),
            Comentarios VARCHAR(50))  
        ''')
        messagebox.showinfo("BBDD","Base de datos creada con exito")
    except:
        #si la tabla ya existe nos mostrara un cuadro de alerta
        messagebox.showwarning("BBDD","La Base de datos ya existe")
    
    miConexion.close()

def InsertarDatos():
    miConexion=sqlite3.connect("practicaCRUD")
    #creamos variable "miConexion" para establecer conexion con una base de datos sqlite
    #si la base de datos no existe se creara una
    miCursor=miConexion.cursor()
    #creamos variable "miCursor" para crear un cursor y asi poder manipular la base de dato
    DatosUsuarios=(NombreUser.get(),ApellidoUser.get(),ContrasenaUser.get(),DireccionUser.get(),ComentariosInput.get("1.0", END))
    #creamos una tupla llamada "DatosUsuarios" y en ella almacenamos las variables las cuales estan asociados a los input y text
    #y con "get" retornamos el valor digitado y que se almacene en dicha variable de los respectivos inputs y text
    #en el caso del elemento "text" el "1.0" indica que debe leerse desde la linea 1 y el caracter numero 0
    #y "END" indica que debe leerse hasta el final
    miCursor.execute("Insert Into Usuarios Values(NULL,?,?,?,?,?)",(DatosUsuarios))
    #el primer campo como es el "ID" por cual es llave primaria y autoincremental por lo cual lo pasamos como "NULL" 
    #al final llamamos la tupla "DatosUsuarios" la cual tiene los datos a insertar en la base de datos
         
    miConexion.commit()
    #con "commit" confirmamos que queremos realizar la accion en la tabla
    messagebox.showinfo("BBDD","Registro insertado")
    miConexion.close()

def ConsultaDatos():
    miConexion=sqlite3.connect("practicaCRUD")
    #creamos variable "miConexion" para establecer conexion con una base de datos sqlite
    #si la base de datos no existe se creara una
    miCursor=miConexion.cursor()
    #creamos variable "miCursor" para crear un cursor y asi poder manipular la base de datos    
    miCursor.execute("select * from Usuarios where ID="+IDUser.get())
    #consultamos los registros de la tabla especificando el id que se ha digitado en el input        
    DatosUser=miCursor.fetchall()
    #creamos variable "DatosUser" y con "fetchall" nos devuelve una lista con todos los registros de la tabla
    if not DatosUser:
    #con este condicional evaluamos si existe o no un "ID" al momento de consultarlo
    #entonces si no existe aparecera el siguiente mensaje
        messagebox.showwarning("BBDD","El ID digitado no existe")
    else:
        for Usuarios in DatosUser:
    #hacemos un bucle for para recorrer todas las columnas de la tabla,llamamos las variables asociadas a los inputs 
    #a dichas variables usamos "set" el cual cambiara e imprimira los datos del id especificado
            IDUser.set(Usuarios[0])
            NombreUser.set(Usuarios[1])
            ApellidoUser.set(Usuarios[2])
            ContrasenaUser.set(Usuarios[3])
            DireccionUser.set(Usuarios[4])
            ComentariosInput.insert(1.0, Usuarios[5])
            #el elemento "text" con "insert" se imprimira el dato almacenado en la columna "Comentarios"
            #con "1.0" indicamos que lea desde la linea 1 y el caracter numero 0

    miConexion.commit()
    #con "commit" confirmamos que queremos realizar la accion en la tabla
    miConexion.close()

def ActualizarDatos():
    miConexion=sqlite3.connect("practicaCRUD")
    #creamos variable "miConexion" para establecer conexion con una base de datos sqlite
    #si la base de datos no existe se creara una
    miCursor=miConexion.cursor()
    #creamos variable "miCursor" para crear un cursor y asi poder manipular la base de dato
    DatosUsuarios=(NombreUser.get(),ApellidoUser.get(),ContrasenaUser.get(),DireccionUser.get(),ComentariosInput.get("1.0", END))
    #creamos una tupla llamada "DatosUsuarios" y en ella almacenamos las variables las cuales estan asociados a los input y text
    #y con "get" retornamos el valor digitado y que se almacene en dicha variable de los respectivos inputs y text
    miCursor.execute("update Usuarios set Nombre_User=?,Apellido_User=?,Contrasena=?,Direccion=?,Comentarios=? where ID="+IDUser.get(),
    (DatosUsuarios))    
    #llamamos la variable del cursor y con "execute" y la sentencia sql "update" actualizamos los datos 
    #especificando el id que se ha digitado en el input
    #al final llamamos la tupla "DatosUsuarios" la cual tiene los datos que actualizaremos de la base de datos
    miConexion.commit()
    #con "commit" confirmamos que queremos realizar la accion en la tabla
    messagebox.showinfo("BBDD","Registro Actualizado")
    miConexion.close()
    
def EliminarDatos():
    miConexion=sqlite3.connect("practicaCRUD")
    #creamos variable "miConexion" para establecer conexion con una base de datos sqlite
    #si la base de datos no existe se creara una
    miCursor=miConexion.cursor()
    #creamos variable "miCursor" para crear un cursor y asi poder manipular la base de dato
    miCursor.execute("select * from Usuarios where ID="+IDUser.get())
    #consultamos los registros de la tabla especificando el id que se ha digitado en el input        
    DatosUser=miCursor.fetchall()
    #creamos variable "DatosUser" y con "fetchall" nos devuelve una lista con todos los registros de la tabla
    if not DatosUser:
    #con este condicional evaluamos si existe o no un "ID" al momento de consultarlo
    #entonces si no existe aparecera el siguiente mensaje
        messagebox.showwarning("BBDD","El ID digitado no existe")
    else:
    #si el id digitado si existe procede a eliminar los datos del id
        miCursor.execute("delete from Usuarios where ID="+IDUser.get())
    #llamamos la variable del cursor y con "execute" y la sentencia sql "delete" eliminamos especificando el id que se ha digitado en el input
        messagebox.showinfo("BBDD","Registro eliminado")
                    
    miConexion.commit()   
    #con "commit" confirmamos que queremos realizar la accion en la tabla    
    miConexion.close()

def VentanaSalir():
#funcion para mostrar la ventana emergente
    valor=messagebox.askquestion("Salir","¿Deseas salir del programa?")
    #con "messagebox.askquestion" nos creara una ventana emergente con dos opciones "si" y "no"
    #la variable "valor" almacenara el valor al oprimir el boton
    if valor=="yes":
    #condicional que si "valor" es "yes" es decir si pulsó el boton "si" en la ventana se cerrara el programa
        raiz.destroy()
        #cerramos la ventana
 
#con "LimpiarCampos" usamos "set" para pasarle un nuevo valor a las variables asociadas al input borrando lo digitado en ellos
def LimpiarCampos():
    IDUser.set("")
    NombreUser.set("")
    ApellidoUser.set("")
    ContrasenaUser.set("")
    DireccionUser.set("")
    ComentariosInput.delete(1.0, END)
    #con el elemento "text" y con "delete" eliminamos todo lo digitado en el textarea
    #indicandole "1.0" que debe eliminar desde la linea 1 y el caracter numero 0
    #y "END" indica que debe eliminar hasta el final

#------------------------------------MENU----------------------------------------------------
barraMenu=Menu(raiz)

raiz.config(menu=barraMenu, width=300, height=500)

MenuArchivo=Menu(barraMenu, tearoff=0)#con "tearoff" quitamos una linea que aparece al desplegar las opcion de un boton
MenuArchivo.add_command(label="Conectar", command=basededatos)
#llamamos la variable del menu "barraMenu" y con "add_command" agregamos opciones para desplegar el boton "Archivo"
#"command" nos sirve para llamar una funcion y asi darle funcionalidad al boton

MenuCrud=Menu(barraMenu, tearoff=0)
MenuCrud.add_command(label="Crear")
#llamamos la variable del menu "barraMenu" y con "add_command" agregamos opciones para desplegar el boton "Ayuda"
#llamamos con "command" la funcion "VentanaInfo" para que al pulsar "Acerca de" se muestre la ventana
MenuCrud.add_command(label="Consultar")
MenuCrud.add_command(label="Actualizar")
MenuCrud.add_command(label="Eliminar")

MenuAyuda=Menu(barraMenu, tearoff=0)
MenuAyuda.add_command(label="Acerca de")
#llamamos la variable del menu "barraMenu" y con "add_command" agregamos opciones para desplegar el boton "Ayuda"
#llamamos con "command" la funcion "VentanaInfo" para que al pulsar "Acerca de" se muestre la ventana
MenuAyuda.add_command(label="Licencia")
#llamamos con "command" la funcion "VentanaLic" para que al pulsar "Licencia" se muestre la ventana

barraMenu.add_cascade(label="Base de datos", menu=MenuArchivo)
#llamamos la variable del menu "barraMenu" y con "add_cascade" creamos el boton del menu, llamamos la variable del boton "MenuArchivo"
barraMenu.add_cascade(label="Borrar",command=LimpiarCampos)
barraMenu.add_cascade(label="CRUD",menu=MenuCrud)
barraMenu.add_cascade(label="Ayuda",menu=MenuAyuda)
barraMenu.add_cascade(label="Salir", command=VentanaSalir)

#----------------------------ETIQUETAS E INPUTS---------------------------------------------
idlabel=Label(raiz, text="Id:")
idlabel.grid(row=0, column=0, padx=10, pady=10)

#asocio la variable "IDUser" con el input o entry
idInput=Entry(raiz,textvariable=IDUser)
idInput.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

Nombrelabel=Label(raiz, text="Nombre:")
Nombrelabel.grid(row=1, column=0, padx=10, pady=10)

#asocio la variable "NombreUser" con el input o entry
NombreInput=Entry(raiz,textvariable=NombreUser)
NombreInput.grid(row=1, column=1, padx=10, pady=10,columnspan=4)

Apellidolabel=Label(raiz, text="Apellidos:")
Apellidolabel.grid(row=2, column=0, padx=10, pady=10)

#asocio la variable "ApellidoUser" con el input o entry
ApellidoInput=Entry(raiz,textvariable=ApellidoUser)
ApellidoInput.grid(row=2, column=1, padx=10, pady=10,columnspan=4)

Contrasenalabel=Label(raiz, text="Contraseña:")
Contrasenalabel.grid(row=3, column=0, padx=10, pady=10)

#asocio la variable "ContrasenaUser" con el input o entry
ContrasenaInput=Entry(raiz,textvariable=ContrasenaUser)
ContrasenaInput.grid(row=3, column=1, padx=10, pady=10,columnspan=4)
ContrasenaInput.config(show="*")
#al campo de contraseña lo configuramos con el metodo "config" con la propiedad "show" para que al escribir aparezcan *

Direccionlabel=Label(raiz, text="Direccion:")
Direccionlabel.grid(row=4, column=0, padx=10, pady=10)

#asocio la variable "DireccionUser" con el input o entry
DireccionInput=Entry(raiz,textvariable=DireccionUser)
DireccionInput.grid(row=4, column=1, padx=10, pady=10,columnspan=4)

Comentarioslabel=Label(raiz, text="Comentarios:")
Comentarioslabel.grid(row=5, column=0, padx=10, pady=10)

ComentariosInput=Text(raiz,width=16, height=10)
ComentariosInput.grid(row=5, column=1, padx=10, pady=10,columnspan=4)

#--------------------------------BOTONES--------------------------------------------------
Crear=Button(raiz,width=8, text="Crear", command=InsertarDatos)
Crear.grid(row=6, column=0,padx=10, pady=10)

Consultar=Button(raiz,width=8, text="Consultar",command=ConsultaDatos)
Consultar.grid(row=6, column=1,padx=10, pady=10)

Actualizar=Button(raiz,width=8, text="Actualizar",command=ActualizarDatos)
Actualizar.grid(row=6, column=2,padx=10, pady=10)

eliminar=Button(raiz,width=8, text="Eliminar",command=EliminarDatos)
eliminar.grid(row=6, column=3,padx=10, pady=10)

raiz.mainloop()