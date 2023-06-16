#!/usr/bin/env python3

#1)
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

# archivo = open("file.txt", "r")
 
# contador = 0
# for linea in archivo:
#    if not linea.startswith("n"):
#        contador += 1
# archivo.close()
# print("Hay", contador, "líneas que no comienzan con la letra n")

#2)
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

#archivo = "file.txt"
#n=1
#with open(archivo, "r") as file:
#    for i in range(n):
#        print(file.readline())

#3)
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

#with open("file.txt", "r") as archivo:
#    lineas = archivo.readlines()
#n = int(input("Ingrese el número de líneas a imprimir: "))
#for linea in lineas[-n:]:
#    print(linea)

#4)
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

#with open("file.txt", "r") as arch:
#    contenido=arch.read()
#palabras=contenido.split()
#cantidad_palabras=len(palabras)
#print(cantidad_palabras)

#5)
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

#archivo1 = open("archivo1.txt", "r")
#contenido = archivo1.read()
#letra = "h"
#letra_cambiada =letra + "\n"
#contenido2=contenido.replace(letra, letra_cambiada)
#archivo2= open("archivo2.txt", "w")
#archivo2.write(contenido2)

#6)
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

#archivo1 = open("archivo1.txt", "r")
#contenido = archivo1.read()
#contenido2=contenido.replace("\n", "")
#archivo2= open("archivo2.txt", "w")
#archivo2.write(contenido2)

#7)
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
# with open("file.txt", "r") as arch:
#     contenido = arch.read()
#     palabras = contenido.split()

# palabra_mas_larga = ""
# longitud_palabra_mas_larga = 0
# for palabra in palabras:
   
#     if len(palabra) > longitud_palabra_mas_larga:
#         palabra_mas_larga = palabra
#         longitud_palabra_mas_larga = len(palabra)

# print("La palabra más larga es:", palabra_mas_larga)
# print("Tiene", longitud_palabra_mas_larga, "caracteres.")

#8)
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
# with open('file.txt', 'r') as archivo1:
#    with open('file2.txt', 'r') as archivo2:
#         with open('nuevo.txt', 'w') as archivo_resultado:
#             contenido1 = archivo1.read()
#             contenido2 = archivo2.read()
#             archivo_resultado.write(contenido1 + contenido2)

#9)
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
# with open("file.txt", "r") as arch:
#     contenido = arch.read()
#     palabras = contenido.split()
#     frecuencia = palabras.count(input("palabra:"))
# print("La frecuencia de la palabra es", frecuencia)

#10)
#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

# import os

# carpeta_entrada = 'Carpeta1'
# carpeta_salida = os.path.join(carpeta_entrada, 'Resultado')
# if not os.path.exists(carpeta_salida):
#     os.makedirs(carpeta_salida)

# archivo_salida = open(os.path.join(carpeta_salida, 'todos_los_archivos.txt'), 'w', encoding='utf-8')

# for nombre_archivo in os.listdir(carpeta_entrada):
#     if nombre_archivo.endswith('.txt'):
#         ruta_archivo = os.path.join(carpeta_entrada, nombre_archivo)
#         archivo = open(ruta_archivo, 'r', encoding='utf-8')
#         contenido = archivo.read()
#         archivo.close()
        
#         archivo_salida.write('Archivo: {}\n\n{}\n\n'.format(nombre_archivo, contenido))
# archivo_salida.close()
