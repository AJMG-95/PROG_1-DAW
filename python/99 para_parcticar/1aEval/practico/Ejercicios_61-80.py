'''61.
Solicita al usuario un número n y dibuja un triángulo de base y altura n, de la siguiente
forma (para 𝑛 = 4):
    *
   * *
  * * *
 * * * *
'''


def triangulo_equi():
    """Dijuja en pantalla un trianguilo equilatero de ancho n usando '*' para ello.
    """
    numero = int(input("Dime cuantas estrellitas quieres: "))
    for i in range(numero + 1):
        if i == 1:
            res = f'{i * "*"}'
        else:
            res = f'{i * "* "}'
        print(res.center(numero * 2).rstrip())

def problema_61():
    """Dijuja en pantalla un trianguilo equilatero de ancho n usando '*' para ello.
    """
    n = int(input("Escribeme un número: "))
    estrellita = "* "
    espacio = " "
    for i in range(0, n + 1):
            print((i * estrellita + espacio).center(20))

'''62.
Para dos números dados, a y b, es posible buscar el máximo común divisor (el número
más grande que divide a ambos números) mediante un algoritmo ineficiente pero
sencillo: desde el menor de a y b, ir buscando de forma decreciente el primer número
que divide a ambos simultáneamente. Realiza un programa que calcule el máximo
común divisor de dos números.
'''
def maxcomdiv():
    num1 =int(input('Introduce un número: '))
    num2 =int(input('Introduce un número: '))
    a, b = max(num1, num2), min(num1, num2)
    while b:
        mcd = b
        b = a % b
        a = mcd
    return mcd

def mcd_euclides(a, b):
    """Calcula el maximo común divisor de dos números.

    Args:
        a (int | float): Valor numeérico para la variable a.
        b (int | float): Valor numeérico para la variable b.

    Returns:
        int | float: maximo común divisor entre a y b.
    """
    if b > a:
        a, b = b ,a # para que a sea el mayor
        while  a % b != 0:
            b, a = a % b, b
        return b

def problema_62(): # Divisores comunes
    """ Pide al ususario dos números a y b. Y Calcula el maximo común divisor de dos números a y b.

    Pre:
        Los Valores introducidos han de ser de tipo entero.

    Returns:
        int | float: maximo común divisor entre a y b.
    """
    numero_1 = int(input("Escribe el primer número: "))
    numero_2 = int(input("Escribe el segundo número: "))
    minimo = min(numero_1, numero_2)
    i = minimo
    while True:
        if numero_1 % i == 0 and numero_2 % i == 0:
            return i
        i -= 1

def mcd_div_com(a, b): # Divisores comunes
    """Calcula el maximo común divisor de dos números.

    Args:
        a (int | float): Valor numeérico para la variable a.
        b (int | float): Valor numeérico para la variable b.

    Returns:
        int | float: maximo común divisor entre a y b.
    """
    maximo = 1
    def frac(a, b):
        return (a / b) - int(a / b)
    for i in range(1, min(a, b) + 1):
        if frac(a, i) == 0 and frac(b, i) == 0:
            maximo = i
    return maximo

'''63.
De forma similar al ejercicio anterior, implementa un algoritmo que calcule el mínimo
común múltiplo de dos números dados.
'''
def mcm():
    """Piede al ususario dos números a y b y calcula el minimo común multiplo.

    Pre:
        Los valores de a y b an de ser números de tipo entero.

    Returns:
        int: Minimo común mutiplo entre a y b.
    """
    num1 =int(input('Introduzca el valor de a: '))
    num2 =int(input('In: troduzca el valor de b: '))
    a = max(num1, num2)
    b = min(num1, num2)
    while b:
        mcd = b
        b = a % b
        a = mcd
    mcm =  (num1 * num2) // mcd
    return mcm

def problema_64():
    numero_1 = int(input("Escribe el primer número: "))
    numero_2 = int(input("Escribe el segundo número: "))
    maximo = max(numero_1, numero_2)
    i = maximo
    while True:
        if i % numero_1 == 0 and i % numero_2 == 0:
            print(i)
            break
        i += 1

def mincommul(a ,b):
    """Calcula el minimo común multiplo de dos números.

    Args:
        a (int | float): Valores numéricos.
        b (int | float): Valores numéricos.

    Returns:
        int | float: Valor del minimo común multiplo de entre a y b.
    """
    return (a * b) / maxcomdiv()

def es_multiplo(n, m):
    """Comprueba si un número 'n' es multiplo de otro 'm'.

    Args:
        n (int | float): Posible multiplo de m.
        m (int | float): Valor para el que se comprueba si n es un multiplo suyo.

    Returns:
        int | float: True si n es multiplo de m o False si no lo es.
    """
    res = 0
    for i in str(n):
        res += int(i)
    for e in range(1, 11):
        if e * m == res:
            return True
        return False

'''64.
Escribir una función que calcule el máximo común divisor de tres números (ver los dos
ejercicios anteriores).
'''
def MCD():
    """Pide al usuario tres números y calcula el maximo común divisor.

    Pre:
        input() -> int

    Returns:
        int: Maximo común divisor de los tres valores introducidos.
    """
    l = []
    for _ in range(3):
        num = int(input('Introduce un número: '))
        l.append(num)
    mcd = min(l)
    while True:
        if l[0] % mcd == 0 and l[1] % mcd == 0 and l[2] % mcd == 0:
            return mcd
        mcd -= 1

