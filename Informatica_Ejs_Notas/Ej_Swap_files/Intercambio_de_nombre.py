#!/usr/bin/env python3
import os

Archivo1= "Hola.txt"
Archivo2= "Chau.txt"

os.rename(Archivo1, Archivo2 + ".temp") 
os.rename(Archivo2,Archivo1)
os.rename(Archivo1, ".temp", Archivo2)

print("Archivos intercambiados con exito")

# os.path.exists

#modificar este script para que se puede incorporar el nombre de los archivos desde la terminal

