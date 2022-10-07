'''
dados 5 enteros positivos, encontrar losa valores minimos y maximos
que se puedan calcular sumando exactamente cuatro de los 5 enteros.

suma_mas_pequeña: 1 + 3 + 5 + 7
suma_mas_grande: 3 + 5 + 7 + 9

'''

l = [7, 1, 9, 3, 5]

def suma_max_min():
    maximo = sum(l) - min(l)
    minimo = sum(l) - max(l)
    print(maximo, minimo)

def suma_min_max():
    l.sort
    suma = sum(l)
    maximo = suma - l[0]
    minimo = suma - l[-1]
    print(minimo, maximo)

'''
dados 5 enteros positivos encontrar los 4 enteros que al sumarlos den 10
si es que es posible
'''
import itertools
def combi():
    lista = list(e for e in itertools.combinations(l, 3) if sum(e) == 10)
    return lista
