from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/libros")
def consultar_libros():
    return 'Consultar libros'

@app.post("/libros")
def cargar_libro():
    libro = request.json
    return f"Cargar libro: {libro}"

@app.delete("/libros/<id>")
def borrar_libro(id):
    return f"Borrar libro con ID: {id}"


