'''
Funcion suma que suma n numeros mediante un proceso recursivo lineal
'''
suma_n_rec = lambda n: 0 if n == 0 else n + suma_n_rec(n - 1)

'''
Funcion suma que suma n numeros mediante un proceso iteravo
_n_(n-1)    _acc_(acc+n)
 4            0
 3            4
 2            7
 1            9
 0           10

suma = lambda n: suma_iter(n, 0)
Suma_iter = lambda n, acc:
        acc, Sí n == 0
        suma_iter(n - 1, acc + n)
'''
suma_n = lambda n: suma_iter(n, 0)
suma_iter = lambda n, acc: acc if n == 0 else suma_iter(n - 1, acc + n)
