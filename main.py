from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sqlite
from flask import json

# Inicializacion de variables
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def hello():
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
