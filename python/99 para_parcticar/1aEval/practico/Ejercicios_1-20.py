"""[summary]
"""
from math import pi

'''1.
    Escribe un programa que salude al usuario con el mensaje
    «Hola. Encantado de conocerle.».
'''
print('Hola. Encantado de conocerle')

'''2.
    Escribe un programa que pida un número al usuario y a continuación
    lo muestre.
'''
n = input('Introduce un número: ')
print(n)

'''3.
    Escribe un programa que pida al usuario su edad y muestre la que tendrá
    el año que viene.
'''
n = int(input('Introduce tu edad: '))
print(n + 1)

'''4.
    Escribe un programa que pida el año actual y el de nacimiento del usuario.
    Debe calcular su edad, suponiendo que en el año en curso el usuario ya ha
    cumplido años.
'''
def edad():
    """Calcula la edad a partir del año de nacimiento y el actual
    """
    a = int(input('Introduzca año actual: '))
    b = int(input('Introduzca su año de nacimiento: '))
    print(f'Tu edad es: {a - b}')

'''5.
    Escribe un programa que calcule la media aritmética de dos notas enteras.
    Hay que tener en cuenta que la media puede contener decimales.
'''
def med_arit_2(nota1, nota2):
    """Calcula la media aritmética de dos notas.

    Args:
        nota1 (numeric): Primera nota
        nota2 (numeric): Segunda nota

    Returns:
        numeric: Media aritmética
    """
    return (nota1 + nota2) / 2

'''6.
    Escribe un programa que calcule la longitud y el área de una circunferencia.
    Para ello, el usuario debe introducir el radio (que puede contener decimales).
    Recordemos:
    𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜
    ́𝑎𝑟𝑒𝑎 = 𝜋 · 𝑟𝑎𝑑𝑖𝑜²
'''

def long_area():
    """Calcula la longitud y el área de una circinferencia en las unidades del dato introducido
    """
    r = float(input('Introduzca el radio de la circunferencia: '))
    l = 2 * pi * r
    a = pi * r ** 2
    print(f'La longitud de es: {l}')
    print(f'El área es: {a}')

'''7.
    Pide dos números al usuario: a y b. Deberá mostrar True si ambos
    números son iguales y False en caso contrario.
'''
def son_iguales():
    """Pide dos números y comprueba si son iguales

    Returns:
        bool: True o False
    """
    a = input('Introduzca un número: ')
    b = input('Intoduzca otro número: ')
    return a == b

'''8.
    Escribe un programa que solicite al usuario su edad y le indique
    si es mayor de edad (mediante un literal booleano True o False).
'''
def mayor():
    """Pregunta la edad y confirma si es mayor de edad

    Returns:
        bool: True o False
    """
    n = int(input('Introduzca su edad: '))
    return n >= 18

'''9.
    Escribe un programa que solicite al usuario un número y le indique
    si es par (mediante un literal booleano True o False).
'''
def es_par():
    """Comprueba si un número es par.

    Returns:
        bool: True o False
    """
    n = float(input('Introduzca un número: '))
    return n % 2 == 0

'''10.
    Escribir un programa que nos indique si podemos salir a la calle.
    Existen aspectos que influirán en esta decisión:
    si está lloviendo y si hemos terminado nuestras tareas.
    Solo podremos salir a la calle si no está lloviendo y hemos finalizado
    nuestras tareas.
    Existe una opción en la que, indistintamente de lo anterior, podremos
    salir a la calle:
    el hecho de que tengamos que ir a la biblioteca (para realizar algún
    trabajo, entregar un libro, etc.).
    Solicitar al usuario (mediante un booleano) si llueve, si ha finalizado
    las tareas y si necesita ir a la biblioteca.
    El programa deberá mostrar mediante un booleano (True o False)
    si es posible que se le otorgue permiso para ir a la calle.
'''
def permiso_para_salir():
    """Comprueba si se otorga permiso para salir

    Returns:
        bool: True o False
    """
    l = input('Indique mediante True o False si está lloviendo o no: ')
    t = input('Indique mediante True o False si a acabado las tareas: ')
    b = input('Indique mediante True o False si tiene que ir a la biblioteca: ')
    if l == t == 'True' or b == 'True':
        return True
    return False

'''11.
    Un frutero necesita calcular los beneficios anuales que obtiene de la
    venta de manzanas y peras. Por este motivo, es necesario diseñar un
    programa que solicite las ventas (en kilos) de cada semestre para cada fruta.
    El programa mostrará el importe total sabiendo que el precio del kilo de
    manzanas está fijado en 2.35 € y el kilo de peras en 1.95 €.
'''
def frutero():
    """Pide las ventas semestrales de peras y manzanas y calcula las ganacias anuales.

    Returns:
        numeric: Ganancias anuales.
    """
    val_man = 2.35
    val_pera = 1.95
    subtotal = 0
    cont = 1
    while cont <= 2:
        print(f'Introduzca las ventas del semestre nº {cont}')
        m = float(input('Kilos de manzana: '))
        p = float(input('Kilos de peras: '))
        subtotal += (val_man * m) + (val_pera * p)
        cont += 1
    return round(subtotal, 2)

