from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sqlite
from flask import json

# Inicializacion de variables
app = Flask(__name__)
global inicioSesion, tablero
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
    global inicioSesion, tablero
    entries = {"tablero": tablero}
    if inicioSesion:
        return render_template('monopoly.html', entries=entries)
    else:

        return redirect(url_for('index'))

    
if __name__ == '__main__':
    app.run(port=8080)
