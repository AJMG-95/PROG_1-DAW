from typing import AsyncContextManager


'''Versión que genera un proceso recursivo lineal'''
fact_rec =  lambda n: n * fact(n - 1) if n > 0 else 1

'''Versión que genera un proceso recusivo iterativo lineal'''
# Pre: n > 0
#   fact_iter(n: int, acc: int) =
#      fact_iter(n - 1, acc * n)
#       Acc     n = 0
# --> int
# Post:

fact = lambda n: fact_iter(n, 1)
fact_iter = lambda n, acc: acc if n == 0  else fact_iter(n - 1, acc + n)
