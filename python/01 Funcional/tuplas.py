'''
Calcular la longitud (nº de elementos) que tiene una tumpla,
    funcion recursiva que genera un prodceso recursivo lineal

# Pre: True
#   long_tupla_rec(n: tupla) --> int
# Post: long_tupla_rec(t)= len(t)
'''
long_tupla_rec = lambda t: 0 if t == () else 1 + long_tupla_rec(t[1:])

'''
Calcular la longitud (nº de elementos) que tiene una tumpla,
    funcion recursiva que genera un prodceso iterativo

# Pre: True
#   long_tupla(n: tupla) --> int
# Post: long_tupla(t)= len(t)
'''
long_tupla = lambda t: long_tupla_iter (t, 0)
long_tupla_iter = lambda t, acc: acc if t == () else long_tupla_iter(t[1:], acc + 1)


'''
Suma los valores de una tupla compuesta unicamente por datos de tipo int y float
    Funcion recursiva que genera un proceso recursivo lineal
# Pre: t:(int or float)
#   suma_tupla(t: tupla) --> number
# Post: suma_tupla(t)= sum(t)
'''
suma_tupla_rec = lambda t: 0 if  t == () else t[0] + suma_tupla_rec(t[1:])

'''
Suma los valores de una tupla compuesta unicamente por datos de tipo int y float
    Funcion recursiva que genera un proceso iterativo
# Pre: t:(int or float)
#   suma_tupla(t: tupla) --> number
# Post: suma_tupla(t)= sum(t)
'''

suma_tupla = lambda t: suma_tupla_iter (t, 0)
suma_tupla_iter = lambda t, acc: acc if t == () else suma_tupla_iter(t[1:], acc + t[0])
