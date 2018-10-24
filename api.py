import flask
import json
from flask import request, jsonify, redirect
import mysql.connector

# Creación de una nueva aplicación web
app = flask.Flask(__name__)

# Conexión al SGBD
  ## reemplazar 'root' por el password del usuario administrador de MySQL
conn = mysql.connector.connect(user="root",host="localhost",password="root")
cursor = conn.cursor()
##cursor.execute("USE sakila")

# Definición de las rutas

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API Sakila</h1>
<p>Un prototipo de API para la base de datos Sakila.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run(debug=False,port=80)