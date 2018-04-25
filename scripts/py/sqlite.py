import sqlite3

con_usr = sqlite3.connect("../../db/usuarios.db")

cursor = con_usr.cursor()

cursor.execute(
    "CREATE TABLE users(\
    username VARCHAR(30) UNIQUE,\
    password VARCHAR(30),\
    email VARCHAR(40) UNIQUE);"
    )

def añadirUsuario(usrName, pswd, email):
    reg = (usrName, pswd, email)
    cursor.execute("INSERT INTO users VALUES(?,?,?)", reg)
    con_usr.commit()



def verDB():
    cursor.execute("SELECT * FROM users")
    for registro in cursor:
        print(registro)
