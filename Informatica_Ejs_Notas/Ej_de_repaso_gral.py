#Ejs 7 y 12 de Intro a python1
#7)
# def longitud_de_onda(rango):
#     return rango >= 223.0 and rango <= 586.8 and rango != 314.5
# print(longitud_de_onda(float(input("Ingrese Longitud:"))))

#12)
# def empieza_con_buenas_buenos(string):
#     if string.startswith("buenos"):
#         return "Arranca con buenos"
#     elif string.startswith("buenas"):
#         return "Arranca con buenas"
#     else:
#         return "No arranca con ninguna"
# print(empieza_con_buenas_buenos("clar dias"))

#Ej 5 de intro python2

# def volver_booleanos(lista):
#     resultado = []
#     for i in lista:
#         if i % 2 == 0:
#             resultado.append(True)
#         else:
#             resultado.append(False)
#     return resultado
# lista = [2, 45, 108, 12, 7]
# print(volver_booleanos(lista))

#Ej 2 y 6 manipulacion de arch
#2)
# archivo = "file.txt"
# n=1
# with open(archivo, "r") as file:
#     for i in range(n):
#         print(file.readline())

# def primeras_lineas(archivo):
#     with open(archivo, "r") as arch:
#         return arch.readlines()
# print(primeras_lineas("file.txt"))

#Ej 1 y 13 de expresiones regulares
#1)
import re
# def permitido(string):
#     patron = "[aA-zZ0-9]"
#     return bool (re.search(patron, string))
# print(permitido("bestia"))

#13)
# def cambio_por_guiones(string):
#     patron = r"[^\w]+"
#     coincidencia = re.search(patron, string)
#     if coincidencia:
#         return re.sub(patron,"_", string)
#     else:
#         return string
# print(cambio_por_guiones("buenas*como v?a"))

#10)
# def substrings(strings):
#     patron = "[@|&](.*?)[@|&]"
#     return re.findall(patron,strings)
# string = "@hdsbduh&jdidj &haha@"
# print(substrings(string))

#Examen hecho por chatgpt
#1)patron = r"^[aA-zZ]+$"
#3)

# def contar_palabras(archivo):
#     c = 0
#     with open (archivo, "r") as arch:
#         contenido = arch.readlines()
#         for contenido in contenido:
#             palabras = contenido.split()
#             c += len(palabras)
#         print(c)
# contar_palabras("file.txt")

# class Rectangulo:
#     def __init__(self,ancho,altura):
#         self.ancho = ancho
#         self.altura = altura
#     def area(self):
#         return self.ancho * self.altura
#     def perimetro(self):
#         return 2*self.ancho + 2*self.altura
#     def escalar(self, factor):
#         self.ancho *= factor
#         self.altura *= factor
    
# rectan1 = Rectangulo(4,8)
# rectan2 = Rectangulo(2,4)

# if rectan1.area() > rectan2.area():
#     print("rectangulo 1 tiene area mas grande que el 2")
# else:
#     print("al reves")
# print("El area del 1 es:", rectan1.area())
# print("El area del 2 es:", rectan2.area())

#Expresiones Regulares
#1)
# def permitido(strings):
#     patron = r"[aA-zZ0-9]"
#     coincidencia = re.search(patron,strings)
#     if coincidencia:
#         return "Patron permitido"
#     else:
#         return "Patron no permitido"
# print(permitido("###"))
    
# #2)
# def caracteres_permitidos(strings):
#     patron = "[^aA-zZ0-9]"
#     return not bool (re.search(patron,strings))
# print(caracteres_permitidos("palabra"))

# #4)
# def unida_por_guion(strings):
#     patron = "[aA-zZ]-[aA-zZ]"
#     coincidencia = re.search(patron, strings)
#     if coincidencia:
#         return "Unido"
#     else:
#         return "No unido"
# print(unida_por_guion("alas-mama"))

# #5)
# def arranca_con_num(strings):
#     patron = "^[0-9]+[aA-zZ]"
#     return bool(re.search(patron,strings))
# print(arranca_con_num("64g"))

# #6)
# def en_frase(frase, listastr):
#     for a in listastr:
#         if a in frase:
#             print(f"{a} esta")
#         else:
#             print(f"{a} no esta")
# listastr = ["papa", "crack","capo"]
# frase = "hola papa como estas crack"
# en_frase(frase, listastr)

# #7)
# def limites(strings):
#     patron = "^[aA-zZ0-9\s]+$"
#     return bool(re.search(patron,strings))
# print(limites("aA03 as"))

# #8)
# def separar_num(strings):
#     patron = "[\D]"
#     extraccion = re.split(patron, strings)
#     for a in extraccion:
#         print(a)
# print(separar_num("me tome 2 bondis a 3 cuadras"))

# #9)
# def extraer_entre_guiones(strings):
#     patron = "-(.*?)-"
#     return re.findall(patron, strings)
# print(extraer_entre_guiones("hola -mama-como -estas-"))

# #10)
# def obtener_substr(strings):
#     patron = "[@|&](.*?)[@|&]"
#     return re.findall(patron, strings)
# print(obtener_substr("@ffty&@ctct@@tftfy&"))

# #12)
# def reemplazo_por_barra(strings):
#     patron = "[\s_:]+"
#     coincidencia = re.search(patron,strings)
#     if coincidencia:
#         return re.sub(patron, "|", strings)
#     else:
#         return strings
# print(reemplazo_por_barra("hola ma_que:estas buscando"))

