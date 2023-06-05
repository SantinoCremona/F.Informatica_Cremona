import requests

rta = requests.get("https://pokeapi.co/api/v2/ability/150") #ability te trae todas las habilidades. Si agregas /id(el cual es un parametro) te trae la habilidad que esta en determinada fila
print(rta.json())

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon') # el ? busca, como hay una key que es tipo, buscamos el tipo que sea = a pantalon. Si queres concatenar parametros usas &.
r.json()
#query params, son todas las claves que le paso a la api a traves de la url para filtrar la busqueda en su base de datos. 

