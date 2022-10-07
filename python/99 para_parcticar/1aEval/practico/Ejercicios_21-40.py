"""[summary]
"""
'''21.
    Solicita al usuario tres distancias:
    · La primera, medida en milímetros.
    · La segunda, medida en centímetros.
    · La última, medida en metros.
    Escribe un programa que muestre la suma (en centímetros) de las tres
    longitudes introducidas.
'''
def suma_unidades():
    """Pasa tres valores de unidades de longitud distnta (mm, cm, m) a cm y los suma

    Returns:
        float: resultado de la suma
    """
    mm = float(input('Introduzca una medida en milimetros: '))
    cm = float(input('Introduzca una segunda medida en centimetros: '))
    m = float(input('Introduzca una última medida en metros: '))
    mm_a_cm = mm / 10
    m_a_cm = m * 100
    return (cm + mm_a_cm + m_a_cm)

'''22.
    Un biólogo está realizando un estudio de distintas especies de invertebrados y necesita
    un programa que le ayude a contabilizar el número de patas que tienen en total todos
    los animales capturados durante una jornada de trabajo.
    Para ello, te ha solicitado que escribas un programa al que hay que proporcionar:
    El número de hormigas capturadas (6 patas).
    El número de arañas capturadas (8 patas).
    El número de cochinillas capturadas (14 patas).
    El programa deberá mostrar el número total de patas.
'''
def cuenta_patas(h, a, c):
    """Suma el número de patas de la cantidad de hormigas, arañas y cochinillas indicada

    Args:
        h (int): Número de hormigas
        a (int): Número de arañas
        c (int): Número de cochinillas

    Returns:
        int: Número de patas totales
    """
    ph = 6 * h
    pa = 8 * a
    pc = 14 * c
    total = (ph + pa + pc)
    return total

'''23.
    Una empresa que gestiona un parque acuático te solicita un programa que les ayude
    a calcular el importe que hay que cobrar en la taquilla por la compra de una serie de
    entradas (cuyo número será introducido por el usuario). Existen dos tipos de entrada:
    infantil, que cuestan 15.50 €; y de adultos, que cuestan 20 €.
    En el caso de que el importe total sea igual o superior a 100 €, se aplicará automática-
    mente un bono descuento del 5 %.
'''
def parque_acuatico():
    """Calcula el precio a pagar por las entradas de un parque acuático

    Returns:
        numeric: Precio total de la entrada al parque
    """
    p_adulto = 20
    p_infantil = 15.50
    ea = int(input('Introduzca el nº de entradas para adultos: '))
    en = int(input('Introduzca el nº de entradas infantiles: '))
    subtotal = ea * p_adulto + en * p_infantil
    if subtotal >= 100:
        total = subtotal * 0.95
    else :
        total = subtotal
    return total

'''24.
    Solicita al usuario un número real y calcula su raíz cuadrada.
    Realiza dos versiones del programa:
    Importando la función raíz cuadrada del módulo correspondiente.
    Importante el propio módulo.
'''
from math import sqrt
def raiz_cuadrada1():
    """Calcula la raíz cuadrada de un número real

    Returns:
        float: Raiz cuadrada del número indicado
    """
    n = float(input('Introduce un número perteneciente al conjunto de los reales: '))
    return sqrt(n)

import math
def raiz_cuadrada2():
    """Calcula la raíz cuadrada de un número real

    Returns:
        float: Raiz cuadrada del número indicado
    """
    n = float(input('Introduce un número perteneciente al conjunto de los reales: '))
    return math.sqrt(n)

'''25.
    La FILA (Federación Internacional de Lanzamiento de Algoritmo) realiza una compe-
    tición donde cada participante escribe un algoritmo en un papel y lo lanza, ganando
    quien consiga lanzarlo más lejos. La peculiaridad del concurso es que la longitud del
    lanzamiento se mide en metros (con tantos decimales como se desee), pero para el
    ranking solo se tiene en cuenta la longitud en centímetros (sin decimales). Por ejemplo,
    para un lanzamiento de 12.3456 m (que son 1234.56 cm) solo se contabilizarán 1234 cm.
    Escribe un programa que solicite la longitud (en metros) de un lanzamiento, y muestre
    la parte entera correspondiente en centímetros.
'''
def fila():
    """Retorna el valor truncado en centrimetros del valor en metros indicado

    Returns:
        int: Distancia truncada en centimetros
    """
    l = float(input('Introduzca la longitud del lanzamiento en metros: '))
    c = l * 100
    return math.trunc(c)

'''26.
    Escribir un programa que solicite al usuario un número e indique si es par o impar.
'''
def par_o_impar():
    """Solicita un númeor al usuario y le indica si es par o impar
    """
    n = float(input('Introduce un número: '))
    if n % 2 == 0:
        print(f'El número {n} es par.')
    else:
        print(f'El número {n} es impar.')

