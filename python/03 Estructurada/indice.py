l = ['a', 25, 'hola', True]

#? i = 0
#? while i < len(l):
#?    print(i, l[i])
#?    i += 1

'''
Donde i es un índice 0, 1, 2, 3, 4
'''

#? for i in range(len(l)):
#?   print(i, l[i])

'''
El pylint me dice que use enumerate() en lugar de usar range(len())
'''

for i, e in enumerate(l):
    print(i, e)

'''
Esta tecnuca es la que mejor funciona, y es la más correcta segun las reglas de estilo

El eumerate() es un flujo de datos que son tuplas, que contienen el indice del elemento y el
elemento, por ello al for se le pasa i como el valor del indice (0, 1, 2,...) y la
e como el elemento de la tupla que corresponde al elemento de la lisata que se esta
recorriendo
'''
