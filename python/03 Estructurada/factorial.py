"""Formas de calcular el factorial de un número
"""
def fact(n):
    """Calcula el factorial de un número


    Args:
        n (int): Número al que se le calcula el factorial
    """
    def fact_iter(acc, m):
        """Función auxiliar para el cálculo del factorial

        Args:
            acc (int): Acumulador
            m (int): n - 1 hasta llegar valor de caso vase 0

        Returns:
            int: Resultado del fact(n)

            >>> fact(5)
            120
            >>> fact(4)
            24
        """
        if m == 0:
            return acc
        acc *= m
        m -= 1
        return fact_iter(acc, m)
    return fact_iter(1, n)


def fact2(n):
    """[summary]

    Args:
        n ([type]): [description]
    """
    def fact_iter(acc):
        """[summary]

        Args:
            acc ([type]): [description]

        Returns:
            [type]: [description]
        """
        nonlocal n
        if n == 0:
            return acc
        acc *= n
        n -= 1
        return fact_iter(acc)
    return fact_iter(1)
