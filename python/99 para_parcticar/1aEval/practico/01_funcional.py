'''1
    Escribir una función dejar_mientras que tenga el mismo comportamiento que
    la función itertools.dropwhile, pero devolviendo una tupla en lugar de un
    iterador:

    from itertools import dropwhile
    tuple(dropwhile(lambda x: x < 5, (1, 4, 6, 4, 1))) => (6, 4, 1)

    Naturalmente, no se puede usar la función itertools.dropwhile.

        Test:
        >>> print(dejar_mientras(lambda x: x < 5 (1, 4, 6, 4, 1)))
        (6, 4, 1)
        >>> print(dejar_mientras(lambda x: True, (1, 2, 3, 4, 5)))
        ()
'''
dejar_mientras = lambda f, t: () if t == () else\
    dejar_mientras(f, t[1:]) if f(t[0]) else t

'''2
    Escribir una función inversa que devuelva la inversa de una tupla,
    de forma que:

    inversa((1, 2, 3, 4)) => (4, 3, 2, 1)

    No se puede usar la función predefinida reversed ni ninguna construcción
    sintáctica que no se haya visto hasta la UD4 (incluyendo slices).

        Test:
        >>> print(inversa((1, 2, 3, 4)))
        (4, 3, 2, 1)
        >>> print(inversa((9, 14, 5)))
        (5, 14, 9)
'''
inversa = lambda t: aux(t, ())
aux = lambda t, acc: acc if t == () else\
    aux(t[1:], (t[0],) + acc)

'''3
    Escribir una función quitar_digitos no recursiva usando expresiones
    generadoras que, dada una cadena, la devuelva quitando todos los dígitos
    que puedan aparecer en ella:

    quitar_digitos("hkj23hk234kj1h24kj") => "hkjhkkjhkj"

        Test:
        >>> print(quitar_digitos("hkj23hk234kj1h24kj"))
        hkjhkkjhkj
        >>> print(quitar_digitos("abc"))
        abc
'''
digitos = '0123456789'
quitar_digitos = lambda c: ''.join(tuple(x for x in c if x not in digitos))

'''4
    Escribir una función quitar_digitos no recursiva usando funciones
    de orden superior que, dada una cadena, la devuelva quitando todos
    los dígitos que puedan aparecer en ella:

    quitar_digitos("hkj23hk234kj1h24kj") => "hkjhkkjhkj"

        Test:
        >>> print(quitar_digitos("hkj23hk234kj1h24kj"))
        hkjhkkjhkj
        >>> print(quitar_digitos("abc"))
        abc
'''
quitar_digitos = lambda c: ''.join(tuple(filter(lambda c: not c.isdigit(), c)))

'''5
    Escribir una función recursiva quitar_digitos que, dada una cadena,
    la devuelva quitando todos los dígitos que puedan aparecer en ella:

    quitar_digitos("hkj23hk234kj1h24kj") => "hkjhkkjhkj"

        Test:
        >>> print(quitar_digitos("hkj23hk234kj1h24kj"))
        hkjhkkjhkj
        >>> print(quitar_digitos("abc"))
        abc
'''
quitar_digitos = lambda c: \
    '' if c == '' else \
        (c[0] if c[0].isalpha() else '') + quitar_digitos(c[1:])

'''5
    Escribir una función tomar_mientras que tenga el mismo comportamiento
    que la función itertools.takewhile, pero devolviendo una tupla en
    lugar de un iterador:

    from itertools import takewhile
    tuple(takewhile(lambda x: x < 5, (1, 4, 6, 4, 1))) => (1, 4)

    Naturalmente, no se puede usar la función itertools.takewhile.

        Test:
        >>> print(tomar_mientras(lambda x: x < 5, (1, 4, 6, 4, 1)))
        (1, 4)
        >>> print(tomar_mientras(lambda x: True, (1, 2, 3, 4, 5)))
        (1, 2, 3, 4, 5)
'''
tomar_mientras = lambda f, t: () if t == () or not f(t[0]) else\
    (t[0],) + tomar_mientras(f, t[1:])
