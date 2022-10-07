from random import randint

def ahorcado():
    with open('palabras.txt') as f:
        total_lines = sum(1 for line in f)

    n = randint(1, total_lines)
    l = ['',]
    r = []
    l_aux = []

    with open('palabras.txt', 'r') as f:
        for line in f.readlines():
            l.append(line)

    for i in l[n]:
        r.append(i)

    l_aux.append('_ ' * (len(r) - 1))

    opciones = ['1: Iniciar intento', '2:Finalizar']
    for i in opciones:
        print(i)
    opcion = input('Elija una opción: ')

    if opcion == '2':
        return('Gracias por participar.')

    while True:
        for i in r:
            for _ in l_aux:
                letra = input('Introduzca una letra en el ahorcado: ')
                cont = 0
                if letra in r:
                    l[cont] = i
                if r == l_aux:
                    return('Enhorabuena has ganado.')
                cont += 1
