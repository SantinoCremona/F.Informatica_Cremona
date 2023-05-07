import re

#Encuentra todas las palabras que comiencen con la letra "a" en una cadena de texto:

def palabras_a(strings):
    patron = r"[aA][aA-zZ]+"
    return re.findall(patron, strings)
print(palabras_a("Abrimos la pana asi que adios"))

#Encuentra todas las direcciones de correo electrónico en una cadena de texto:

def mails(strings):
    patron = "[aA-zZ0-9]+@gmail.com"
    return re.findall(patron, strings)
print(mails("mi mail es crema@gmail.com y el de papa mike@gmail.com"))

#Encuentra todas las palabras que tengan exactamente tres letras en una cadena de texto:

def tres_letras(strings):
    patron = r"\b[aA-zZ]{3}\b"
    return re.findall(patron, strings)
print(tres_letras("buenas ana cae bien"))

#Encuentra todas las palabras que terminen con la letra "o" en una cadena de texto:

def termina_con_o(strings):
    patron = "[aA-zZ]+o"
    return re.findall(patron, strings)
print(termina_con_o("capo no me pasas la mayo"))

#Encuentra todas las palabras que contengan una "e" entre dos letras "r" en una cadena de texto:

def e_entre_r(strings):
    patron = r"\b[aA-zZ]*[rer]+\b"
    return re.findall(patron, strings)
print(e_entre_r("erremos el gol querer, merer"))