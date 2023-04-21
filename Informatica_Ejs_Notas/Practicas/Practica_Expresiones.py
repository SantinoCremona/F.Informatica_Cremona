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

#6)
# def buscar_strings_en_frase(frase, lista_strings):
#     for a in lista_strings:
#         if a in frase:
#             print(f'La frase "{a}" se encuentra en la frase dada.')
#         else:
#             print(f'La frase "{a}" no se encuentra en la frase dada.')
# frase = "El perro corre por el parque"
# lista_strings = ["perro", "gato", "corre"]
# buscar_strings_en_frase(frase, lista_strings)

#7)
# def palabra_con_limites (string):
#     patron = r'^[a-zA-Z0-9\s]+$'
#     if re.search(patron,string):
#         return "Cumple con requisitos"
#     else:
#         "No cumple"
# print(palabra_con_limites())

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

#11)
# def buscar_palabra_con_P(lista_strings):
#     for palabra in lista_strings:
#         palabras_separadas = palabra.split()
#     if len(palabras_separadas) >= 2 and palabras_separadas[0][0] == 'P' and palabras_separadas[1][0] == 'P':
#         print(palabra)
# lista_strings = ["Práctica Python", "Práctica C++", "práctica Fortran"]
# print(buscar_palabra_con_P(lista_strings))