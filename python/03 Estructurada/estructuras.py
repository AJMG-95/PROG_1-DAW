'''
Ejemplo de una estructura de control condicional mediante el uso de:
- if
- elif
- else

Este bloque compara dos numeros introducidos por el usuario y dice cual de los dos es mayor
'''

a = int(input('Introduce el primer numero: '))
b = int(input('Introduce el segundo numero: '))
if a > b:
    print('El primer numero es mayor que el segundo')
elif a == b:
    print('Los dos numeros on iguales')
else:
    print('El segundo nuemero es mayor al primero')

'''
Ejemplo de una estructura de control iterartiva, mediante un bucle "while ___:"
Su funcion es imprimir por pantalla todos los nuemros del 0 al 4.
Esta estructura contiene 3 estructuras y 4 sentencias simples.
'''
# En este caso la x es un contador que vale para que el blucle sepa cuando ha de parar
x = 0
while x < 5:
    print (x)
    x += 1
print ('Fin')

# En este caso la x es un interruptor, ya que es su valor, el cual es unico, el que fuerza que se
#  detenga el bucle
salida = False
while not salida:
    x = input('Introduce un numero: ')
    if x == '2':
        salida = True
    print(x)

'''
Escribir un programa que calcule la suma de los elementos de una LISTA usando
un bucle
'''
LISTA = [7, 8, 4, 5, 1, 2, 9, 6, 3]
'''
# Versión facil:
suma_l = sum(LISTA)
print('La suma es: ', suma_l)
'''

# Bucle:
suma = 0    # Suma es un acumulador que guarda el valor de la suma
i = 0       # Es un contador para garantizar que se recorre la LISTA completa
while i < len(LISTA):
    suma += LISTA[i]
    i += 1
print('La suma es: ', suma)
