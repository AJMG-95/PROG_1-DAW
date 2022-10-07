"""
def pareja(x, y):
    def select(indice):
        return x if indice == 0 else y

    dic = {'select': select}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho
"""

# Se plantea el acceder al numerador y al denominador de forma
# independiente, con lo que en lugar de haber una unaca función
# que use una condicion para acceder a ellos, usar dos funcones
# independientes una para cada uno
"""
def pareja(x, y):
    def primero():
        return x

    def segundo():
        return y

    dic = {'primero': primero, 'segundo': segundo}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho

def racional(n, d):
    p = pareja(n, d)

    def numer():
        return p('primero')()

    def denom():
        return p('segundo')()

    dic = {'numer': numer, 'denom': denom}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho

def mul(r1, r2):
    return racional(r1('numer')() * r2('numer')(),
                    r1('denom')() * r2('denom')())

def imprimir(r):
    print(r('numer')(), '/', r('denom')(), sep='')
"""

#! Racionales Mutables


def pareja(x, y):
    def primero():
        return x

    def segundo():
        return y

    def set_primero(nuevo_x):
        nonlocal x
        x = nuevo_x

    def set_segundo(nuevo_y):
        nonlocal y
        y = nuevo_y

    dic = {'primero': primero,
           'segundo': segundo,
           'set_primero': set_primero,
           'set_segundo': set_segundo}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho


def racional(n, d):
    p = pareja(n, d)

    def numer():
        return p('primero')()

    def denom():
        return p('segundo')()

    def set_numer(nuevo_numer):  # No usa nonlical porque no modifica p sino su estado interno
        p('set_primero')(nuevo_numer)

    def set_denom(nuevo_denom):
        p('set_segundo')(nuevo_denom)

    dic = {'numer': numer,
           'denom': denom,
           'set_numer': set_numer,
           'set_denom': set_denom}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho


def mul(r1, r2):
    return racional(r1('numer')() * r2('numer')(),
                    r1('denom')() * r2('denom')())


def imprimir(r):
    print(r('numer')(), '/', r('denom')(), sep='')
