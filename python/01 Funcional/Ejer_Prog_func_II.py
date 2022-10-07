'''
1. Dada la siguiente función matemática:

f(n) =
    0                   Sí n = 0
    1 + 2 * f(n - 1)    Sí n > 0

Calcula el valor de f(3)
'''
f = lambda n: 0 if n == 0 else n + f(n -1)

'''
2. La función potencia tiene la siguiente especificación:
'''
# Pre: b >= 0
#   potencia(a: int, b: int) --> int
# Post: potencia(a, b) = a^b
'''
    a) Implementa una función no recursiva
    b) Implementa una funcion recursiva
'''
potencia = lambda a, b: a ** b

potencia_2 = lambda a, b: potencia_rec(a, b, 1)
potencia_rec = lambda a, b, acc: acc if b == 0 else potencia_rec(a, b - 1, a * acc)

'''
3. La función repite tiene la siguiente especificación:
'''
# Pre n >= 0
#   repite(s: str, n: int) --> str
# Post:repite(s, n) = s * n
'''
Implementar la fucnión de forma recursiva
'''
repite = lambda s, n: s if n == 1 else s + ' ' + repite(s, n - 1)

'''
4. La suma lenta es un algoritmo para sumar dos números para el que sólo necesitamos
saber cuáles son el anterior y el siguiente de un número dado. El algoritmo se basa en
la siguiente recurrencia:

suma_lenta (a, b) =
    b                           Sí a = 0
    suma_lenta(ant(a), sig(b))  Sí a > 0

Suponiendo que tenemos las siguientes funciones ant y s

ant = lambda n: n - 1
sig = lambda n: n + 1

Se pide:
    a) Escribir su especicación.
    b) Implementar una función recursiva que satisfaga dicha especificación
'''
# Pre: a >= 0
#   suma_lenta(a: int, b: numeric) --> numeric
# Post: suma_lenta (a, b) = a + b

ant = lambda n: n - 1
sig = lambda n: n + 1

suma_lenta = lambda a, b: b if a == 0 else suma_lenta(ant(a), sig(b))

'''
5. La función suma_digitos calcula la suma de los dígitos de un número entero:

suma_digitos(423) = 4 + 2 + 3 = 9
suma_digitos(7) = 7

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Recordar que n // 10 le quita el último dígito a n. Además, n % 10 devuelve
el último dígito de n
'''
# Pre: 0 < n: int
#   suma_digitos (n: int) --> int
# Post: suma_digitos(n) = Sumatorio de los digitos de n

suma_digitos = lambda n: s_d(n, 0)
s_d = lambda n, acc: acc if n == 0 else s_d(n // 10, acc + n % 10)

'''
6. La función voltea le da la vuelta a un número entero:

voltea(423) = 324
voltea(7) = 7

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
entero. Usar además la indicación del ejercicio anterior.

>> Para unafincion recursiva <<
digitos = lambda n: len(str(n))

voltear(n)
    Caso Base -->       n,  Sí n < 10
    Caso recursivo -->  voltea((n % 10)*(10 ** (digitos - 1)) + n // 10)
'''

voltear = lambda n: int(str(n[::-1]))

'''
7. La función par_positivo determina si un número entero positivo es par:

par_positivo(0) = True
par_positivo(1) = False
par_positivo(27) = False
par_positivo(82) = True

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificacion

'''

# par_positivo = lambda n: n % 2 == 0

par_positivo = lambda n: pv(n, True)
pv = lambda n, acc: acc if n % 2 == 0 else pv(n - 1, False)
'''
8. La función par determina si un número entero (positivo o negativo) es par:

par(0) = True
par(1) = False
par(-27) = False

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.
    c) ¿Cómo se podría implementar una función impar a partir de la función par?
'''
par = lambda n: pv(n, True)
pv = lambda n, acc: acc if n % 2 == 0 else pv(n - 1, False)

impar = lambda n: not par(n)

'''
9. La función elem tiene la siguiente especificación:
'''
# Pre: True
#   elem(e, t: tupla) --> bool
# Post: elem(e, t) =
#                    True   Sí e está en t
#                    False  en caso contrario
'''
Escribir una función recursiva que satisfaga dicha especificació
'''
elem = lambda e, t: False if e == t[0] and () else elem(t[1:])

'''
10. La función cuantos tiene la siguiente especificación
'''
# Pre: True
#   cuantos(e, t: tuple) --> int
# Post: cuantos(e, t) = el número de veces que aparece e en t
'''
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
    a) recursivo.
    b) iterativo.
'''
# Version que genera un proceso recursivo
cuantos_rec = lambda e, t: 0 if t == () else \
    1 + cuantos_rec(e, t[1:]) if e == t[0] else \
    0 + cuantos_rec(e, t[1:])

# Version que genera un proceso iterativo
cuantos = lambda e, t: cuan_iter(e, t, 0)
cuan_iter = lambda e, t, acc: acc if t == () else \
    cuan_iter(e, t[1:], acc + 1 if e == t[0] else acc)


'''
11. La función quita tiene la siguiente especificación
'''
# Pre: True
#   quita(e, t: tuple) --> tuple
# Post: quita(e, t) = una tupla igual que t pero sin los e
'''
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:

a) recursivo.
b) iterativo.
'''
# Version que genera un proceso recursivo
#quita = lambda e, t: () if t == () else quita(t[1:]) if e == t[0] else quita(tuple(t[0]) + t[1:])

# Version que genera un proceso iterativo


'''
12. La función sustituye tiene la siguiente especificación:
'''
# Pre: True
#   sustituye(a, b, t: tuple) --> tuple
# Post: sistituye(a, b, t) = una tupla igual a t pero sustituyendo los a por b
'''
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.
'''



'''
13. La función ultimo tiene la siguiente especificación
'''
# Pre: t != ()
#   ultimo(t: tuple)
# Post: ultimo(t) = el último elemento de t
'''
Escribir una función recursiva que satisfaga dicha especificacion
'''



'''
14. La función enesimo tiene la siguiente especificación
'''
# Pre : t != () and 0 <= n < len(t)
#   enesimo (n: int, t: tuple)
# Post: enesimo(n, t) = el n-ésimo elemento de t
'''
Escribir una función recursiva que satisfaga dicha especificación
'''


'''
15. Una funcion invertir_t que invierta el orden de los elementos de una tupla y que:
    a) genere un proceso recursivo
    b) genere un proceso iterativo
    c) usando la función reduce de functools
'''

invertir_tupla = lambda t: () if t == () else invertir_tupla(t[1:]) + (t[0],)

inver_t = lambda t: inver_iter(t, ())
inver_iter = lambda t, acc: acc if t == () else \
    inver_iter(t[1:], (t[0],) + acc)

from functools import reduce
inv_reduce = \
        lambda t: reduce(lambda acc, x: (x,) + acc, t, ())
