from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sqlite
import random

# Inicializacion de variables
app = Flask(__name__)
global inicioSesion, tablero, turno
inicioSesion=False

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



@app.route('/', methods=['GET', 'POST'])
def index():
    global inicioSesion
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
                    return redirect(url_for('monopoly'))
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
    global inicioSesion, tablero, turno
    entries = {"tablero": tablero}
    dados=0
    if inicioSesion:
        turno=1
        if(request.method == "POST"):
                if(request.form["boton"]=="Mover"):
                    dado1=random.randint(1,6)
                    dado2=random.randint(1,6)
                    moverFicha("A", dado1+dado2)
                    entries["tablero"]=tablero
                    entries["dados"]=[]
                    return render_template('monopoly.html', entries=entries)
        else:
            return render_template('monopoly.html', entries=entries)
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
                tablero[posx][posy]=""
                tablero[posx+mov][0]=jug




    
if __name__ == '__main__':
    app.run(port=8080)
