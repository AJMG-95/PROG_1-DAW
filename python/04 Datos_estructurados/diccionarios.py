
# cuadrado en forma de filas
c = [
    [2, 9, 4],
    [7, 5, 3],
    [6, 1, 8]
]
cc = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
d = [
    [2, 9, 4],
    [7, 5, 7],
    [6, 1, 8]
]

'''
Escirbir una funcion covertir() que dado un cuadrado en forma de
lista de listas lo devuelva el cuadrado en forma de diccionario
'''
def convertir(cuadrado):
    d = {}
    for fila in range(3):
        for elem in range(3):
            d[fila, elem] = cuadrado[fila][elem]
    return d


'''
Escribir una funcion que reciba un cuadrado/matriz y devuelva
True or False si es un cuadrado magico o no (hacer con diccionario
o lista)
'''
# hace tantas comprobaciones como filas haya, tantas como columnas haya
 # más las dos diagonales principales (suma)
 # y si todas dan los mismo devuelve true
def es_magico(cuadrado):
    for colum in range(3):
        res = 0
        for fila in range(3):
            res += cuadrado[colum, fila]
        if res != 15:
            return False

    for colum in range(3):
        res = 0
        for fila in range(3):
            res += cuadrado[fila, colum]
        if res != 15:
            return False

    res = 0
    for colum in range(3):
        res += cuadrado[colum, colum]
    if res != 15:
        return False

    for colum in range(2, -1, -1):
        res = 0
        for fila in range(3):
            res += cuadrado[fila, colum]
        if res != 15:
            return False
    return True