# #13)
# def reemplazo_por_guion(strings):
#     patron = "[\W]+"
#     coincidencia = re.search(patron,strings)
#     if coincidencia:
#         return re.sub(patron, "_", strings)
#     else:
#         return strings
# print(reemplazo_por_guion("hola como*va"))

# #14)
# def reemplazo_por_puntocoma(strings):
#     patron = "[\s\t]+"
#     coincidencia = re.search(patron, strings)
#     if coincidencia:
#         return re.sub(patron, ";",strings)
# print(reemplazo_por_puntocoma("hola que onda    todo"))

# #15)
# def ver_mail(strings):
#     patron = "[aA-zZ0-9]+@+[a-z]+.com"
#     return re.search(patron,strings)
# print(ver_mail("crema32@gmail.com"))

#Manipulacion de archivos
#1)
# def lineas_arranca_con_p(archivo):
#     c = 0
#     with open(archivo, "r") as file:
#         for linea in file:
#             if not linea.startswith("p"):
#                 c += 1
#         print(c)
# print(lineas_arranca_con_p("file.txt"))

#2)
# def primeras_lineas(archivo):
#     with open(archivo, "r") as arch:
#         for i in range(1):
#             print(arch.readline())
# primeras_lineas("file.txt")

#3)
# def ultimas_lineas(archivo):
#     with open(archivo, "r") as arch:
#         lineas = arch.readlines()
#     n = int(input("Ingrese el número de líneas a imprimir: "))
#     for linea in lineas[-n:]:
#         print(linea)
# print(ultimas_lineas("Teoria.txt"))

#4)
# def cantidad_palabras(archivo):
#     with open(archivo, "r") as arch:
#         contenido = arch.read()
#         palabras = contenido.split()
#     print(len(palabras))
# print(cantidad_palabras("Teoria.txt"))

#5)
# def reemplazo_letra(archivo, archivo2):
#     with open (archivo, "r")as arch:
#         contenido = arch.read()
#     letra = input("Letra:")
#     letra_cambiada = letra + "\n"
#     contenido2 = contenido.replace(letra, letra_cambiada)
#     with open (archivo2, "a") as nuevo:
#         nuevo.write(contenido2)
# print(reemplazo_letra("Teoria.txt", "nuevo.txt"))

#6)
# def eliminar_saltos(archivo, archivo2):
#     with open(archivo, "r") as arch:
#         contenido = arch.read()
#     contenido2 = contenido.replace("\n", "")
#     with open(archivo2,"a") as nuevo:
#         nuevo.write(contenido2)
# print(eliminar_saltos("Teoria.txt", "nuevo.txt"))

#7)
# def palabra_mas_larga(archivo):
#     with open(archivo, "r") as arch:
#         contenido = arch.read()
#         palabras = contenido.split()
#     palabra_mas_larga = ""
#     longitud_palabra_mas_larga = 0
#     for palabra in palabras:
   
#         if len(palabra) > longitud_palabra_mas_larga:
#             palabra_mas_larga = palabra
#             longitud_palabra_mas_larga = len(palabra)

#     print("La palabra más larga es:", palabra_mas_larga)
#     print("Tiene", longitud_palabra_mas_larga, "caracteres.")
# print(palabra_mas_larga("Teoria.txt"))

#8)
# def dos_en_uno(archivo, archivo2, nuevo):
#     with open(archivo, "r") as arch:
#         contenido = arch.read()
#         with open(archivo2, "r") as arch2:
#             contenido2 = arch2.read()
#             with open(nuevo, "a") as nuevo:
#                 nuevo.write(contenido + contenido2)
# print(dos_en_uno("file.txt", "file2.txt", "nuevo.txt")) 

#9)
# def frecuencia(archivo):
#     with open(archivo, "r") as arch:
#         contenido = arch.read()
#         palabras = contenido.split()
#     frecuencia = palabras.count(input("Palabra:"))
#     print("La frecuencia de la palabra es", frecuencia)
# print(frecuencia("file.txt"))

#SIMULACRO
#1)
# def entre_X_Y(strings):
#     patron = r"X(.*?ab.*?)Y"
#     return re.findall(patron, strings)
# print(entre_X_Y("XababYXbaYXababX"))

# def entre_ag_cta(strings):
#     patron = r"ag(.*?)cta"
#     return re.findall(patron,strings)
# print(entre_ag_cta("aghaca34cta"))

# import glob
# def mails(archivo,archivo2):
#     with open(archivo, "r")as arch:
#         contenido = arch.read()
#         patron = "[aA-zZ0-9]+@gmail.com"
#         contenido2 = re.findall(patron, contenido)
#     with open(archivo2, "a")as base:
#         for email in contenido2:
#             base.write(email + "\n")
# print(mails("",""))

# class Pacman:
#     def __init__(self):
#         self.puntos = 0
#         self.vidas = 3

#     def comer_bolitas(self, bolitas):
#          self.puntos += bolitas

#     def pierde_vida(self):
#         self.vidas -=1

#     def comer_fantasma(self, fantasma):
#         self.puntos += fantasma


def exre(strings):
    patron = "ab"
    return re.findall(patron, strings)
print(exre("caaaababc aaaa acb aeb aa1babbba "))

