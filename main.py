from flask import Flask, request, redirect, url_for, render_template, session
import flask
import sqlite
import random

# Inicializacion de variables
app = Flask(__name__)
app.secret_key = ".unamuymuysecretasecreta."
global inicioSesion, tablero, turno
inicioSesion=False
turno=1

tablero = [["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","",""],
           ["","","","","","","","","","","C"]]


global jugador, jugador2, infoCasillas

infoCasillas={
    0:{
    "pos": [10,10],
    "nombre": "Go",
    "valor": 200,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },

    1:{
    "pos": [10,9],
    "nombre": "Camp Searchlight",
    "valor" : -60,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    2:{
    "pos": [10,8],
    "nombre": "Lockpick",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    3:{
    "pos": [10,7],
    "nombre": "Vault 22",
    "valor": -60,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    4:{
    "pos": [10,6],
    "nombre": "NCR Tax",
    "valor": -200,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    5:{
    "pos": [10,5],
    "nombre": "South Monorail",
    "valor": -200,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    6:{
    "pos": [10,4],
    "nombre": "Nipton",
    "valor": -100,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    7:{
    "pos": [10,3],
    "nombre": "Luck",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    8:{
    "pos": [10,2],
    "nombre": "Boulder city",
    "valor": -100,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    9:{
    "pos": [10,1],
    "nombre": "Sloan",
    "valor": -120,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    10:{
    "pos": [10,0],
    "nombre": "Visit jail",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    11:{
    "pos": [9,0],
    "nombre": "Goodsprings",
    "valor": -140,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    12:{
    "pos": [8,0],
    "nombre": "Primm",
    "valor": -140,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    13:{
    "pos": [7,0],
    "nombre": "Poseidon",
    "valor": -150,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    14:{
    "pos": [6,0],
    "nombre": "Freeside",
    "valor": -160,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    15:{
    "pos": [5,0],
    "nombre": "West Monorail",
    "valor": -200,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    16:{
    "pos": [4,0],
    "nombre": "Novac",
    "valor": -180,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    17:{
    "pos": [3,0],
    "nombre": "Trading post",
    "valor": -180,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    18:{
    "pos": [2,0],
    "nombre": "Lockpick",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    19:{
    "pos": [1,0],
    "nombre": "Sarsaparrilla",
    "valor": -200,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    20:{
    "pos": [0,0],
    "nombre": "Sleep",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    21:{
    "pos": [0,1],
    "nombre": "Mojave outpost",
    "valor": -220,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    22:{
    "pos": [0,2],
    "nombre": "Luck",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    23:{
    "pos": [0,3],
    "nombre": "Heilds one",
    "valor": -220,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    24:{
    "pos": [0,4],
    "nombre": "Repconn",
    "valor": -240,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    25:{
    "pos": [0,5],
    "nombre": "North Monorail",
    "valor": -200,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    26:{
    "pos": [0,6],
    "nombre": "Hidden valley",
    "valor": -260,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    27:{
    "pos": [0,7],
    "nombre": "Jacob's town",
    "valor": -260,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    28:{
    "pos": [0,8],
    "nombre": "Lake mead",
    "valor": -150,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    29:{
    "pos": [0,9],
    "nombre": "Gun runners",
    "valor": -280,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    30:{
    "pos": [0,10],
    "nombre": "Jail",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    31:{
    "pos": [1,10],
    "nombre": "Nellis",
    "valor": -300,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    32:{
    "pos": [2,10],
    "nombre": "The fort",
    "valor": -300,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    33:{
    "pos": [3,10],
    "nombre": "Lockpick",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    34:{
    "pos": [4,10],
    "nombre": "Camp Mccarran",
    "valor": -320,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    35:{
    "pos": [5,10],
    "nombre": "East Monorail",
    "valor": -200,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    36:{
    "pos": [6,10],
    "nombre": "Luck",
    "valor": 0,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    37:{
    "pos": [7,10],
    "nombre": "Hoover dam",
    "valor": -350,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    },
    38:{
    "pos": [8,10],
    "nombre": "Credit check",
    "valor": -75,
    "propiedad": False,
    "cantCasas": 0,
    "dueño": ""
    },
    39:{
    "pos": [9,10],
    "nombre": "The strip",
    "valor": -400,
    "propiedad": True,
    "cantCasas": 0,
    "dueño": ""
    }
}

jugador={
    "usrname": "",
    "dinero": 2000,
    "nJugador": ""
}
jugador2={
    "usrname": "",
    "dinero": 2000,
    "nJugador": ""
}

@app.route('/', methods=['GET', 'POST'])
def index():
    global inicioSesion, jugador, jugador2
    session["jug"]=""
    error = None
    if request.method == 'POST':
        if request.form['boton'] == "Contraseña":
            return redirect(url_for('forget'))
        elif request.form['boton'] == "Registro":
            return redirect(url_for('sign_up'))
        elif request.form['boton'] == "Entrar":
            usr = request.form['usuario']
            pswd = request.form['password']
            if(sqlite.validarUsuario(usr)):
                if sqlite.verificarContraseña(usr, pswd):
                    inicioSesion=True
                    if(jugador["usrname"] == ""):
                        jugador["usrname"]=usr
                        jugador["nJugador"]="A"
                        session["jug"]="A"
                    elif(jugador2["usrname"] == ""):
                        jugador2["usrname"]=usr
                        jugador2["nJugador"]="B"
                        session["jug"]="B"
                    else:
                        error="sala_llena"
                        return render_template('index.html', error=error)
                    return redirect(url_for('monopoly'), session["jug"])
                else:
                    error = "pswdIncorrecta"
                    return render_template('index.html', error=error)
            else:
                error = "usuario!exist"
                return render_template('index.html', error=error)
            
    else:
        return render_template('index.html')
    
@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == 'POST':
        if request.form['boton'] == "Iniciar sesión":
            return redirect(url_for('index'))
        elif request.form['boton'] == "Registro":
            return redirect(url_for('sign_up'))
    else:
        return render_template('forget.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        if request.form['boton'] == "Iniciar sesión":
            return redirect(url_for('index'))
        elif request.form['boton'] == "Contraseña":
            return redirect(url_for('forget'))
        elif request.form['boton'] == "Registrarse":
            usr = request.form['usuario']
            pswd = request.form['password']
            email = request.form['email']
            if sqlite.validarUsuario(usr):
                error = "usuarioExist"
                return render_template('sign_up.html', error=error)
            sqlite.añadirUsuario(usr, pswd, email)
            error = "usuarioCreado"
            return redirect(url_for('index'))
    else:
        return render_template('sign_up.html')

@app.route('/monopoly', methods=['GET', 'POST'])
def monopoly():
    global inicioSesion, tablero, jugador, turno, jugador2, infoCasillas
    entries = {"tablero": tablero, "dados" : [0,0], "turno": turno}
    dados=0
    dado1=0
    dado2=0
    if inicioSesion:

        if(request.method == "POST"):
                if(request.form["boton"]=="Mover J1"):
                    if(turno==1):
                        turno=2
                        dado1=random.randint(1,5)
                        dado2=random.randint(1,5)
                        moverFicha("A", dado1+dado2)
                        entries["tablero"]=tablero
                        entries["dados"]=[dado1, dado2]
                        cont=0
                        cont2=0
                        for i in tablero:
                            cont2=0
                            for j in i:
                                if(tablero[cont][cont2]=="A" or tablero[cont][cont2]=="C"):
                                    break
                                cont2+=1
                            cont+=1
                        n=0
                        for i in infoCasillas:
                            if(infoCasillas[i]["pos"]==[cont, cont2]):
                                n=i
                        n=n+dado1+dado2
                        if(infoCasillas[n]["dueño"]=="" and infoCasillas[n]["propiedad"]):
                            infoCasillas[n]["dueño"]="A"
                            jugador["dinero"]=jugador["dinero"]+infoCasillas[n]["valor"]
                            print(infoCasillas[n]["dueño"])
                        elif(infoCasillas[n]["dueño"]=="B"):
                            jugador["dinero"]=jugador["dinero"]-infoCasillas[n]["valor"]

                    else:
                        entries["tablero"]=tablero
                        entries["dados"]=[dado1, dado2]
                        entries["turno"]=turno
                elif(request.form["boton"]=="Mover J2"):
                    if(turno==2):
                        turno=1
                        dado1=random.randint(1,5)
                        dado2=random.randint(1,5)
                        moverFicha("B", dado1+dado2)
                        entries["tablero"]=tablero
                        entries["dados"]=[dado1, dado2]

                        cont=0
                        cont2=0
                        for i in tablero:
                            cont2=0
                            for j in i:
                                if(tablero[cont][cont2]=="B" or tablero[cont][cont2]=="C"):
                                    break
                                cont2+=1
                            cont+=1
                        n=0
                        for i in infoCasillas:
                            if(infoCasillas[i]["pos"]==[cont, cont2]):
                                n=i
                        n=n+dado1+dado2
                        if(infoCasillas[n]["dueño"]=="" and infoCasillas[n]["propiedad"]):
                            infoCasillas[n]["dueño"]="B"
                            jugador["dinero"]=jugador["dinero"]+infoCasillas[n]["valor"]
                            print(infoCasillas[n]["dueño"])
                        elif(infoCasillas[n]["dueño"]=="A"):
                            jugador["dinero"]=jugador["dinero"]-infoCasillas[n]["valor"]
                    else:
                        entries["tablero"]=tablero
                        entries["dados"]=[dado1, dado2]
                        entries["turno"]=turno


                return render_template('monopoly.html', entries=entries, jugador=jugador, jugador2=jugador2)
        else:
            return render_template('monopoly.html', entries=entries, jugador=jugador, jugador2=jugador2)
    else:
        return redirect(url_for('index'))


def moverFicha(jug, cant):
    """
    Descripcion: Funcion que mueve las ficha recibida la cantidad de espacios que se pide
    Entrada: Jugador a mover y cantidad de espacios
    Salida: Tabla con el jugador movido
    """
    global tablero
    cont=0
    cont2=0
    posx=0
    posy=0
    for i in tablero:
        cont2=0
        for j in i:
            if(tablero[cont][cont2]==jug or tablero[cont][cont2]=="C"):
                posx=cont
                posy=cont2
            cont2+=1
        cont+=1
    if(posx==10):
        if(posy-cant>=0):
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[posx][posy-cant]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[posx][posy-cant]=jug
            else:
                if(tablero[posx][posy-cant]=="A" or tablero[posx][posy-cant]=="B"):
                    tablero[posx][posy]=""
                    tablero[posx][posy-cant]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[posx][posy-cant]=jug
        else:
            mov=(posy-cant)
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[posx+mov][0]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[posx+mov][0]=jug
            else:
                if(tablero[posx+mov][0]=="A" or tablero[posx+mov][0]=="B"):
                    tablero[posx][posy]=""
                    tablero[posx+mov][0]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[posx+mov][0]=jug

    elif(posy==0):
        if(posx-cant>=0):
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[posx-cant][0]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[posx-cant][0]=jug
            else:
                if(tablero[posx][posy-cant]=="A" or tablero[posx][posy-cant]=="B"):
                    tablero[posx][posy]=""
                    tablero[posx-cant][0]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[posx-cant][0]=jug
        else:
            mov=abs(posx-cant)
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[0][mov]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[0][mov]=jug
            else:
                if(tablero[0][mov]=="A" or tablero[0][mov]=="B"):
                    tablero[posx][posy]=""
                    tablero[0][mov]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[0][mov]=jug
    elif(posx==0):
        if(posy+cant<=10):
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[posx][posy+cant]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[posx][posy+cant]=jug
            else:
                if(tablero[posx][posy-cant]=="A" or tablero[posx][posy-cant]=="B"):
                    tablero[posx][posy]=""
                    tablero[posx][posy+cant]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[posx][posy+cant]=jug
        else:
            mov=posy+cant-10
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[mov][10]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[mov][10]=jug
            else:
                if(tablero[mov][10]=="A" or tablero[mov][10]=="B"):
                    tablero[posx][posy]=""
                    tablero[mov][10]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[mov][10]=jug
    elif(posy==10):
        if(posx+cant<=10):
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[posx+cant][posy]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[posx+cant][posy]=jug
            else:
                if(tablero[posx+cant][posy]=="A" or tablero[posx+cant][posy]=="B"):
                    tablero[posx][posy]=""
                    tablero[posx+cant][posy]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[posx+cant][posy]=jug
        else:
            mov=posx+cant-10
            if(tablero[posx][posy]=="C"):
                if(jug=="A"):
                    tablero[posx][posy]="B"
                    tablero[10][10-mov]=jug
                elif(jug=="B"):
                    tablero[posx][posy]="A"
                    tablero[10][10-mov]=jug
            else:
                if(tablero[10][10-mov]=="A" or tablero[10][10-mov]=="B"):
                    tablero[posx][posy]=""
                    tablero[10][10-mov]="C"
                else:
                    tablero[posx][posy]=""
                    tablero[10][10-mov]=jug





    
if __name__ == '__main__':
    app.run(port=8080)
