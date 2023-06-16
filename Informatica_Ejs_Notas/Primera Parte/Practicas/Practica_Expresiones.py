#!/usr/bin/env python3
import re

#1) Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

# def caracteres_permitidos(string):
#     return bool(re.search('[a-zA-Z0-9.]',string))
# print(caracteres_permitidos("palabra"))

#2) Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

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

#4) Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

# def palabra_unida(string):
#     patron = "[aA-zZ]+_[aA-zZ]+$"
#     if re.search(patron, string) is not None:
#         return "Patron encontrado"
#     else:
#         return "Patron no encontrado"
# cadena = input("Ingrese cadena:")
# print(palabra_unida(cadena))

#5) Escribí un programa que diga si un string empieza con un número específico.

# def arranca_con(string):
#     patron = "5"
#     if re.search(patron,string) is not None:
#         return "Patron encontrado"
#     else:
#         "Patron no encontrado"
# print(arranca_con("5g"))

#6) Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

# def buscar_strings_en_frase(frase, lista_strings):
#     for a in lista_strings:
#         if a in frase:
#             print(f'La frase "{a}" se encuentra en la frase dada.')
#         else:
#             print(f'La frase "{a}" no se encuentra en la frase dada.')
# frase = "El perro corre por el parque"
# lista_strings = ["perro", "gato", "corre"]
# buscar_strings_en_frase(frase, lista_strings)

#7) Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

# def palabra_con_limites (string):
#     patron = r'^[a-zA-Z0-9\s]+$'
#     if re.search(patron,string):
#         return "Cumple con requisitos"
#     else:
#         "No cumple"
# print(palabra_con_limites())

#8) Escribí un programa que separe y devuelva los caracteres númericos de un string.

# def extraer_numeros(string):
#     resultado = re.split("\D+", string)
#     for elemento in resultado:
#         print(elemento)
# string = "Hoy viaje a la facultad en 2 bondis"
# extraer_numeros(string)

#9) Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

# def extraer_guiones(string):
#     return re.findall(r"-(.*?)-", string)
# string = "Hoy laburamos -con expresiones- bastante -bien-"
# print(extraer_guiones(string))

#10) Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

# def get_substr(string):
#     return re.findall("[@|&](.*?)[@|&]", string)
# string = "ssdaubafubauf@jdnjde& sd @ ini"
# lista_substr =  "ssdaubafubauf@jdnjde@ sd  &ini&"
# resultado = {}
# print(get_substr(lista_substr))

#11) Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

# def buscar_palabra_con_P(lista_strings):
#     for palabra in lista_strings:
#         palabras_separadas = palabra.split()
#     if len(palabras_separadas) >= 2 and palabras_separadas[0][0] == 'P' and palabras_separadas[1][0] == 'P':
#         print(palabra)
# lista_strings = ["Práctica Python", "Práctica C++", "práctica Fortran"]
# print(buscar_palabra_con_P(lista_strings))

#12) Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

# def cambiar_por_barra(string):
#     patron = r"[_:\s-]+"
#     coincidencia = re.search(patron,string)
#     if coincidencia:
#         return re.sub(patron,"|", string)
# print(cambiar_por_barra("hola_como:v a-p"))

#13) Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

# def cambiar_por_guion(string):
#     patron = "[\W]{2}"
#     coincidencia = re.search(patron,string)
#     if coincidencia:
#         return re.sub(patron,"_", string)
#     else:
#         return string
# print(cambiar_por_guion("Hola te va"))

#14) Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

# def cambiar_por_puntocoma(string):
#     patron = "[\s\t]+"
#     coincidencia = re.search(patron,string)
#     if coincidencia:
#         return re.sub(patron, ";", string)
# print(cambiar_por_puntocoma("   hola capo    como va"))

#15) Realizá un programa que validar si una cuenta de mail está escrita correctamente.

# def validacion(string):
#     patron = r"[aA-zZ0-9]+@+[a-z]+.com"
#     coincidencia = re.search(patron,string)
#     if coincidencia:
#         return "Mail correcto"
#     else:
#         return "Mail incorrecto"
# print(validacion("Cremona03@hotmail.com.ar"))
