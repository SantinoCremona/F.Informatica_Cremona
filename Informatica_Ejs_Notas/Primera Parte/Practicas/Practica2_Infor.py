#!/usr/bin/env python3

#1)
#def revisar_lista(lista):
#    if "control" in lista:
#        lista.remove("control")
#        lista.append("revisado")
#    return lista
#lista1 = ["control","avion", "auto", "moto"]
#lista1Revisada = revisar_lista(lista1)
#print(lista1Revisada)

#2)
#def eliminar_primer_elemento(lista):
#    return lista.remove
#listaA = [1,2,3,4]
#listaA_0eliminado = eliminar_primer_elemento(listaA)
#print(listaA_0eliminado)

#3)
#def encontrar_posicion(lista, elemento):
#        return lista.index(elemento)
#lista = [1, 2, 3, 4, 5]
#print(encontrar_posicion(lista, 2))  
#print(encontrar_posicion(lista, 1))  

#4)
# def mover_elemento_v1(lista1, lista2, elemento):
#     if elemento in lista1:
#         lista1.remove(elemento)
#         lista2.append(elemento)
    
# def mover_elemento_v2(lista1, lista2, elemento):
#     index = lista1.index(elemento)
#     lista2.append(lista1.pop(index))

# lista1=[1, 2, 3, 4, 5]
# lista2=[6, 7, 8, 9, 10]
# lista_movida=mover_elemento_v1(lista1,lista2)
# print(lista_movida)

#5)
# lista = [2,5,22,9]
# def lista_a_booleano(par, impar):
#     num%2=0
#     if par in lista:
#         return True
#     elif impar in lista:
#         return False
# print(lista_a_booleano)

#6)
#def cantidad_de_apariciones(string):
#     apariciones = {}
#     for caracter in string:
#         if caracter in apariciones:
#             apariciones[caracter] += 1
#         else:
#             apariciones[caracter] = 1
#     return apariciones
# print(cantidad_de_apariciones("Paaper"))

#9)
# def productoria(lista):
#     mult = 1
#     for i in lista:
#         mult *= i 
#     return mult
# print(productoria([1,2,4,5]))

#10)
# import datetime

# socios_fundadores = {
#     1: {
#         "nombre": "Florencia",
#         "apellido": "Ocampo",
#         "fecha_ingreso": datetime.date(2001, 9, 14),
#         "cuota_al_dia": True
#     },
#     2: {
#         "nombre": "David",
#         "apellido": "Estévez",
#         "fecha_ingreso": datetime.date(2001, 9, 14),
#         "cuota_al_dia": True
#     },
#     3: {
#         "nombre": "Sofía",
#         "apellido": "Cáceres",
#         "fecha_ingreso": datetime.date(2001, 9, 14),
#         "cuota_al_dia": True
#     }
# }

# def cargar_socio(numero, nombre, apellido, fecha_ingreso, cuota_al_dia):
#     socios[numero] = {
#         "nombre": nombre,
#         "apellido": apellido,
#         "fecha_ingreso": fecha_ingreso,
#         "cuota_al_dia": cuota_al_dia
#     }

# socios = socios_fundadores.copy()

# print("El club tiene", len(socios), "socios.")

# numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas: "))
# socio = socios.get(numero_socio)
# if socio:
#     socio["cuota_al_dia"] = True
#     print("Se ha registrado que el socio", numero_socio, "ha pagado todas las cuotas.")
# else:
#     print("No se ha encontrado el socio", numero_socio, "en el listado.")

# for numero, socio in socios.items():
#     if socio["fecha_ingreso"] == datetime.date(2017, 10, 21):
#         socio["fecha_ingreso"] = datetime.date(2017, 10, 22)

# nombre = input("Ingrese el nombre del socio a dar de baja: ")
# apellido = input("Ingrese el apellido del socio a dar de baja: ")
# socio_encontrado = False
# for numero, socio in socios.items():
#     if socio["nombre"] == nombre and socio["apellido"] == apellido:
#         del socios[numero]
#         socio_encontrado = True
# if socio_encontrado:
#     print("Se ha dado de baja al socio", nombre, apellido)
# else:
#     print("No se ha encontrado al socio", nombre, apellido, "en el listado.")

# print("Listado de socios:")
# for numero, socio in socios.items():
#     print("Número:", numero)
#     print("Nombre completo:", socio["nombre"], socio["apellido"])
#     print("Fecha de ingreso:", socio["fecha_ingreso"].strftime("%d/%m/%Y"))
#     if socio["cuota_al_dia"]:
#         print

