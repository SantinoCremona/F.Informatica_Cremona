from aves import pepita, anastasia, roberta

# print(pepita.volar_en_circulos())
# print(pepita.hablar())
# print(pepita.comer_alpiste(200))
#aprendimos que pepita es una golondrina, que vuela, come alpiste pero no habla

# print(pepita.energia)
# print(pepita.volar_en_circulos())
# print(pepita.energia)
#objetos tienen atributos(caracteristicas) y tambien tienen estado(como su energia)
#el estado de los objetos puede cambiar al darle ordenes

# print(anastasia.energia)
# (anastasia.volar_en_circulos())
# print(anastasia.energia)
# (anastasia.comer_alpiste(200))
# print(anastasia.energia)
# print(type(anastasia))
#anastasia tiene distinto estado que pepita, a pesar de eso entienden mismos mensajes(metodos)

# print("Llamemos a Roberta")
# print("Energia al principio:", roberta.energia)
# roberta.volar_en_circulos()
# print("Energia post-volar:", roberta.energia)
# roberta.comer_alpiste(200)
# print("Energia post-comer", roberta.energia)
#Es un dragon, no come al piste
# roberta.escupir_fuego()
# print("Energia post-escupir fuego:", roberta.energia)
# roberta.comer_peces(200)
# print("Energia post-comer", roberta.energia)
#Hay objetos que entienden los mismos mensajes aunque no sean de la misma clase.
#esos mensajes que entienden se llaman interfaces
#los objetos que comparten su interfaz son polimorficos. En este caso es polimorfismo parcial