'''65.
Calcula la raíz cuadrada de un número natural mediante aproximaciones. En el caso
de que no sea exacta, muestra el resto.
Por ejemplo, para calcular la raíz cuadrada de 23,
probamos 12 = 1, 24 = 4, 32 = 9, 42 = 16, 52 = 25 (nos pasamos), resultando 4 la raíz
cuadrada de 23 con un resto (23 − 16) de 7.
'''
def problema_66():
    """Pide un número al usuario u calcula su raiz cuadrada por aproximación.

    Pre:
        input() -> int

    Returns:
        str: Valor del aproximado y el resto.
    """
    numero = int(input("Escribe el primer número: "))
    cont = 1
    while True:
        if cont ** 2 < numero:
            cont += 1
        else:
            return f"el resultado es {cont - 1} y el resto es {abs(numero - ((cont - 1) ** 2))}"

'''66.
Escribe un programa que solicite al usuario las distintas cantidades de dinero de las
que dispone. Por ejemplo, la cantidad de dinero que tiene en el banco, en una hucha,
en un cajón y en los bolsillos. El programa mostrará la suma total de dinero de la que
dispone el usuario. La manera de especificar que no se desea introducir más cantidades
es mediante el cero.
'''
def suma_dinero():
    d = {'el banco':'', 'la hucha':'', 'el cajon':'', 'los bolsillos':''}
    a = 0
    for i in d:
        a = input(f'Introduzca la cantidad de dinero que tiene en {i}: ')
        d[i] = a
    return sum([int(value) for value in d.values()])

'''67.
Diseñar la función eco a la que se le pasa como argumento un número entero n y
muestra por pantalla n veces el mensaje «Eco...».
'''
def eco(n):
    print('Eco... ' * n)

'''68.
Escribir una función a la que se le pasen dos enteros y muestre todos los números
comprendidos entre ellos.
'''
def comprende(n, m):
    for i in range(n + 1 , m):
        print(i)

'''69.
Escribir una función a la que se le pasen dos enteros y devuelva en una lista todos los
números comprendidos entre ellos.
'''
def comprendidos(n, m):
    print([i for i in range(n + 1, m)])

'''70.
Escribir una función que calcule y devuelva el área o el volumen de un cilindro, según
se especifique. Para distinguir un caso de otro, se le pasará como opción un número: 1
(para el área) o 2 (para el volumen). Además, hay que pasarle a la función el radio de la
base y la altura.
 ́𝑎𝑟𝑒𝑎 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜 · (𝑎𝑙𝑡𝑢𝑟𝑎 + 𝑟𝑎𝑑𝑖𝑜)
𝑣𝑜𝑙𝑢𝑚𝑒𝑛 = 𝜋 · 𝑟𝑎𝑑𝑖𝑜2 · 𝑎𝑙𝑡𝑢𝑟𝑎
'''



'''71.
Diseñar una función que recibe como argumentos dos números enteros y devuelve el
máximo de ambos.
'''



'''72.
Crear una función que, mediante un booleano, indique si el carácter que se le pasa como
argumento corresponde a una vocal.
'''



'''73.
Implementar la función definida según la siguiente especificación:
Pre : 𝑛 ≥ 0
    es_primo(𝑛 : int) -> bool
Post : es_primo(𝑛 ) =
    True si n es primo
    False en caso contrario
'''



'''74.
Escribir una función a la que se le pase un número entero y devuelva el número de
divisores primos que tiene
'''



'''75.
Diseñar la función calculadora, a la que se le pasan dos números reales (los operandos)
y qué operación se desea realizar con ellos. Las operaciones disponibles son: sumar,
restar, multiplicar o dividir. Las operaciones se especifican mediante un número: 1
para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. La función
devolverá el resultado de la operación en forma de número real.
Indicación: Los números se codifican las operaciones disponibles se pueden representar
más adecuadamente usando constantes.
'''



'''76.
Diseñar una función que calcule y muestre la superficie y el volumen de una esfera.
𝑠𝑢𝑝𝑒𝑟 𝑓 𝑖𝑐𝑖𝑒 = 4𝜋 · 𝑟𝑎𝑑𝑖𝑜2
𝑣𝑜𝑙𝑢𝑚𝑒𝑛 = 4𝜋
3 · 𝑟𝑎𝑑𝑖𝑜3
'''



'''77.
Implementar la función distancia que, con la siguiente especificación:
Pre : True
es_primo(𝑥1 : float, 𝑦1 : float, 𝑥2 : float, 𝑦2 : float) -> float
Post : es_primo(𝑥1, 𝑦1, 𝑥2, 𝑦2) = la distancia euclídea de
los puntos (𝑥1, 𝑦1) y (𝑥2, 𝑦2)
La fórmula para calcular la distancia euclídea es:
𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑖𝑎 = √︁(𝑥1 − 𝑥2)2 + (𝑦1 − 𝑦2)2
'''



'''78.
Escribir la función numeros_pares que muestre por la consola los n primeros números
pares.
'''



'''79.
Escribir una función a la que se le pase como argumentos una cantidad de días, horas y
minutos. La función calculará y devolverá el número de segundos que existen en los
datos de entrada.
'''



'''80.
Escribir la función divisores_primos que devuelva una lista con todos los divisores
primeros del número entero que se le pasa como argumento.
'''
