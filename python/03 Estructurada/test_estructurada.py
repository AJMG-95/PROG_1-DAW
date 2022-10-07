'''
PI segun leibnitz
el numerador va alternando 1 y -1
'''

def leibnitz():
    res = 0
    num = 1
    den = 1
    while True:
        term = num / den
        res += term
        if abs(term) < 1e-4:
            break
        num = -num
        den += 2
    return res * 4

'''
PI según wallis
'''

""" def wallis1():
	n = int(input('numero de factores: '))
    numerador = 2
    denominador = 1
	pi = 1
	for i in range(n):
      pi = pi * (numerador / denominador)
        if i % 2 != 0:
            numerador += 2
        else:
            denominador += 2
	print(pi * 2)
 """


def wallis():
    num = 2
    denom = 1
    pi = 1
    i = 0
    while i < 5000:
        pi = pi * (num / denom)
        if i % 2 != 0:
            num += 2
        else:
            denom += 2
        i += 1
    return pi * 2


def wallis2():
    res = 1
    numer = 2
    denom = 1
    for i in range(5000):
        term = numer / denom
        res *= term
        if i % 2 == 0:
            denom += 2
        else:
            numer += 2
    return res * 2


'''
PI segun vieta
'''
from math import sqrt

def vieta():
    num = 2
    den = sqrt(2)
    res = 1
    while True:
        term = num / den
        res *= term
        if term < 1 + 1e-5:
            break
        den = sqrt(2 + den)
    return res * 2


'''
Adivina el numero
'''
import random
def adivinar_numero():
    rand = random.randint(0, 99)
    num = int(input('Introduce un número: '))
    while True:
        if num == rand:
            print('¡Acertaste!')
            break
        if num < rand:
            print('Es demasiado pequeño.')
        elif num > rand:
            print('Es demasiado grande.')
        num = int(input('Introduce un número:'))


'''
isograma
'''
def isograma_mal(palabra):
    palabra = palabra.lower().replace(' ','')
    cont = 0
    lon = len(palabra)
    i = 0
    while i < lon:
        if palabra[0] in palabra[1:]:
            cont += 1
        else:
            palabra = palabra[1:]
        i += 1
    if cont > 0:
        print(False)
    else:
        print(True)


def isogram(str25):
    str25 = str25.lower().replace(' ', '')
    lon = len(str25)
    i = 0
    while i < lon:
        if str25[0] in str25[1:]:
            return False
        str25 = str25[1:]
    return True


def isogra(str25):
    str25 = str25.lower().replace(' ', '')
    for i in str25:
        if i in str25[1:]:
            return False
        str25 = str25[1:]
    return True


def isograma(cad):
    cad = cad.lower().replace(' ','')
    carac = set(cad)
    if len(cad) == len(carac):
        return True
    return False


def isograma2(palabra):
    palabra = palabra.lower().replace(' ', '')
    repeticiones = set(palabra)
    "".join([str(_) for _ in repeticiones])
    if len(palabra) == len (repeticiones):
        return True
    return False


'''
distancia hamming
'''
def hamming (cad1, cad2):
    """Calcula la distancia de hamming

    Args:
        cad1 (str): una cadena de longitud x
        cad2 (str): una cadena de longitud igual a la anterior

    Returns:
        [int]: El valor de la distancia hamming
    """
    cont = 0
    aux = list(zip(cad1, cad2))
    for e in aux:
        if e[0] != e[1]:
            cont += 1
    return cont


def hamming2 (cad1, cad2):
    cont = 0
    for x, y in zip(cad1, cad2):
        if x != y:
            cont += 1
    return cont


def hamming3(cad1, cad2):
    acum = 0
    for i, car1 in enumerate(cad1):
        if car1 != cad2[i]:
            acum += 1
    return acum


def hamming4(cad1, cad2):
   return list(map(lambda t: 1 if t[0] != t[1] else 0, zip(cad1, cad2)))
    # Muestra las posiciones en las que encuentra una diferencia entre las
    #  cadenas


def hamming5(cad1, cad2):
    return sum(map(lambda t: 1 if t[0] != t[1] else 0, zip(cad1, cad2)))
    # Retorna la distancia hamming


def hamming6(cad1, cad2):
    return sum(map(lambda x, y: 1 if x != y else 0, cad1, cad2))
