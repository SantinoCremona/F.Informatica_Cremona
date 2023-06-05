import requests

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") #get es el verbo asociado HTTP asociado a las consultas. Este le pregunta al servidor que onda y trae la info.
datos = respuesta.json() #json es una estructura de dato y es un diccionario
print(datos)
print(len(datos)) #en cuantas orgs esta el usuario
#nombre de las orgs. en las que esta involucrado
print(respuesta.headers) #headers da info. sobre el propio pedido
print(respuesta.status_code) #te da el codigo 
#HTTP tiene 5 verbos: get, post(escribe datos nuevos), delete(borra datos), patch(reescribe o modifica datos), put(modifica todos los datos)
#http solo recibe datos que son textos.

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto") #url accedes recurso via internet, similar a un path solo que el path accede a archivos locales.
datos = respuesta.json()
print(datos.keys()) #keys te muestra las cosas que tiene ese diccionario
print(respuesta.headers["Content-type"]) 
print(respuesta.status_code)
print(len(datos["abilities"]))

#1) El protocolo es https://, el dominio(nombre con el que se mapea una url particular) es pokeapi.co, el recurso(cosas que puedo consultarde la base de datos) es api/v2/pokemon/ditto
#2) Obtengo todos los contenidos al recurso Ditto, con los detalles de sus caracteristicas. Haciendo un .json()
#3) El content type es un json(que es un diccionario). Para sacar el content type usas headers["Content-type"]
#4) El status code es 200.
#5) Tiene 2 habilidades.




