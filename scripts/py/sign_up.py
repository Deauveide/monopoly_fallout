from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
import sqlite
from flask import json

# Inicializacion de variables
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/../sign_up', methods=['GET', 'POST'])

def sign_up():
    if request.method == 'POST':
        if request.form['boton'] == "Registrarse":
            usuario=request.form['usuario']
            correo=request.form['email']
            contraseña=request.form['password']
            print(usuario)
            
            return redirect(url_for('pagina_principal'))

if __name__ == '__main__':
    app.run(debug=True)
