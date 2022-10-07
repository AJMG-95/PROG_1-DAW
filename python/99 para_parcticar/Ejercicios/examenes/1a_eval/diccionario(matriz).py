"""
Ejercicio 2 examen 2021-2022
"""

m1 = {(0, 0): 11, (0, 1): 2, (0, 2): 4,
      (1, 0):  4, (1, 1): 5, (1, 2): 6,
      (2, 0): 10, (2, 1): 8, (2, 2): -12}


m2 = {(0, 0): 11, (0, 1): 2, (0, 2): 9,
      (1, 0):  4, (1, 1): 5, (1, 2): 6,
      (2, 0): 10, (2, 1): 8, (2, 2): -12}


def diferencia_diagonales1(matriz):
    """Toma una matriz cuadrada y devuelve la suma de sus dos diagonales.

    Args:
        matriz (dic): Matriz que recibe la fución como argumento.

    Returns:
        int: Valor absoluto de la diferencia entre diagonales.
    """
    """Docstring:
    n1 = {(0, 0): 11, (0, 1): 2,(0, 2): 4,
          (1, 0): 4, (1, 1): 5, (1, 2): 6,
          (2, 0): 10, (2, 1): 8, (2, 2): -12}

    n2 = {(0, 0): 11, (0, 1): 2,(0, 2): 9,
          (1, 0): 4, (1, 1): 5, (1, 2): 6,
          (2, 0): 10, (2, 1): 8, (2, 2): -12}

    >>> print(diferencia_diagonales(n1))
        15
    >>> print(diferencia_diagonales(n2))
        12

    Args:
        matriz (dic): Matriz  en forma de dicionaro con claves en forma de tupla de enteros y valores enteros.
                    {(n , m): x, ...}

    Returns:
        int: Valor absoluto de la diferencia de las sumas de los valores de la diagonal principal y la secundaria.
    """
    ma = max(matriz)[0]
    suma_principal = 0
    suma_secundaria = 0
    for i in range(ma + 1):
        suma_principal += matriz[i, i]
    fila, col = 0, ma
    while col >= 0:
        suma_secundaria += matriz[fila, col]
        fila += 1
        col -= 1
    return abs(suma_principal - suma_secundaria)

def diferencia_diagonales2(matriz):
    """Toma una matriz cuadrada y devuelve la suma de sus dos diagonales.

    Args:
        matriz (dic): Matriz que recibe la fución como argumento.

    Returns:
        int: Valor absoluto de la diferencia entre diagonales.
    """
    suma_principal = sum(matriz[k] for k in matriz if k[0] == k[1])
    ma = max(matriz)[0]
    suma_secundaria = sum(matriz[k] for k in matriz if k[0] + k[1] == ma)
    return abs(suma_principal - suma_secundaria)