'''12.
    Escribe un programa que pida un número al usuario y muestre su valor absoluto.
'''
def fruteria():
    """Pide las ventas semestrales de peras y manzanas y calcula las ganacias anuales.

    Returns:
        numeric: Ganancias anuales.
    """
    val_man = 2.35
    val_pera = 1.95
    subtotal = 0
    cont = 1
    while cont <= 2:
        print(f'Introduzca las ventas del semestre nº {cont}')
        m = float(input('Kilos de manzana: '))
        p = float(input('Kilos de peras: '))
        subtotal += (val_man * m) + (val_pera * p)
        cont += 1
    return round(abs(subtotal))

'''13.
    Escribe un programa que solicite las notas del primer, segundo y
    tercer trimestre (notas enteras que se solicitarán al usuario).
    El programa debe mostrar la nota media del curso como se utiliza en el
    boletín de calificaciones (sólo la parte entera) y como se usa en el
    expediente académico (con decimales).
'''
def notas():
    """Calcula la nota media del curso, para el voletin y el expediente del alumno
    """
    cont = 1
    nota = 0
    try:
        while cont <= 3:
            n = int(input(f'Introduce la nota del trimestre nº {cont}: '))
            nota += n
            cont += 1
            boletin = int(nota // 3)
        expediente = round(nota / 3, 2)
        print(f'Nota boletin {boletin}')
        print(f'Nota expediente {expediente}')
    except ValueError:
        print('Han de ser números enteros')


'''14.
    Escribir un programa que pida como entrada un número decimal y lo muestre
    redondeado al entero más próximo.
'''
def entero_mas_proximo():
    """Pide un número decimal y devuelve el entero más proximo

    Returns:
        int: Entero más cercano al valor del input.
    """
    n = float(input('Introduzca un número decimal: '))
    return int(round(n))

'''15.
    Un economista te ha encargado un programa para realizar cálculos con el IVA.
    El programa debe solicitar la base imponible y el IVA que se debe aplicar.
    Muestra en pantalla el importe correspondiente al IVA y al total.
'''
def economista(base, iva):
    """Calcula el Total a pagar y el importe por iva

    Args:
        base (numeric): Precio base imponible al producto
        iva (mumeric): iva aplicable al producto
    """
    iva = base * (iva / 100)
    total = iva + base
    print(f'Importe por iva: {iva}, Precio total: {total}')

from math import sqrt
'''16.
    Escribe un programa que tome como entrada un número entero e indique qué
    cantidad hay que sumarle para que el resultado sea múltiplo de 7. Un ejemplo:

        A 2 hay que sumarle 5 para que el resultado (2 + 5 = 7) sea múltiplo de 7.

        A 13 hay que sumarle 1 para que el resultado (13 + 1 = 14) sea múltiplo
        de 7.

    Si proporcionas el número 2 o el 13, la salida del programa debe ser 5 ó 1,
    respectivamente.

    Indicación: Usar el operador módulo.
'''
def multiplo_7(num):
    """Dice cuanto se le ha de sumar al valor proporcionado
       para que se multiplo de 7

    Args:
        num (int): Un entero cualquiera

    Returns:
        int: Valor que sumado a num da como resultado un multiplo de 7
    """
    cont = 0
    while not num % 7 == 0:
        num += 1
        cont += 1
    return cont

'''17.
    Modifica el ejercicio anterior para que, indicando dos números n y m,
    diga qué cantidad hay que sumarle a n para que sea múltiplo de m.
'''
def es_multiplo(n, m):
    """Dice cuanto hay que sumarle a n para que sea multiplo de m

    Args:
        n (int): Valor a modificar
        m (int): Valor del para el cual n ha de ser un multiplo

    Returns:
        int: Cantidad a sumar a n para que sea multiplo de m
    """
    cont = 0
    while n % m != 0:
        cont += 1
        n += 1
    return cont

'''18.
    Escribe un programa que pida la base y la altura de un triángulo y
    muestre su área.
    ́𝑎𝑟𝑒𝑎 = 𝑏𝑎𝑠𝑒 × 𝑎𝑙𝑡𝑢𝑟𝑎^2
'''
def area_triangulo():
    """Calcula el área de un triangulo

    Returns:
        float: Tamaño del área de un triangulo
    """
    b = float(input('Indique el tamaño de la base del triangulo: '))
    a = float(input('Indique la altura del triangulo: '))
    area = b * a ** 2
    return area

'''19.
    Dado el siguiente polinomio de segundo grado:
        y = ax² + bx + c
    escribe un programa que pida los coeficientes a, b y c, así como el
    valor de x, y calcule el valor correspondiente de y.
'''
def ec_segundo_grado():
    """Calcula el resultado de una ecuación de 2º grado

    Returns:
        float: Valor de y (solucion a la ecuación)
    """
    print('Para la sigiente ecuación de segundo grado: y = ax² + bx + c')
    a = float(input('Indique el valor de a: '))
    b = float(input('Indique el valor de b: '))
    c = float(input('Indique el valor de c: '))
    x = float(input('Indique el valor de x: '))
    return a * x ** 2 + b * x + c

'''20.
    Escribe un programa que solicite al usuario que introduzca una cantidad
    de segundos. El programa deberá mostrar cuántas horas, minutos
    y segundos hay en el número de segundos introducidos por el usuario.
'''
def h_m_s(seg):
    """Transforma los segundos al formato horas, minutos y segundos

    Args:
        seg (int): Cantidad de segundos a indicar
    """
    h = seg // 3600
    m = (seg - (h * 3600)) // 60
    s = seg - (h * 3600) - (m * 60)
    print (f'{h}:h, {m}:m, {s}:s')
