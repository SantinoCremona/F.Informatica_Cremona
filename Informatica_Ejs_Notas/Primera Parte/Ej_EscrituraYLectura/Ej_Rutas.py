#!/usr/bin/env python3

import os, glob, sys

# def ejercicio_rutas():
#     os.chdir("Informes")
#     txt = glob.glob("*.txt")
#     cantidad_estado = []
#     cantidad_lineas = []
#     for archivo in txt:
#         with open(archivo, "r") as file:
#             file_completa = file.read()
#             cantidad_estado.append(file_completa.count("estado"))
#             cantidad_lineas.append(file_completa.count("\n"))
#     os.mkdir("Apellido")
#     with open("Apellido/Lista.txt","w") as salida:
#         for archivo in txt:
#             with open(archivo, "r") as file:
#                 #primer_linea=file.readline()
#                 salida.write(file.readline())
#     return cantidad_estado, cantidad_lineas
# c1,c2 = ejercicio_rutas()

#Clonar la carpeta que te dan.

# def primeras_lineas(path_a_txt, path_a_resultado, salida):
#     os.chdir(path_a_txt)
#     textos = glob.glob("*.txt")
#     primer_linea = []
#     for txt in textos:
#         with open(txt,"r") as texto:
#             primer_linea.append(texto.readline())
#     os.chdir("../../")
#     os.mkdir(path_a_resultado)
#     os.chdir(path_a_resultado) 
#     with open(salida,"a") as final_txt:
#         for linea in primer_linea:
#             final_txt.write(linea)
# primeras_lineas("Datos/Marzo", "Resultado", "Salida.txt")