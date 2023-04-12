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
#     numb%2=0
#     if par in lista:
#         return True
#     elif impar in lista:
#         return False
# print(lista_a_booleano)