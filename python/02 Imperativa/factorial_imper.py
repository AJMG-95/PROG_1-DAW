fact = lambda n: 1 if n == 0 else n * fact(n - 1)
num = input('Introduce un numero: ')
res = fact(int(num))
print('El factorial de ', num, 'es', res)
