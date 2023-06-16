import re, os, glob
#1a)
#armar el patron
# def encontrar_xy(string):
#    #patron = "X(.*?ab.*?)Y"
#    patron="X([^XY]*ab[^XY]*)Y" 
#    return re.findall(patron,string)
# print(encontrar_xy("XababYXbabbbaaYababY"))

#1b)
#def funcionDeExpresiones_Regulares():
#    return re.findal("ag\d.*?)cta")
# Falso, porque tiene que tener un parametro y el nombre tiene que estar escrito todo en minisculas con guion bajo y el nombrede la funcion debe ser expresivo.
# El error es AttributeError> module "re", porque findall esta mal escrito. Si se corrige eso el error es Typeerror
# def entre_ag_cta_sin_numeros(string):
#    return re.findall("ag([^\d]*)cta",string)

#2)
# def filtrar(archivo):
#     lista_txt = glob.glob("*.txt")

#     with open(archivo, "a") as arch:
#         for archivo in lista_txt:
#             with open(archivo, "r") as archivo_secreto:
#                 texto = archivo_secreto.read()
#                 lista = re.findall("[\W]+[-_\.]*[\W]+@gmail.com", texto)
#                 for email in lista:
#                     arch.write(email + "\n")
# print(filtrar("gmails.txt"))

# def buscar_mails(miarch, nuevo):
#     with open("gmails.txt", "r") as miarch:
#         contenido = miarch.read()
#         patron = '[Aa-zZ0-9]+@gmail.com'
#         contenido2 =  re.findall(patron, contenido)
#         with open ("gmails2.txt", "a") as nuevo:
#             for email in contenido2:
#                 nuevo.write(email + "\n")

# print(buscar_mails("gmails.txt", "gmails2.txt"))

#4)
# class  Fantasma:
#     def __init__(self):
#         self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
#     def puntos_color(self, color):
#         return self.fantasmas[color]


# class PacMan(Fantasma):
#     def __init__(self):
#         super().__init__()
#         self.puntos = 0
#         self.vidas = 3

#     def comer_bolitas(self, bolas):
#         self.puntos += 2 * bolas

#     def comer_fantasma(self, fantasma, color):
#         self.puntos += fantasma.puntos_color(color)

#     def va_mas_rapido(self): 
#         return 2 + self.puntos/100

#     def pierde_vida(self):
#         self.puntos = 0
#         self.vidas -= 1
#         if self.vidas == 0:
#             return "Game Over"

# mat = PacMan()
# fantasma = Fantasma()

# print(mat.puntos)
# print(mat.comer_bolitas(10))
# print(mat.puntos)

# print(mat.vidas)
# mat.pierde_vida()
# print(mat.vidas)
# mat.pierde_vida()
# mat.pierde_vida()
# print(mat.vidas)
# print(mat.vidas)