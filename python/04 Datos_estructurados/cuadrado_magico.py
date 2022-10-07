"""Script que comprueba si un cuadrado es mágico.
"""
from itertools import chain

def elementos_diferentes(matriz):
    numeros = list(chain(*matriz))

    return len(set(numeros)) == len(numeros)


def es_cuadrado_magico(matriz):
    """En primer lugar, comprobar que tiene el mismo número de filas y
    de columnas.
    """
    if len(matriz[0]) == len(matriz):
    # Ahora comprobaremos que todos los números son diferentes.
        if elementos_diferentes(matriz):
            suma_fila1 = sum(matriz[0])

            # Comprueba las filas
            for i in range(1, len(matriz)):
                if suma_fila1 != sum(matriz[i]):
                    return False

            # Comprueba las columnas
            for j in range(len(matriz)):
                suma_columnas = sum([matriz[i][j] for i in range(len(matriz))])

                if suma_fila1 != suma_columnas:
                    return False

            # Comprueba las diagonales
            suma_diagonal_principal = sum([matriz[i][i] for i in range(len(matriz))])

            if suma_fila1 != suma_diagonal_principal:
                return False

            columnas = len(matriz[0]) - 1
            suma_diagonal_secundaria = 0

            for i, e in enumerate(matriz):
                suma_diagonal_secundaria += e[columnas - i]

            return suma_fila1 == suma_diagonal_secundaria

        else:
            return False
    else:
        return False

cuadrado = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

resultado = es_cuadrado_magico(cuadrado)
print(resultado)
