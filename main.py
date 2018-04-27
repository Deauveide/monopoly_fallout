from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sqlite
from flask import json

# Inicializacion de variables
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['boton'] == "Contraseña":
            return redirect(url_for('forget'))
        elif request.form['boton'] == "Registrarse":
            return redirect(url_for('sign_up'))
    else:
        return render_template('index.html')
    
@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == 'POST':
        if request.form['boton'] == "Iniciar sesión":
            return redirect(url_for('index'))
        elif request.form['boton'] == "Registrarse":
            return redirect(url_for('sign_up'))
    else:
        return render_template('forget.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        if request.form['boton'] == "Iniciar sesión":
            return redirect(url_for('index'))
        elif request.form['boton'] == "Contraseña":
            return redirect(url_for('forget'))
    else:
        return render_template('sign_up.html')
    """
    if request.method == 'POST':
        if request.form['boton'] == "Registrarse":
            usuario=request.form['usuario']
            correo=request.form['email']
            contraseña=request.form['password']
            print(usuario)
            return redirect(url_for('pagina_principal'))
    """
    
if __name__ == '__main__':
    app.run(port=8080)
