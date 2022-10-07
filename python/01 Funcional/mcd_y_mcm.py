'''
1º Calcular Maximo comun divisor

max_com_div(a, b)
    a  Sí  a == b
    b  Sí  a > b and a % b == 0
    max_com_div(b, a % b)
'''

# Pre: a > 0 y b > 0
#   max_com_div(a: numeric, b: numeric) --> numeric
# Post: max_com_div(a, b) = máximo común divisor entre a y b


max_com_div = lambda a, b: a if a == b else \
                                b if a > b and a % b == 0 else \
                                max_com_div(b, a % b)

# Version de Ricardo:
mcd = lambda a, b: b if a % b == 0 else mcd(b, a % b)

'''
2º Calcular Minimo comun multiplo

mcm = (a * b) / mcd
'''
# Pre: a > 0 y b > 0
#   min_com_mul(a: numeric, b: numeric) --> numeric
# Post: min_com_mul(a, b) = minimo común multiplo entre a y b

min_com_mul = lambda a, b: (a * b) / max_com_div(a, b)
