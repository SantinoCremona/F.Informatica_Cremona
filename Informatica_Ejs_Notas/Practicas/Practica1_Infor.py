#!/usr/bin/env python3

#1)
#def siguiente (numeros):
#   return numeros + 1
#print(siguiente(int(input("Ingrese numero:"))))
#def anterior (numeros):
#   return numeros - 1
#print(anterior(int(input("Ingrese numero:"))))

#2)
#def doble(numeros):
#    return numeros * 2
#print(doble(int(input("Ingrese numero:"))))

#3)
#def doblesig (numeros):
#    return (numeros + 1)*2
#print(doblesig(4))
#def dobleant (numeros):
#    return (numeros - 1)*2
#print(dobleant(2))

#4)
#def retirar_dinero(saldo, montoretirado):
#    return max(saldo - montoretirado,0)
#print(int(input("Queda:" +str(retirar_dinero(20,10)))))

#5)
#def dia_de_la_semana_favorito (dia):
#    return dia == "Sábado"
#print(dia_de_la_semana_favorito("Martes"))
#print(dia_de_la_semana_favorito("Sábado"))

#6
# def longitud_de_onda(rango):
#     return rango >= 223.0 and rango <= 586.8 
# print(longitud_de_onda(float(input("Ingrese longitud:"))))

#7)
# def longitud_de_onda(rango):
#     return rango >= 223.0 and rango <= 586.8 and rango != 314.5
# print(longitud_de_onda(float(input("Ingrese longitud:"))))

#8)
# def tiene_descuento(edad):
#     return edad <= 12 or edad >= 60
# print(tiene_descuento(int(input("Ingrese edad:"))))

#10)
# def saludador(nombre, apellido):
#     return "Hola " + nombre + apellido
# print(saludador(input("Nombre:") , input("Apellido:")))


#11)
#def string(palabra): 
#    if palabra[0] == "H":
#        return(len(palabra))
#    else: 
#        return("No empieza con H")
#print(string("Helado"))

#12)
# def empieza_con_buenos(string):
#     return string.startswith("Buenos") or string.startswith("Buenas")
# print(empieza_con_buenos("Buenas"))
# print(empieza_con_buenos("Boca"))

#13) 
# def es_multiplo(N1,N2):
#     return N2 % N1 == 0
# print(es_multiplo(8,16))

#14)
def par_impar(numerop):
    numerop == int(input("Numero:"))
    if numerop%2==0:
        print("Par")
    else:
        print("Impar")
    return
print(par_impar)

