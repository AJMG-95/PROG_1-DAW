'''
1. Encontrar el valor de la variable valor después de la ejecución de las
siguientes sentencias:
a) valor = 4.0 * 5
b) x = 3.0
   y = 2.0
   valor = x ** y - y
c) valor = 5
   x = 3
   valor = valor * x
'''
# A)
# valor = 20.0
# B)
# x = 3.0
# y = 2.0
# valor = 6
# c)
# valor = 5
# x = 3
# valor = 5 * 3
#   >> valor = 15

'''
2. ¿Cuál es la diferencia entre [1, 2, 3] y [[1, 2, 3]]?
'''
# El primero es una lista que contiene valores de tipo int
# El segundo es una lista que a su vez contiene a otra lista y esta lista
#  más interna continene valores de tipo int

'''
3. Explicar la diferencia entre el operador ternario:
〈valor〉 if 〈condición〉 else 〈valor〉
y la estructura de control:
if 〈condición〉:
〈sentencia〉
'''
# El () if () else (), es un operador ternario, que recibe una condicion y
#   dependiendo de si esta se cumple o no se ejecuta el valor True que se
#   indica antes del if o el valor False que se indica despues del else.
#   Y siempre es necesario incluir el else
#
# El if de estructura de control compruba si se cumple una condición y solo
#   entra en el cuerpo del if si se cumple la condición.
#   Y no siempre es necesario incluir un else.

'''
4. Escribir un programa que pida al usuario su edad y que imprima el mensaje
«¡Qué joven!» si es menor de 25 años.
'''

def edad_1(int):
    if int < 25:
        print('¡Qué joven!')


edad_01 = int(input('Indique su edad: '))
if edad_01 < 25:
    print('¡Qué joven!')

'''
5. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años y «¡Qué mayor!» en caso contrario
'''

def edad_2(int):
    if int < 25:
        print('¡Qué joven!')
    else:
        print('¡Qué viejo!')


edad_02 = int(input('Indique su edad: '))
if edad_02 < 25:
    print('¡Que joven!')
else:
    print('¡Que mayor!')

'''
6. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años y «No está mal.» si tiene entre 25 y 40 años.
'''

def edad_3(int):
    if int < 25:
        print('¡Qué joven!')
    elif 25 <= int < 40:
        print('No está mal')

'''
7. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años, «No está mal.» si tiene entre 25 y 40 años y «¡Qué
mayor!» si tiene más de 40 años.
'''

def edad_4(int):
    if int < 25:
        print('¡Qué joven!')
    elif 25 <= int < 40:
        print('No está mal')
    else:
        print('¡Que mayor!')

'''
8. Escribir un programa que muestre por pantalla la tabla de multiplicar de un
número comprendido entre 0 y 10, introducido por teclado.
'''

def tabla_multiplicar(numeric):
    i = 0
    res = 0
    while i < 11:
        res = numeric * i
        print(numeric, 'x', i, '=', res)
        i += 1

'''
9. Dado el siguiente código:
 n = int(input('¿Hasta dónde llego?: '))
 i = 0
 while i < n:
   print('Aquí la i vale', i)
   i += 2
se pide:
a) Contar cuántas sentencias hay.
b) Por cada una de ellas, indicar si son simples o compuestas.
c) Por cada sentencia compuesta, indicar de qué tipo de estructura se trata.
d) Deducir cuántas veces se ejecuta la sentencia de la línea 4 en función del valor de
la variable n.
e) ¿Es posible provocar un bucle infinito al ejecutar ese programa?
'''
# A) 4 simples y 1 compuesta
#       3 simles y 1 compuesta qie contiene 1 simple

# B) las 2 primeras lineas son simples, la dos siguientes
#       es un bucle while que es una sentencia compuesta que
#       contiene una simple y la ultima es una sentencia simple

# c) Estructura de comtrol de iteración (bucle while)

# D) Tantas veces como sean necesarias mientras i sea menor a n

# E) No

'''
10. Escribir un programa que calcule la media de cinco valores numéricos reales
(tipo float) introducidos por teclado.
'''

def media_5():
    print('Introduce 5 valores para calcular la media entre ellos')
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    x = int(input('Tercero número: '))
    n = int(input('Cuarto número: '))
    m = int(input('Último número: '))
    print(((a + b + x + n + m) / 5))


def media_501():
    print('Introduca 5 valores para calcular la media entre ellos')
    i = 1
    acc = 0
    while i <= 5:
        a = float(input('Introduzca un número: '))
        acc += a
        i += 1
    print(acc / 5)


'''
11. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
desde el último elemento hasta el primero.
'''

