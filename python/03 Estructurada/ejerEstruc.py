'''
Considérese la siguiente fórmula (debida a Herón de Alejandrı́a),
que expresa el valor de la superficie S de un triángulo cualquiera
en función de sus lados, a, b y c:


Escribir una función que obtenga el valor SSS a partir de aaa, bbb y ccc,
evitando el cálculo repetido del semiperı́metro,
sp=a+b+c2sp = \frac{a+b+c}{2}sp=2a+b+c​, y almacenando el resultado
finalmente en la variable S.
'''
from math import sqrt
def heron(a, b, c):
    """Calcula la superficie de un triangulo

    Args:
        a (int): 1er lado del triangulo
        b (int): 2º lado del triangulo
        c (int): 3er lado del triangulo

    Returns:
        int: Superficie del triangulo
    """
    sp = (a + b + c) / 2
    s = sqrt((sp - a) * (sp - b) * (sp - c))
    return s

'''
Escribir tres funciones que impriman las siguientes salidas en función de
la cantidad de líneas que se desean (␣ es un espacio en blanco):

*****     ␣*         ␣␣␣␣*␣␣␣␣
*****     ␣␣*        ␣␣␣***␣␣␣
*****     ␣␣␣*       ␣␣*****␣␣
*****     ␣␣␣␣*      ␣*******␣
*****     ␣␣␣␣␣*     ␣␣␣␣*␣␣␣␣
'''

def rectangulo (n):
    i = 0
    while i < n:
        print('*****')
        i += 1


def rectangulo2(n):
    for _ in range(n):
        print('*****')


def rectangulo3 (n):
    print('*****\n' * n, end='')


def rectangulo4 (n):
    """Dibuja un triangulo

    Dibuja un rectangulo con asteriscos

    Args:
        n (int): la altura del triangulo

    """
    if n > 0:
        print('*****')
        rectangulo3(n - 1)


def diagonal (n):
    i = 0
    while i < n:
        print((' ' * i) + '*')
        i += 1


def diagonal2(n):
    for i in range(1, n + 1):
        print((' ' * i) + '*')

# Usar la funcion .center para el arbolito
# obtener formula que me diga el ancho en funcion del numero de lineas
#   EL numero de astericos y para el ancho, se obtiene como (n * 2) - 1


def arbol (n):
    """Dibuja un arbo de navidad con la altura indicada

    Args:
        n (int): Altura del arbol
    """
    def ancho(n):
        """Calcula e ancho del arbol segun la altura

        Args:
            n (int): Altura del arbol

        Returns:
            int: Ancho del arbol
        """
        return 2 * n - 1
    if n > 0:
        i = 1
        an = ancho(n)
        while i < n:
            a = '*' * ancho(i)
            print(a.center(an))
            i += 1
        print('*'.center(an))


def arbolito():
    n = int(input('Introduce la antura del arbol: '))
    for i in range(1, n * 2 - 1, 2):
        print(f'{"*"*i:^10}')
    x = '*'.center(n * 2 - 1)
    print(f'{x}')

'''
Convertir una cantidad de tiempo (en segundos, Z) en la correspondiente en horas,
minutos y segundos, con arreglo al siguiente formato:
3817 segundos = 1 horas, 3 minutos y 37 segundos
'''

def horas (n):
    h = n // 3600
    m = (n - (h * 3600)) // 60
    s = n - (h * 3600) - (m * 60)
    print(h, 'horas', m, 'minutos', s, 'segundos')


'''
Escribir un programa que, en primer lugar, lea los coeficientes a2 , a1 y a0
de un polinomio de segundo grado a2x^2 +a1x + a0 y escriba ese polinomio.
Y, en segundo, lea el valor de x y escriba qué valor toma el polinomio
para esa x.
Para facilitar la salida, se supondrá que los coeficientes y x son enteros.
Por ejemplo, si los coeficientes y x son 1, 2, 3 y 2, respectivamente,
la salida puede ser:

1x^2 + 2x + 3
p(2) = 11
'''
def polinomio_2(a0, a1, a2, x):
    print(a2, 'x² +', a1, 'x +', a0)
    resul = a2 * x ** 2 + a1 * x + a0
    print(resul)


def pol_2():
    while True:
        try:
            a0 = int(input('Introduzca un valor entero para a0: '))
            a1 = int(input('Introduzca un valor entero para a1: '))
            a2 = int(input('Introduzca un valor entero para a2: '))
            x = int(input('Introduzca un valor entero para x: '))
            print(a2, 'x² +', a1, 'x +', a0)
            resul = a2 * x ** 2 + a1 * x + a0
            print(resul)
            break
        except ValueError:
            print('Los vallores introducidos han de ser números enteros')


'''
Escribir un programa apropiado para cada una de las siguientes tareas:

a. Pedir los dos términos de una fracción y dar el valor de la división
correspondiente, a no ser que sea nulo el hipotético denominador, en cuyo
caso se avisará del error.

b. Pedir los coeficientes de una ecuación de segundo grado y dar las dos
soluciones correspondientes, comprobando previamente si el discriminante
es positivo o no.

c. Pedir los coeficientes de la recta ax +by +c =0 y dar su pendiente y
su ordenada en el origen en caso de que existan, o el mensaje apropiado
en otro caso.

d. Pedir un número natural n y dar sus divisores.
'''

def fraccion():
    while True:
        try:
            divn = float(input('Introduzca el dividendo: '))
            divs= float(input('Introduza el divisor: '))
            if divs == 0:
                print('No es posible realizar una división entre 0')
            else:
                resul = divn / divs
                return resul
        except ValueError:
            print('El dato ha de ser de tipo númerico')


'''
Escribir un programa que lea un carácter, correspondiente a un dígito
hexadecimal:
0, 1, ..., 9, A, B, ..., F
y lo convierta en el valor decimal correspondiente:
0, 1, ..., 9, 10, 11, ..., 15
'''


'''
Para hallar en qué fecha cae el Domingo de Pascua de un anyo cualquiera,
basta con hallar las cantidades a y b siguientes:
a = (19 * (anyo % 19) + 24) % 30
b = (2 * (anyo % 4) + 4 * (anyo % 7) + 6 * a + 5) % 7
y entonces, ese Domingo es el 22 de marzo + a + b días, que podrı́a caer
en abril. Escriba un programa que realice estos cálculos, produciendo
una entrada y salida claras.
'''


'''
Escribir una función para hallar (n, k), donde n y k son datos enteros
positivos,
a. mediante la fórmula n!
    (n−k)! k!
b. mediante la fórmula n(n−1)···(k+1)
    (n−k)!
¿Qué ventajas presenta la segunda con respecto a la primera?
'''
