'''Versión que genera un proceso recursivo en arbol'''
# Pre: n >= 0
#       fib(n: int) --> int
# Post: fib(n) = el n-ésimo termino de la sucesión de Fibonacci
#   Casos Base:
#       0   si  n = 0
#       1   si  n=1
#   Caso Recursivo: fib(n - 1) + fib(n - 2)       Sí      n > 1

fib_rec = lambda n: 0 if n == 0 else 1 if n == 1 else fib(n - 1) + fib(n - 2)

'''Versión que genera un proceso iterativo'''
#   _n_ _a_ _b_
#   4   0   1
#   3   1   1
#   2   1   2
#   1   2   3
#   0   3   5

# fib_iter(n , a, b) =
#     a   sí n = 0
#     fib_iter(n - 1, b, a + b)
# fib(n)=fib_iter(n, 0, 1)

fib = lambda n: fib_iter(n, 0, 1)
fib_iter = lambda n, a, b: a if n == 0 else fib_iter(n - 1, b, a + b)
