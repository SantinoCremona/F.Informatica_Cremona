#!/usr/bin/env python3
import re

#1)
# def caracteres_permitidos(string):
#     return bool(re.search('[a-zA-Z0-9.]',string))
# print(caracteres_permitidos("palabra"))

#2)
# def caracteres_permitidos(string):
#     return not bool(re.search('[^a-zA-Z0-9]',string))
# print(caracteres_permitidos("pala"))

#3)
# def encontrar_patron(string):
#     patron = "he*" 
#     if re.search(patron, string) is not None:
#         return "Se encontro el patron"
#     else:
#         return "No se encontro el patron"
# print(encontrar_patron("a"))
# print(encontrar_patron("h"))
# print(encontrar_patron("he"))
# print(encontrar_patron("heeee"))

# def encontrar_patron(string):
#     patron = "he+" 
#     if re.search(patron, string) is not None:
#         return "Se encontro el patron"
#     else:
#         return "No se encontro el patron"
# print(encontrar_patron("a"))
# print(encontrar_patron("h"))
# print(encontrar_patron("he"))
# print(encontrar_patron("heeee"))

# def encontrar_patron(string):
#     patron = "he?" 
#     if re.search(patron, string) is not None:
#         return "Se encontro el patron"
#     else:
#         return "No se encontro el patron"
# print(encontrar_patron("he"))
# print(encontrar_patron("heeee"))

# def encontrar_patron(string):
#     patron = "he{2,3}" 
#     if re.search(patron, string) is not None:
#         return "Se encontro el patron"
#     else:
#         return "No se encontro el patron"
# print(encontrar_patron("he"))
# print(encontrar_patron("hheeey"))

#4)
# def palabra_unida(string):
#     patron = "^[aA-zZ]+_[aA-zZ]+$"
#     if re.search(patron, string) is not None:
#         return "Patron encontrado"
#     else:
#         return "Patron no encontrado"
# cadena = input("Ingrese cadena:")
# print(palabra_unida(cadena))

#5)
# def arranca_con(string):
#     patron = "5"
#     if re.search(patron,string) is not None:
#         return "Patron encontrado"
#     else:
#         "Patron no encontrado"
# print(arranca_con("5g"))

#8)
# def extraer_numeros(string):
#     resultado = re.split("\D+", string)
#     for elemento in resultado:
#         print(elemento)
# string = "Hoy viaje a la facultad en 2 bondis"
# extraer_numeros(string)

#9)
# def extraer_guiones(string):
#     return re.findall(r"-(.*?)-", string)
# string = "Hoy laburamos -con expresiones- bastante -bien-"
# print(extraer_guiones(string))

#10)
# def get_substr(string):
#     return re.findall("[@|&](.*?)[@|&]", string)
# string = "ssdaubafubauf@jdnjde& sd @ ini"
# lista_substr =  "ssdaubafubauf@jdnjde@ sd  &ini&"
# resultado = {}
# print(get_substr(lista_substr))