'''27.
    Pedir dos números enteros y decir si son iguales o no.
'''
def son_iguales():
    """Compara dos números enteros e indica si son iguales o no

    Returns:
        bool: True o False
    """
    try:
        n = int(input('Introduce el primer número entero: '))
        m = int(input('Introduce el segundo número entero: '))
        return n == m
    except ValueError:
        print('Se ha de indicar dos números enteros')

'''28.
    Solicitar dos números distintos y mostrar cuál es el mayor.
'''
def el_mayor():
    """Solicita dos números distintos e indica cual es el mayor.
    """
    n = float(input('Introduzca el primer número: '))
    m = float(input('Introduzca el segundo número: '))
    while m == n:
        print()
        print('Han de ser número distintos')
        m = float(input('Introduzca el segundo número nuevamente: '))
    if n > m:
        print(f'El primer número "{n}", es el mayor.')
    else:
        print(f'El segundo número "{m}", es el mayor.')

'''29.
    Solicitar dos números (que pueden ser iguales o distintos) y mostrar cuál es el mayor.
'''
def mayor():
    """Compara dos números e indica cual es el mayor
    """
    n = float(input('Introduzca el primer número: '))
    m = float(input('Introduzca el segundo número: '))
    if n > m:
        print(f'El primer número "{n}", es el mayor.')
    else:
        print(f'El segundo número "{m}", es el mayor.')

'''30.
    Implementar un programa que pida por teclado un número decimal e indique si es un
    número casi-cero, que son aquellos números (positivos o negativos) que se acercan a
    cero por menos de 1 unidad (aunque, curiosamente, el 0 no se considera un número
    casi-cero). Ejemplos de números casi-cero son el 0.3, el −0.99 o el 0.123. En cambio,
    algunos números que no se consideran casi-cero son 12.3, el 0 o el −1
'''
def casi_cero():
    """Comprueba si un número es un número casi-cero

    Los valores casi-cero son los que se acercan a cero por menos de 1 unidad.
    El 0, 1 y -1 no se consideran casi-cero
    """
    n = float(input('Introduzca un número: '))
    m = abs(0 - n)
    if n in range(-1, 2):
        print(f'{n} no es un núnero casi-cero')
    elif m < 1:
        print(f'{n} es un número casi-cero')
    else:
        print(f'{n} no es un núnero casi-cero')
    print()

'''31.
    Pedir dos números y mostrarlos ordenados en orden decreciente.
'''
def orden():
    """Pide dos números y los ordena de menor a mayor.
    """
    n = float(input('Introduce el primer número: '))
    m = float(input('Introduce el segundo número: '))
    if n > m:
        print(f'{m}, {n}')
    else:
        print(f'{n}, {m}')

'''32.
    Pedir tres números y mostrarlos ordenados de mayor a menor.
'''
def ordena():
    """Pide tres números y los ordena de menor a mayor.
    """
    a = float(input('Introduce el primer número: '))
    b = float(input('Introduce el segundo número: '))
    c = float(input('Introduce el último número: '))
    l = [a, b, c]
    l.sort()
    return l

'''33.
    Pedir los coeficientes de una ecuación de segundo grado y mostrar sus soluciones reales.
    Si no existen, habrá que indicarlo. Hay que tener en cuenta que las soluciones de una
    ecuación de segundo grado 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 son:
    𝑥 = −𝑏 ± √𝑏2 − 4𝑎𝑐
            2𝑎
'''
from math import sqrt
def ec_seg_grdo():
    """Calcula los valores de x para una Ec. de segundo grado, pero solo dentro de los reales.
    """
    print('Para la siguiente ecuación de segundo grado: ax² + bx + c = 0')
    a = float(input('Introduce el valor de a: '))
    b = float(input('Introduce el valor de b: '))
    c = float(input('Introduce el valor de c: '))
    try:
        raiz = sqrt((b ** 2) - (4 * a * c))
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print(f'x = {x1} y x = {x2}')
    except ValueError:
        print('Los resultados no estan dentro del conjunto de los reales')

'''34.
    Escribir un programa que indique cuántas cifras tiene un número entero introducido
    por teclado, que estará comprendido entre 0 y 99999.
'''
def long_num_entero():
    """Pide un número entero y calcula su longitud.

    Returns:
        int: Longitud del número introducido.
    """
    try:
        num = len(str(int(input('Introduzca un número entero: '))))
        return num
    except ValueError:
        print('Se debe introducir un número entero')

