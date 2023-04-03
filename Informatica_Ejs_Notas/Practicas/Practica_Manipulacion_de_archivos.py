#1)
#archivo = open("file.txt", "r")
 
#contador = 0
#for linea in archivo:
#    if not linea.startswith("n"):
#        contador += 1
#archivo.close()
#print("Hay", contador, "líneas que no comienzan con la letra n")

#2)
#archivo = "file.txt"
#n=1
#with open(archivo, "r") as file:
#    for i in range(n):
#        print(file.readline())

#3)
#with open("file.txt", "r") as archivo:
#    lineas = archivo.readlines()
#n = int(input("Ingrese el número de líneas a imprimir: "))
#for linea in lineas[-n:]:
#    print(linea)

#4)
#with open("file.txt", "r") as arch:
#    contenido=arch.read()
#palabras=contenido.split()
#cantidad_palabras=len(palabras)
#print(cantidad_palabras)

#5)
#archivo1 = open("archivo1.txt", "r")
#contenido = archivo1.read()
#letra = "h"
#letra_cambiada =letra + "\n"
#contenido2=contenido.replace(letra, letra_cambiada)
#archivo2= open("archivo2.txt", "w")
#archivo2.write(contenido2)

#6)
#archivo1 = open("archivo1.txt", "r")
#contenido = archivo1.read()
#contenido2=contenido.replace("\n", "")
#archivo2= open("archivo2.txt", "w")
#archivo2.write(contenido2)