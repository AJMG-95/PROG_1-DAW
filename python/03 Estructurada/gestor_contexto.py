'''
try:
    f = open('suma.txt', 'r+')
    a = int(f.readline().rstrip())
    b = int(f.readline().rstrip())
    f.write('La suma de ', + str(a) +, ' y ', + str(b) +, ' es ', + str(a))
finally:
    f.close()
'''

with open('suma.txt', 'r+') as f:
    f = open('suma.txt', 'r+')
    a = int(f.readline().rstrip())
    b = int(f.readline().rstrip())
    f.write('La suma de ', + str(a) +, ' y ', + str(b) +, ' es ', + str(a))

# Esto es un gestor de contexto y sirve para liberar recursos externos del programa una vez
#  se han usado