'''35.
    Pedir una nota entera de 0 a 10 y mostrarla de la siguiente forma:
    Insuficiente (de 0 a 4).
    Suficiente (5).
    Bien (6).
    Notable (7 y 8).
    Sobresaliente (9).
    Matrícula de honor (10).
'''
def nota():
    """Adjudica una calificación sobre las notas introducidas.
    """
    try:
        nota = int(input('Introduce una nota (Valor entero): '))
        while nota not in range(0, 11):
            print()
            print('La nota debe ser un entero entre 0 y 10')
            nota = int(input('Vuelva a introducir la nota: '))
        print()
        if nota in range(0, 5):
            print('Insuficiente')
        elif nota == 5:
            print('Suficiente')
        elif nota == 6:
            print('Bien')
        elif nota in range(7, 9):
            print('Notable')
        elif nota == 9:
            print('Sobresaliente')
        elif nota == 10:
            print('Matrícula de honor')
        print()
    except ValueError:
        print('Se ha de introducir un número entero.')

'''36.
    Escribir un programa que solicite al usuario un número comprendido entre 1 y 7,
    correspondiente a un día de la semana. Se debe mostrar el nombre del día de la semana
    al que corresponde. Por ejemplo, el número 1 corresponde a «lunes» y el 6 a «sábado».
'''
def dia():
    """Pide un número (1-7) y devuelve el día de la sema correspondiente a ese número

    Returns:
        str: Nombre del del día de la semana.
    """
    dia = {1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado', 7:'Domingo'}
    try:
        n = int(input('Introduce un número entre 1 y 7: '))
        while n not in range(1, 8):
            n = int(input('El número debe estár entre 1 y 7: '))
            print()
        return dia[n]
    except ValueError:
        print('Ha de introducir un número entre 1 y 7')

'''37.
    Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Hay que tener en
    cuenta que existen meses con 28, 30 y 31 días (no se considerará los años bisiestos).
'''
from datetime import datetime

def n_dias():
    try:
        año = input('Introduce el año: ')
        mes = input('Introduce el nº del més: ')
        dia = input('Introduce el nº de día del mes: ')
        f = (año, mes, dia)
        fecha = '-'.join(f)
        if datetime.strptime(fecha, '%Y-%m-%d'):
            return True
    except ValueError:
        return False


'''38.
    Hacer el mismo ejercicio anterior pero considerando los años bisiestos.
    Un año es bisiesto si cumple las siguientes condiciones:
    Es bisiesto si es divisible entre 4.
    Pero no es bisiesto si es divisible entre 100.
    Pero sí es bisiesto si es divisible entre 400. (2000 y 2400 sí son bisiestos porque
    son divisibles entre 100 pero también entre 400. 1900, 2100, 2200 y 2300 no lo son
    porque solo son divisibles entre 100).
'''
def n_dias_2():
    mtreinta = [4, 6, 9, 11]
    anio = int(input('Introduce el año: '))
    mes = int(input('Introduce el nº del més: '))
    dia = int(input('Introduce el nº de día del mes: '))
    if dia > 28 and mes == 2:
        return "No es una fecha válida"
    if dia > 30 and mes in mtreinta:
        return "No es una fecha válida"
    if not anio % 4 and (anio % 100 or not anio % 400):
        print("Es bisiesto")
    return f"{dia}-{mes}-{anio}"

'''39.
    Escribir un programa que solicite al usuario una fecha (día, mes y año) y muestre la
    fecha correspondiente al día siguiente.
'''
def manana():
    anio = int(input('Introduce el año: '))
    mes = int(input('Introduce el nº del més: '))
    dia = int(input('Introduce el nº de día del mes: '))
    treinta = [4, 6, 9, 11]
    if dia > 28 and mes == 2:
        return 'No es una fecha válida'
    if dia > 30 and mes in treinta:
        return 'No es una fecha válida'
    if (dia == 30 and mes in treinta) or (mes == 2 and dia == 28):
        mes += 1
        dia = 1
        return f"{dia}-{mes}-{anio}"
    if dia == 31 and mes == 12:
        anio += 1
        dia = 1
        mes = 1
        return f"{dia}-{mes}-{anio}"
    if dia != 31 and mes != 12 and mes not in treinta:
        dia += 1
        return f"{dia}-{mes}-{anio}"

'''40.
    Escribir un programa que pida una hora de la siguiente forma: hora, minutos y segundos.
    El programa debe mostrar qué hora será un segundo más tarde.
    Por ejemplo: hora actual: 10:41:59 → hora actual + 1 segundo: 10:42:00.
'''
def seg_mas():
    horas = int(input("Indique el valor de la hora: "))
    minutos = int(input("Indique el valor de los minutos: "))
    segundos = int(input("Indique el valor de los segundos: "))

    if segundos != 60:
        segundos += 1

    if minutos == 60 or (minutos == 60 and segundos == 60):
        horas += 1
        minutos = 0
        segundos = 0

        return f"{horas}:{minutos}:{segundos}"

    if minutos != 60 and segundos == 60:
        minutos += 1
        segundos = 0

    return f"{horas}:{minutos}:{segundos}"