def iver_lista():
    lista = []
    while len(lista) < 10:
        entrada = input('Introduzca la cadena numero ' + str(len(lista)) + ': ')
        lista.append(entrada)

    i = len(lista) - 1
    while i >= 0:
        print(lista[i])
        i -= 1


'''
12. Escribir un programa que calcule el máximo común divisor de dos números
enteros introducidos por teclado, usando:
a) La función math.gcd.
b) Bucles
'''
from math import gcd


def max_com_div(n, m):
    print(gcd(n, m))


def mcd(n, m):
    v = n % m
    if n == m:
        print(n)

    if n > m and v == 0:
        print(m)
    else:
        mcd(m, v)


def maximo_comun_divisor(a, b):
    aux = 0
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

'''
max_com_div = lambda a, b: a if a == b else \
                                b if a > b and a % b == 0 else \
                                max_com_div(b, a % b)

min_com_mul = lambda a, b: (a * b) / max_com_div(a, b)
'''

'''
13. Escribir un programa que determine si un número entero introducido por
teclado es primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente
por sí mismo y por 1.
'''


def es_primo(n):
    def divisores(n):
        def es_divisor_de(a, b):
            return b % a == 0

        num_div = 0
        i = 1
        while i <= n:
            if es_divisor_de(i, n):
                num_div += 1
            i += 1
        return num_div
    return divisores(n) == 2


def prim_comp():
    while True:
        try:
            n = int(input('Introduzca un numero entero positivo: '))
            if n <= 0:
                print('El número ha de ser mayor a 0')
            else:
                break
        except ValueError:
            print('El número introducido no es correscto')
    if es_primo(n):
        print('El número es primo')
    else:
        print('El número es compuesto')

    i = 1
    primos = 0
    while primos < n:
        if es_primo(i):
            primos += 1
            print(i, end=' ')
        i += 1


# Los x primeros numeros primos
def primo():
    while True:
        try:
            n = int(input('Introduzca un numero entero positivo: '))
            if n <= 0:
                print('El número ha de ser mayor a 0')
            else:
                break
        except ValueError:
            print('El número introducido no es correscto')
    if es_primo(n):
        print('El número es primo')
    else:
        print('El número es compuesto')

    i = 1
    primos = 0
    while primos < n:
        if es_primo(i):
            primos += 1
            print(i, end=' ')
        i += 1


# todos los primos menores que una cantidad
def primos():
    while True:
        try:
            n = int(input('Introduzca un numero entero positivo: '))
            if n <= 0:
                print('El número ha de ser mayor a 0')
            else:
                break
        except ValueError:
            print('El número introducido no es correscto')
    if es_primo(n):
        print('El número es primo')
    else:
        print('El número es compuesto')

    i = 1
    primos = 0
    while i < n:
        if es_primo(i):
            primos += 1
            print(i, end=' ')
        i += 1


# todos los primos menores que una cantidad
def primos2():
    while True:
        try:
            n = int(input('Introduzca un numero entero positivo: '))
            if n <= 0:
                print('El número ha de ser mayor a 0')
            else:
                break
        except ValueError:
            print('El número introducido no es correscto')
    if es_primo(n):
        print('El número es primo')
    else:
        print('El número es compuesto')

    primos = [i for i in range(1, n + 1) if es_primo(i)]
    print(primos)


def primos3(n):
    def primos_iter(i, acc):
        if i >= n:
            return acc
        else:
            if es_primo(i):
                return primos_iter(i + 1, acc + [i])
            else:
                return primos_iter(i + 1, acc)
    return primos_iter(1, [])


# los n primeros numeros primos
def primos4(n):
    def primos_iter(i,):
        nonlocal cuantos
        if cuantos == n:
            return acc

        if es_primo(i):
            cuantos += 1
            acc.append(i)
            return primos_iter(i + 1)
    cuantos = 0
    acc = []
    return primos_iter(1)


def primo5(n):
    p = 0
    for i in range(1, n):
        if es_primo(i):
            p += 1
    return p


'''
14. Escribir un programa que gestione datos almacenados en una lista, de forma que
muestre un menú con las siguientes opciones:

1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.

El programa deberá pedir la información necesaria para cada opción elegida por el
usuario.
'''

