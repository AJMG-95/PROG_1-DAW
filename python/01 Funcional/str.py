'''Determina si una cadena c tiene una longitud n'''
# Pre: True
#         long_str(cadena: str, num: int) --> bool
# Post: long_str(cadena, num) =
#   - True si cadena tiene num caracteres
#   - Fale en caso contrario

long_str = lambda c, n: len(c) == n

'''
Calcular la longitud de una cadena con una función recursiva, que genera un proceso recursivo lineal
    longitud(c)=
        0, Sí c == ''  --> Caso base
        1 + longitud(c[1:]), --> e.o.c.
'''
# Pre: True
#   longitud(c: str) --> int
# Post: longitud(c) = len(c)

longitud_rec = lambda c: 0 if c == '' else 1 + longitud_rec(c[1:])

'''
Calcular la longitud de una cadena con una función recursiva, que genera un proceso iterativo lineal
    longitud(c)=
        0, Sí c == ''  --> Caso base
        long_iter(c[1:], acc + 1), --> e.o.c.
'''
longitud = lambda c: long_iter (c, 0)
long_iter = lambda c, acc: acc if c == '' else long_iter(c[1:], acc + 1)

'''
Filtrar una cadena de forma que devuelva la misma cadena pero sin mayusculas.
    Con un unico caso recursivo y un caso base



# Pre: True
#   filtra_mayus (c: str) --> str
# Post: filtra_mayus(c) --> la cadena c original pero habiendo quitado las mayusculas.
'''

filtra_mayus = lambda c: '' if c == '' else\
                        ('' if c[0].isupper() else c[0]) + filtra_mayus(c[1:])

'''
Filtrar una cadena de forma que devuelva la misma cadena pero sin mayusculas.
    Con dos casos recursivo y un caso base

{ '' si c == ''
{ f(c[1:]) si c[0] es mayuscula
{ c[0] + f(c[1:]) si c[] es minuscula

# Pre: True
#   filtra_mayus (c: str) --> str
# Post: filtra_mayus(c) --> la cadena c original pero habiendo quitado las mayusculas.
'''
filtra_mayus2 = lambda c: '' if c == '' else \
                        filtra_mayus2(c[1:]) if c[0].isupper() else \
                        c[0] + filtra_mayus2(c[1:])

'''
Filtra_mayus3, se apoya en la función quita_mayus, hace lo mismo que la función original
pero la expresión de la misma es más semcilla ya que la comprovación de las mayusculas
la hace quita_mayus

# Pre: True
#   filtra_mayus (c: str) --> str
# Post: filtra_mayus(c) --> la cadena c original pero habiendo quitado las mayusculas.
'''
quita_si_mayus = lambda c: '' if c.isupper() else c
filtra_mayus3 = lambda c: '' if c == '' else\
                        quita_si_mayus(c[0]) + filtra_mayus(c[1:])
