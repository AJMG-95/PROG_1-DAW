"""Examen 2019

Returns:
    int: 10/10
"""

'''
Convertir un diccionario en una lista y viceversa
'''
def dic2list(dic):
    """convierte un diccionario en una lista

    Args:
        dic (dict): Es un diccionario

    Returns:
        list: Lista con los valores del diccionario
    """
    res = []
    for i in range(0, max(dic) + 1):
        res.append(dic.get(i))
    return res


def list2dic(lst):
    dic = {}
    for i, e in enumerate(lst):
        dic[i] = e
    return dic


'''
m sobre n
'''
def sobre(m, n):
    """Calcula m sobre n

    Args:
        m ([type]): [description]
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    if m == 0 and n > 0:
        return 0
    if m >= 0 and n == 0:
        return 1
    return sobre(m - 1, n - 1) + sobre(m - 1, n)


'''
lista sobre a
'''
def lista_sobre_A(ultima_fila):
    """Devuelve una lista de listas que de un numero sobre otro

    Args:
        ultima_fila (int): Indice de la última fila

    Returns:
        list: Lista de listas de enteros que componen el triangulo

    >>> lista_sobre_A(2)
    [[1], [1, 1], [1, 2, 1]]
    """
    if ultima_fila == 0:
        return [[1]]
    triangulo = lista_sobre_A(ultima_fila - 1)
    ultima = triangulo[-1]
    copia = ultima
    ultima = [0] + ultima
    copia = copia + [0]
    nueva = list(map(lambda a, b: a + b, ultima, copia))
    #! from operator import add   map(add, ultima, copia)
    # a + b for a, b in zip (ultima, copia)
    #* suma = []
    #* for a, b in zip(x, y):
        #* suma.append(a + b)
    triangulo.append(nueva)
    return triangulo

'''
piramides de 1
     1
    1  1
   1  2  1
1   3  3   1
'''
#cada vez que calculouna fila la duolico le pongo un cero delante y otro por detras

'''
x = 0 fila 1
y = fila 2 0
z = x + y
'''

def triangulo(num_filas):
    triangulo = lista_sobre_A(num_filas - 1)
    for fila in triangulo:
        res = ''
        for e in fila:
            res += f'{e:6}'
    print(res.center(50).rstrip())
