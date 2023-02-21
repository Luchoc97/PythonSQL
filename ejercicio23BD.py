import sqlite3 #importamos el modulo "sqlite3" para manipular bd sqlite

miConexion=sqlite3.connect("BaseDatos2")
#creamos variable "miConexion" para establecer conexion con una base de datos sqlite
#si la base de datos no existe se creara una

miCursor=miConexion.cursor()
#creamos variable "miCursor" para crear un cursor y asi poder manipular la base de datos

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))  
''')
#llamamos la variable del cursor y con "execute" crearemos la tabla PRODUCTOS y sus 4 campos, su tipo de dato y longitud del campo
#al campo "ID" lo creamos con llave primaria con el cual especificamos que el campo "ID" debe ser unico en la tabla
#al campo "ID" lo colocamos como campo autoincrementable para que cada registro tenga un identificador en la tabla
#al campo "NOMBRE_ARTICULO" le indicamos con "UNIQUE" que el dato o registro del campo no puede repetirse


DatosProductos=[
    ("pelota", 20, "jugeteria"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
    ("florero", 65, "cerámica"),
    #("pantalón", 45, "confección")#esta linea dara error ya que el campo "NOMBRE_ARTICULO" no puede repetirse por ser "UNIQUE"
]
#creamos lista "DatosProductos" la cual tendra dentro una tupla con los 3 campos de la tabla PRODUCTOS

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", DatosProductos)
#llamamos la variable del cursor y con "executemany" que nos permite insertar varios registros
#despues de values colocamos un "?" por cada campo que existe en la tabla, luego llamamos la lista que tiene los datos para insertar
#colocamos "NULL" el cual se refiere al campo "ID" ya que dicho campo es llave primaria y autoincrementable

miConexion.commit()
#con "commit" confirmamos que queremos realizar la accion en la tabla

miConexion.close()
#cerramos la conexion con la base de dato