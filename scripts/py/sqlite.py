import sqlite3

con_usr = sqlite3.connect("../../db/usuarios.db")

cursor = con_usr.cursor()

def crearTabla():
    """
    Descripcion: Funcion que se encarga de crear la tabla sql.
    Salida: Tabla en el archivo db creado anteriormente.
    """
    cursor.execute(
        "CREATE TABLE users(\
        username VARCHAR(30) UNIQUE PRIMARY KEY,\
        password VARCHAR(30),\
        email VARCHAR(40) UNIQUE);"
        )


def añadirUsuario(usrName, pswd, email):
    """
    Descripcion: Funcion encargada de añadir el usuario a la tabla.
    Entrada: Nombre de usuario, contraseña, email.
    Salida: Cambios en la tabla.
    """
    reg = (usrName, pswd, email)
    cursor.execute("INSERT INTO users VALUES(?,?,?)", reg)
    con_usr.commit()


def eliminarUsuario(usrName):
    """
    Descripcion: Funcion que elimina un usuario de la tabla.
    Entrada: Nombre del usuario a eliminar.
    Salida: Cambios en la tabla.
    """
    val=(usrName,)
    cursor.execute('DELETE FROM users WHERE username=?', val)
    con_usr.commit()


def cambiarPass(usrName, pswd, newPswd):
    """
    Descripcion: Funcion que permite cambiar la contraseña.
    Entradas: Nombre de usuario, contraseña, nueva contraseña.
    Salida: Cambios en la tabla.
    """
    par=(usrName)
    cursor.execute("SELECT password FROM users WHERE username=?", par)
    registro = cursor.fetchone()
    if(pswd==registro[0]):
        values = (newPswd, par, )
        cursor.execute("UPDATE users SET password=? WHERE username=?", values)
        con_usr.commit()
        

def verDB():
    """
    Descripcion: Funcion para ver el contenido de la tabla
    Salida: Tabla por consola
    """    
    cursor.execute("SELECT * FROM users")
    for registro in cursor:
        print(registro)