def gestor_datos():
    LISTA = []
    def anniadir():
        nonlocal LISTA
        dato = input('Introduzca el nuevo elemento de la lista: ')
        LISTA.append(dato)


    def cambiar_elem():
        def pedir_num():
            while True:
                try:
                    indice = int(input('Introduzca el indice del dato a cambiar: '))
                    if indice >= 0:
                        break
                    print('El número de indice debe ser, al menos, 0.')
                except ValueError:
                    print('Debe introducir una número entero mayor o igual a 0')
            return indice

        num_indice = pedir_num()
        i = 0
        while i < num_indice:
            if i > len(LISTA):
                print('No hay tantos elementos en la lista')
            i += 1




    def eliminar_uno():
        pass


    def eliminar_todo():
        pass


    def mostrar_lista():
        print(LISTA)


    while True:
        print('''
        1. Añadir un elemento al archivo.
        2. Cambiar el valor de un elemento del archivo.
        3. Eliminar un elemento del archivo.
        4. Eliminar todos los elementos del archivo.
        5. Mostrar los elementos del archivo.
        0. Salir del programa.
        '''
            )
        a = input('Elija una de las opciones: ')

        if a == '1':
            anniadir()
        elif a == '2':
            cambiar_elem()
        elif a == '3':
            eliminar_uno()
        elif a == '4':
            eliminar_todo()
        elif a == '5':
            mostrar_lista()
        elif a == '0':
            break
        else:
            print('Opción incorrecta')

'''
15. Los datos de los empleados de una empresa se almacenan en una lista de
tuplas, donde cada tupla representa a un empleado de la siguiente forma:
(nombre, apellidos, salario)
En el programa, los cuatro empleados que tiene la empresa se almacenan
en la siguiente lista:
empleados = [('María', 'González', 1800.23),
('Javier', 'Ruiz', 1630.50),
('Jesús', 'Pérez', 2100.42),
('Rosa', 'Muñoz', 2240.78)]
Se pide escribir un programa que modifique la lista de empleados incrementando
en un 10% el salario de cada empleado y muestre por pantalla el salario total
de los empleados de la empresa
'''


'''
16. Escribir un programa que gestione datos almacenados en un fichero, de forma
que muestre un menú con las siguientes opciones:

1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.

El programa deberá pedir la información necesaria para cada opción elegida por
el usuario.

# Hacer subprogramas uno para cada opción, y que el programa llame al subprograma
#  adecuado cuando el usuario introduzaca una opción concreta
'''
from functools import cached_property
import os

ARCHIVO = "archivo.txt"

def anyadir():
    cadena = input('Introduzca la cadena a añadir al archivo: ')
    with open(ARCHIVO, 'a', encoding='UTF-8') as f:  # El with garantiza el cierre del progrma a pesar de posibles errores
        print(cadena, file=f)


def pedir_numero():
    while True:
        try:
            num_linea = int(input('Introduzca el número de línea a cambiar: '))
            if num_linea >= 1:
                break
            print('El número de línea debe ser, al menos, 1.')
        except ValueError:
            print('Debe introducir un número')
    return num_linea


def cambiar():
    num_linea = pedir_numero()
    with open(ARCHIVO, 'r+', encoding='UTF-8') as f:
        i = 1
        pos = 0
        linea = ''
        while i <= num_linea:
            pos = f.tell()
            linea = f.readline()
            if linea == '':
                print('ERROR: No hay tantas líneas')
                break
            linea = linea[:-1]
            i += 1
        f.seek(pos)
        long = len(linea)
        if linea == '':
            print('No se puede cambiar una línea vacía.')
        else:
            while True:
                print('Debe introducir una cadena con', long, 'caracteres.')
                cadena = input('Introduzca la nueva cadena: ')
                if len(cadena) == long:
                    print(cadena, file=f)
                    break


def elim_elem():
    def limpiar_aux():
        with open('auxiliar.txt', 'w', encoding='UTF-8'):
            pass
    num_linea = pedir_numero()
    limpiar_aux()
    with open(ARCHIVO, 'r', encoding='UTF-8') as viejo:
        with open('auxiliar.txt', 'a', encoding='UTF-8') as nuevo:
            i = 1
            while True:
                linea = viejo.readline()
                if linea == '':
                    break
                if i != num_linea:
                    nuevo.write(linea)
                i += 1
    os.rename('auxiliar.txt', ARCHIVO)  # Machaca el archivo de destino


def elim_todo():
    with open(ARCHIVO, 'w', encoding='UTF-8'):
        pass


def mostrar():
    with open(ARCHIVO, 'r', encoding='UTF-8') as f:
        while True:
            cadena = f.readline().rstrip()
            if cadena == '':
                break
            print(cadena)


while True:
    print('''
    1. Añadir un elemento al archivo.
    2. Cambiar el valor de un elemento del archivo.
    3. Eliminar un elemento del archivo.
    4. Eliminar todos los elementos del archivo.
    5. Mostrar los elementos del archivo.
    0. Salir del programa.
    '''
          )
    opcion = input('Introduzca una opción: ')

    if opcion == '1':
        anyadir()
    elif opcion == '2':
        cambiar()
    elif opcion == '3':
        elim_elem()
    elif opcion == '4':
        elim_todo()
    elif opcion == '5':
        mostrar()
    elif opcion == '0':
        break
    else:
        print('Opción incorrecta')
