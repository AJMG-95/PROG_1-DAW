'''
Ecribir una fucnión recursiva que rsuelva las Torres de Hanoi
    Devuelve una str que indica los movimientos que se han de hacer para resolver el prblema
'''
# Pre: a: str, b: str, c: str, n >= 0
#   hanoi(a, b, c, n: int) --> str
# Post: hanoi(a, b, c, n) = Es la cadena que descriobe los movimientos que se han de hacer para
#                           reolver el hanoi del pivote a al pivote c con n discos.
'''
a --> inicio
b --> apoyo
c --> fin

_a_     _b_     _c_

hanoi(1, 2, 3, 4) = hanoi(1, 3, 2, 3) + 'muevo el disco del pivote 1 al pivote 3 + hanoi(2, 1, 3, 3)
hanoi(a, b, c, n) = \
            hanoi(a, c, b, n - 1) + 'muevo el disco del pivote 1 al pivote 3 + hanoi(b, a, c, n -1)

caso base       --> hanoi(a, b, c, n) = ''    Sí n = 0
caso recursivo  --> hanoi(a, b, c, n) = \
            hanoi(a, c, b, n - 1) + 'muevo el disco del pivote 1 al pivote 3 + hanoi(b, a, c, n -1)
'''
hanoi = \
    lambda a, b, c, n: '' if n == 0 else \
        hanoi(a, c, b, n - 1) + \
        ' --> Mover un disco del ' + a + ' al ' + c + \
        hanoi(b, a, c, n - 1)

contar_hanoi = lambda n: (2 ** n) - 1
