'''
Escribir una función quitar_digitos no recursiva usando funciones de orden superior que,
dada una cadena, la devuelva quitando todos los digitos que puedan aparecer en ella

# Pre: True
#   quitar_digitos(c: str) --> str
# Post: quitar_digitos(c) = c sin diigitos numerios
'''
# numeros = ''.join(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
# quitar_digitos = lambda c: ''.join(tuple(x for x in c if x not in numeros))

# quita_digito = lambda c: ''.join(tuple(filter(lambda c: aux_1, c)))
# aux_1 = lambda c: not c.isdigit()

quita_digito = lambda c: ''.join(tuple(filter(lambda c: not c.isdigit(), c)))

'''
Escribir una función recursiva quitar_digitos que, dada una cadena, la devuelva quitando
todos los digitos que puedan aparecer en ella:

# Pre: True
#   quitar_digitos(c: str) --> str
# Post: quitar_digitos(c) = c sin caracteres numericos
'''
# digito = lambda c: c[0] if c[0].isalpha() else ''
# quitar_digitos = lambda c: '' if c == '' else digito(c[0]) + quitar_digitos(c[1:])

quitar_digitos = lambda c: \
    '' if c == '' else \
        (c[0] if c[0].isalpha() else '') + quitar_digitos(c[1:])


'''
Escribir una función quitar_digitos no recursiva usando expresiones
generadoras que, dada una cadena, la devuelva quitando todos los dígitos
que puedan aparecer en ella:
'''
digitos = '0123456789'
quitar_digitos = lambda c: ''.join(tuple(x for x in c if x not in digitos))


'''
Escribir una función tomar_mientras que tenga el mismo comportamiento que la función
intertools.takewhile, pero devolviendo una tupla en lugar de un iterador:

    from itertools import takewhile
    tuple(takewhile(lambda x: x < 5, (1, 4, 6, 4, 1))) => (1, 4)

Naturalmente no se puede usar la función intertools.takewhile


# Pre: x > 0
#   tomar_mientras(x: lambda x: x < int, t: tuple) --> tuple
# Pro: tomar_mientras(x) = Recorre la tupla x hasta que encuentra una valor > x y devueve una tupla
        con los valores anteriores al valor > x
'''
tomar_mientras = lambda x, t: aux_2(x, t, ())
aux_2 = lambda x, t, acc: acc if t == () else \
    aux_2(x, t[1:], acc + (t[0],)) if x(t[0],) else acc


tomar_mientras2 = lambda f, t: () if t == () or not f(t[0]) else\
    (t[0],) + tomar_mientras2(f, t[1:])


'''
Escribir una función dejar_mientras que tenga el mismo comportamiento que la fucnión
intertools.dropwhile, pero devolviendo una tupla en lugar de un iterador:

    from itertools import dropwhile
    tuple(dropwhile(lambda x: x < 5, (1, 4, 6, 4, 1))) => (6, 4, 1)

# Pre: x > 0
#   dejar_mientras(x: lambda x: x < int, t: tuple) --> tupla
# Post: dejar_mientras(x) = Recorre la tupla x hasta que encuentra una valor > x y devueve una tupla
        con los valores posteriores incluyendo el valor > x
'''

dejar_mientras = lambda x, t: () if tuple(t) == () else \
    dejar_mientras(x, t[1:]) if x(t[0],) else t


'''
Escribe una función inversa que devuelva la inversa de una tupla de forma que:

    inversa((1, 2, 3, 4)) => (4, 3, 2, 1)

No se puede usar la función predefinida reversed ni ninguna construcción sintactica que
no se haya visto hasta la unidad 4(incluyendo slices)

Pre: True
    inversa(t: tuple) --> tuple
Post: inversa(t) = tupla t(n1...ni) con el orden invertido --> t(ni...n1)
'''

inversa = lambda t: () if t == () else \
    inversa(t[1:]) + (t[0],)


inversa2 = lambda t: inver(t, ())
inver = lambda t, acc: acc if t == () else \
    inver(t[1:], (t[0],) + acc)

def inversa3 (t):
    res = ()
    for e in t:
        res = (e,) + res
    return res

t = (1, 4, 6, 4, 1)
tuple(reversed(t))
t[::-1]
