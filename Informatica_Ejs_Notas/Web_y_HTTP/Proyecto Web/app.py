#API-->rutas(endpoint)-->una url en las cuales se accede a los recursos
#Api rest no solo los recursos sino que mapee bien los verbos http.
from flask import Flask, render_template, request, url_for, redirect
from markupsafe import escape

app = Flask(__name__)

prendas = {
    100: {"name": "Pantalon M", "price": 42},
    150: {"name": "Remera S", "price": 40}
}

@app.get("/") #se llama decorador a los que tienen @, determina la ruta y el metodo. El home se escribe como barra.
def home():
    return render_template("home.html") #<p></p> es etiqueta de parrafo. En vez de dominio hay puerto/IP. html es lenguaje de texto++, se basa en etiquetas

@app.get("/prendas/") #/prendas va a tener los verbos get(buscar las prendas) y post(agregar una prenda nueva)
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas.items())

@app.get("/prendas/<int:id>") #Va a tener los verbos get(traigo una sola prenda de id = x) y patch(modificar una prenda)
def get_una_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template("unaprenda.html", id=id, prenda=prenda )
    else:
        return ("No hay prenda", 404)

#Maquetado html
#<a></a> para agregar enlaces
#<br> salto de linea
#<div></div>
#<iframe></iframe> es para embeber iconos o videos, etc.

#css
#link es la etiqueta para conectar el html con el css
#va entre llaves: referencia a un elemento{atributos} y termina con ; para cerrar, excepto el ultimo elemento de la llave
#elemento se identifica con la etiqueta o class name
#Layout, donde de cada cosa
#padding espacio entre margenes, para centrar etc
#width y height para elegir cuanto ocupa un elemento
