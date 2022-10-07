'''
Cuantas vocales (a, e, i, o, u) contienen una cadena
Pre: Una sola palabra y sin numeros
'''

# def is_vowel (c):
#    return
#    c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
#    c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
'''---------'''

# def is_vowel(c):
#     return c.lower() in 'aeiou'

# def count_vowels(txt):
#     res = 0
#     i = 0
#     while i < len(txt):
#         if is_vowel(txt[i]):
#             res += 1
#     i += 1
#     return res
'''
# def count_vowels(txt):
#     def is_vowel(c):
#         return c.lower() in 'aeiou'
#     res = 0
#     i = 0
#     while i < len(txt):
#         if is_vowel(txt[i]):
#             res += 1
#         i += 1
#     return res
'''
'''
De la siguiente forma no es posile extraer la función is_vowel ya que depende de que en el entorno
existan las variables txt y lavariable i, por ello es preferible la función anterior, porque sí
se puede extraer la función is_vowel fuera de la funcion principal
'''

def count_vowels(txt):
    def is_vowel():
        return txt[i].lower() in 'aeiou'
    res = 0
    i = 0
    while i < len(txt):
        if is_vowel():
            res += 1
        i += 1
    return res

'''-------'''
def is_vowel(c):
    return c.lower() in 'aeiou'

def count_vowel(txt):
    return sum(1 for c in txt if is_vowel(c))

'''
# Expresión Generadora #

def count_vowel(txt):
    return sum(1 for c in txt if c.lower() in 'aeiou')
'''

'''
# Recursiba #

def count_vowel(txt):
    if txt == '':
        rerturn 0
    else:
        if txt[0].lower() in 'aeiou':
            return 1 + count_vowel(txt[1:])
        else:
            return count_vowel(txt[1:])
'''
'''
# Recursiba 2#

def count_vowel(txt):
    if txt == '':
        rerturn 0
    else:
        if txt[0].lower() in 'aeiou':
            res = 1
        else:
            res = 0
        return res + count_vowel(txt[1:])
'''
'''
# Recursiba 3 #

def count_vowel(txt):
    if txt == '':
        rerturn 0
    else:
        res = 1 if txt[0].lower() in 'aeiou' else 0
        return res + count_vowel(txt[1:])
'''
'''
# Recursiba 4 #

# es igual que la 2 pero el else es inecesario y se puede quitar, ya que si se cumple la
# condicion devuelve 0 y se sale de la funcion pero si no se cumple sigue leyendo
# el cuerpo de la fucion y entra en el segundo if

def count_vowel(txt):
    if txt == '':
        rerturn 0

    if txt[0].lower() in 'aeiou':
        res = 1
    else:
        res = 0
    return res + count_vowel(txt[1:])
'''
