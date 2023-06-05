#API-->rutas(endpoint)-->una url en las cuales se accede a los recursos
#Api rest no solo los recursos sino que mapee bien los verbos http.
from flask import Flask, render_template
from markupsafe import escape

prendas = [
    {"ID":1, "Tipo": "Pantalon", "Talle": 40},
    {"ID":2, "Tipo": "Pantalon", "Talle": 41}
]

app = Flask(__name__)

@app.get("/") #se llama decorador a los que tienen @, determina la ruta y el metodo. El home se escribe como barra.
def home():
    return render_template("home.html") #<p></p> es etiqueta de parrafo. En vez de dominio hay puerto/IP. html es lenguaje de texto++, se basa en etiquetas

@app.get("/prendas") #/prendas va a tener los verbos get(buscar las prendas) y post(agregar una prenda nueva)
def get_all_prendas():
    return render_template("prendas.html")

@app.get("/prendas/<id>") #Va a tener los verbos get(traigo una sola prenda de id = x) y patch(modificar una prenda)
def get_una_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"

#Maquetado html
#<a></a> para agregar enlaces
#<br> salto de linea
#<div></div>
#<iframe></iframe> es para embeber iconos o videos, etc.

#css
#link es la etiqueta para conectar el html con el css
#va entre llaves: referencia a un elemento{atributos} y termina con ; para cerrar, excepto el ultimo elemento de la llave
#elemento se identifica con la etiqueta o class name
