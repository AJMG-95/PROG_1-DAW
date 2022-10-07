'''
El proceso que genera esta función recursiva es un proceso recursivo lineal, ya que el numero de pasos
para ejecutar la función es proporcional al tamaño de la entrada
'''
# Pre: n >= 0
#   count_digits(n: int) --> int
# Post:

digitos_rec = lambda n: digitos_rec(n // 10) + 1 if n > 10 else 1

'''
Proceso iterativo final, se le añade una contador

_n_ (n//10)    _acc_(acc+1)
2347             1
234              2
23               3
2                4

digitos_iter(n, acc)=
    acc, si n > 10
    digitos_iter(n // 10, acc + 1),  e.o.c.

digitos(n) = digitos_iter(n, 1)
'''
#
# Pre: n >= 0
#   digitos(n: int) --> int
# Post:

digitos = lambda n: digitos_iter(n, 1)
digitos_iter = lambda n, acc: acc if n < 10 else digitos_iter(n // 10, acc + 1)
