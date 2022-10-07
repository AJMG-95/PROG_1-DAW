'''41.
    Escribir un programa que muestre, para cada número introducido por teclado, si es par,
    si es positivo y su cuadrado. El proceso se repetirá hasta que se introduzca un 0.
'''
def num_caract():
    """
    Pide un número al usuario e indica si es par o impar, positivo o negativo y su cuadrado.
    Para detener el progrma se debe introducir 0.
    """
    try:
        i = True
        while i:
            num = int(input('Introduzca un número: '))
            if num == 0:
                i = False
            if num % 2 == 0:
                print('Es par.')
            else:
                print('Es impar.')
            if num > 0:
                print('Es positivo')
            else:
                print('Es negativo')
            print(f'El cuadrado de {num} es {num ** 2}')
    except ValueError:
        print('Debe introducir un valor numérico.')

'''42.
    Escribir un programa para calcular datos estadísticos de las edades de los alumnos de
    un centro educativo. Se introducirán datos hasta que uno de ellos sea negativo, y se
    mostrará: la suma de todas las edades introducidas, la media, el número de alumnos y
    cuántos son mayores de edad.
'''
def estad_edad():
    """
    Solicita al ususario las edades del alumnado y calcula la suma, la media y
    el número de alumnos mayores de edad.
    El programa se detiene al introducir un valor negativo.
    """
    cont = 0
    suma = 0
    num = 0
    try:
        while True:
            edad = int(input('Introduzca la edad del alumno: '))
            if edad > 0:
                cont += 1
                suma += edad
                media = suma // cont
                if edad >= 18:
                    num += 1
            else:
                print()
                print(f'Suma = {suma}, Media = {media}, Alumnos mayores de edad = {num} ')
                print()
                break

    except ValueError:
        print('Debe introducir un valor numérico entero.')

'''43.
    Codificar el juego «el número secreto», que consiste en acertar un número entre 1 y 100
    (generado automáticamente). Para ello se introduce por teclado una serie de números,
    para los que se indica: «mayor» o «menor», según sea mayor o menor con respecto
    al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde
    (introduciendo un -1).
'''
from random import randint

def numero_secreto():
    """
    Genera un valor numérico aleatorio y piede al usuario que introduzca un número indicale si
    ha acertado o no.
    Si el jugador ha acertado o introduce el valor -1 se termina el juego.
    """
    r = randint(1, 100)
    while True:
        n = int(input('Introduzca un número: '))
        if n == -1:
            break
        if n == r:
            print('¡Acertaste!')
            break
        if n < r:
            print('El número es mayor.')
        elif n > r:
            print('El número es menor.')
        print()

'''44.
    Un centro de investigación de la flora urbana necesita una aplicación que muestre cuál
    es el árbol más alto. Para ello, se introducirá por teclado la altura (en centímetros) de
    cada árbol (terminando la introducción de datos cuando se utilice -1 como altura). Los
    árboles se identifican mediante etiquetas con números únicos correlativos, comenzando
    en 0. Escribir un programa que resuelva el problema planteado.
'''
def arboles():
    """Pide al ususario valores de tipo entero hasta que se introduce
    el valor -1 que detiene el programa.

    Raises:
    ValueError: Valores enteros.

    Returns:
        dic: id(clave) y valor, del valor más alto introducido.
    """
    arboles = {}
    cont = 0
    try:
        while True:
            altura = int(input('Introduzca la alura del arbol: '))
            if altura == -1:
                print()
                clave = max(arboles, key=arboles.get)
                valor = max(arboles.values())
                return {clave:valor}
            arboles[cont] = altura
            cont += 1

    except ValueError:
        print('Se ha de introducir la altura en centimetros (Valores enteros)')

def problema_44():
    """Pide al ususario valores de tipo entero hasta que se introduce
    el valor -1 que detiene el programa.

     Raises:
            ValueError: Valores enteros.

    Returns:
        dic: id(clave) y valor, del valor más alto introducido.
    """
    arboles = {}
    cont = 0
    try:
        while True:
            altura = int(input('Introduzca la alura del arbol: '))
            if altura == -1:
                print()
                for key, value in arboles.items():
                    if value == max(arboles.values()):
                        return {key:value}
            arboles[cont] = altura
            cont += 1

    except ValueError:
        print('Se ha de introducir la altura en centimetros (Valores enteros)')

'''45.
    Desarrollar un juego que ayude a mejorar el cálculo mental de la suma. El jugador
    tendrá que introducir la solución de la suma de dos números aleatorios comprendidos
    entre 1 y 100. Mientras la solución introducida sea correcta, el juego continuará. En
    caso contrario, el programa terminará y mostrará el número de operaciones realizadas
    correctamente.

'''
from random import randint

def aprende_suma():
    """Genera la suma de dos números aleatores entre 1 y 100
        Pide al usuario que introduzca la solución a las suma, si éste falla se
        detiene el programa e indica el número de aciertos.

    Raises:
        ValueError: Valores de tipo entero
    """
    cont = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        sol = a + b
        try:
            num = int(input(f'Introduce la solución al problema ({a} + {b}): '))
            cont += 1
            if num != sol:
                cont -= 1
                print(f'Ha realizado {cont} operaciones correctamente.')
                break
        except ValueError:
            break


'''46.
Escribir un programa para aprender a contar, que pedirá un número n y mostrará todos
los números del 1 al n.
'''
def aprende_contar():
    """Pide al ausuario un entero y muestra los valores conprendidos entre 1
    y el entero indicado.
    """
    n = int(input('Introduce un número de tipo entero: '))
    print(range(1, n + 1))

'''47.
Escribir todos los múltiplos de 7 menores que 100.
'''
def multiplos7():
    """Vuelca por pantalla todos los multiplos de 7 menores de 100.
    """
    for i in range(1, 100):
        sol = 7 * i
        if sol >= 100:
            break
        print(f'7 x {i} = {sol}')

'''48.
Pedir diez números enteros por teclado y mostrar la media.
'''
def media():
    """Pide al usuario un total de 10 números de tipo enterp y calcula la media aritmética.

    Returns:
        float: Media aritmetica.
    """
    con = 0
    aux = 0
    while con < 10:
        num = int(input('Intorduce un número de tipo entero: '))
        con += 1
        aux += num
    return aux / 10

def problema_48():
    """Pide al usuario un total de 10 números de tipo enterp y calcula la media aritmética.

    Returns:
        float: Media aritmetica.
    """
    cont = 0
    lista = []
    while cont != 10:
        numero = int(input("Introduce un número: "))
        lista.append(numero)
        cont += 1
    return sum(lista)/cont

'''49.
Implementar un programa que pida al usuario un número comprendido entre 1 y 10. Hay
que mostrar la tabla de multiplicar de dicho número, asegurándose de que el número
introducido se encuentra en el rango establecido.
'''
def tabla_mult():
    """Pide al usuario un número de tipo entero y muestra la tabla de multiplicar de dicho número.
    """
    n = int(input('Introduce un entero comprendido entre 0 y 10: '))
    cont = 1
    if n in range(1, 11):
        while cont in range(1, 11):
            res = n * cont
            print(f'{n} * {cont} = {res}')
            cont += 1

'''50.
Diseñar un programa que muestre las tablas de multiplicar del 1 al 10.
'''
def tablas_multiplicar():
    """Muestra las tablas de multiplicar del 1 al 10.
    """
    for i in range(0, 11):
        print(f'TABLA DEL {i}:')
        print('-------------')
        for x in range(0, 11):
            print (f"{i} x {x} = {i * x}")
        print()

'''51.
Diseñar un programa que muestre la suma de los 10 primeros números impares.
'''
def suma_impar():
    """Muestra la suma de los 10 primeros números impares dentro de la totalidad
    de los reales.
    """
    l = []
    cont = 0
    n = 1
    while True:
        if n % 2 != 0:
            l.append(n)
            cont += 1
        if cont == 10:
            print(f'{l}')
            print(sum(l))
        n += 1

'''52.
Pedir un número y calcular su factorial.
'''
def fact():
    """Pide al ususario un número entero y calcula su factorial

    Returns:
        int: Factorial de n
    """
    n = int(input('Introduza el número del que desee saber su factorial: '))
    acc = 1
    if n == 0:
        return acc
    for i in range(1, n + 1):
        acc *= i
    return acc

'''53.
Pedir 5 calificaciones de alumnos y decir al final si hay algún suspenso.
'''
def calificacion():
    """Pide 5 calificaciones de alumnos y al final dice si hay algún suspenso.
    """
    cont = 0
    sus = 0
    while cont < 5:
        n = float(input(f'Intorduce la calificancion del alumno: '))
        if n < 5:
            sus += 1
        cont += 1
    if sus > 0:
        print(f'Hay algún alumno/s suspenso')

'''54.
Dadas 6 notas, escribir la cantidad de alumnos aprobados, condicionados
(nota igual a 4) y suspensos.
'''
def n_suspenso():
    """Pide 5 calificaciones de alumnos y al final dice cuantos suspenso hay.
    """
    cont = 0
    sus = 0
    while cont < 5:
        n = float(input(f'Intorduce la calificancion del alumno: '))
        if n < 5:
            sus += 1
        cont += 1
    print(f'Hay {sus} alumnos suspensos')

'''55.
Pedir por consola un número n y dibujar un triángulo rectángulo de n elementos de
lado, utilizando para ello asteriscos (*). Por ejemplo, para 𝑛 = 4:
* * * *
* * *
* *
*
'''
def triangulo():
    """Dijuja en pantalla un trianguilo rectangulo de ancho n usando '*' para ello.
    """
    n = int(input('Indique el ancho del triangulo: '))
    m = n
    while m != 0:
        for _ in range(n):
            print(n * "* ")
            n -= 1
        m -= 1

def problema_55():
    """Dijuja en pantalla un trianguilo rectangulo de ancho n usando '*' para ello.
    """
    numero = int(input("Dime cuantas estrellitas kieres: "))
    for i in range(numero, 0, -1):
        print(i * "*")

'''56.
Escribir un programa que convierta un número decimal en su representación binaria.
Hay que tener en cuenta que desconocemos cuántas cifras tiene el número que introduce
el usuario.
'''
def dec2bin():
    """
    Pide al usuario un número 'n' en base decimal y lo pasa a binario.

    Pre:
        El valor indicado por ekl ususario ha de ser numérico de tipo entero.

    Returns:
        int: Valor de 'n' en binario.
    """
    n = int(input('Indique un número decimal: '))
    l = []
    while n != 0:
        l.insert(0, str(n % 2))
        n //= 2
    return int(''.join(l))

def problema_56():
    """Pide al usuario un numero decimal, lo pasa a bianrio y vuelca el resultado por pantalla
    """
    numero = int(input("Dime un número decimal si kieres: "))
    binarios = []
    resto = 0
    while numero != 0:
        resto = numero % 2
        numero = numero // 2
        binarios.append(str(resto))
    alreve = binarios[::-1]
    print("".join(alreve))

'''57.
Escribir un programa que convierta un número binario en su representación decimal.
'''
def problema_58():
    """Pide al usuario un número binario y devuelve el número en forma decimal

    Pre:
        Los caracteres introducidos han de ser 0's o 1's

    Returns:
        int: Forma decimal del número introducido
    """
    cont = 0
    solucion = 0
    numero = input("Escribeme un número en binario: ")
    cont = len(numero)
    for i in str(numero):
        cont -= 1
        solucion +=  int(i) * (2 ** cont)
    return solucion

def bin2dec():
    """Pide al usuario un número binario y devuelve el número en forma decimal

    Pre:
        Los caracteres introducidos han de ser 0's o 1's

    Returns:
        int: Forma decimal del número introducido
    """
    n = input('Introduce un número binario: ')
    l = []
    p = 0
    for x in n[::-1]:
        l.append(int(x) * 2 ** p)
        p+= 1
    return sum(l)

def binario_a_decimal():
    """Pide al usuario un número binario y devuelve el número en forma decimal

    Pre:
        Los caracteres introducidos han de ser 0's o 1's

    Returns:
        int: Forma decimal del número introducido
    """
    n_bin = input('Introduce un número binario: ')
    n_dec = 0
    for posicon, digito in enumerate(n_bin[::-1]):
        n_dec += int(digito) * 2 ** posicon
    return n_dec

'''58.
Escribir un programa que incremente la hora de un reloj. Se pedirán por teclado la hora,
minutos y segundos, así como cuántos segundos se desea incrementar la hora introdu-
cida. El programa mostrará la nueva hora. Por ejempo, si las 13:59:51 se incrementan
en 10 segundos, resultan las 14:00:01.
'''
def icrementa_hora():
    """Pide al ususario introducir horas, minutos, segundos y los segundos de incremento
    que le quiere aplicar.

    Vuelca por pantalla la hora actualizada, con el incremento aplicado.
    """
    hms = ['las horas', 'los minutos', 'los segundos']
    l = []
    for i in hms:
        r = int(input(f'Introduce el valor de {i}:'))
        l.append(r)
    i = int(input('Indique el incremento en segundos: '))
    h = l[0] * 3600
    m = l[1] * 60
    s = l[2] + h + m + i
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    print(f'{h}:{m}:{s}')

'''59.
Escribe un programa que nos pida un número n y nos diga cuántos números primos
hay entre 1 y n.
Por ejemplo, para 𝑛 = 8, comprobamos todos los números del 1 al 8: 1 → primo ; 2 →
primo ; 3 → primo ; 4 → no primo ; 5 → primo ; 6 → no primo ; 7 → primo ; 8 → no
primo
'''
def primo():
    """Pide al ususario un número 'n' y devuelve los números primos comprendidos entre 1 y 'n', iclusive.

    Pre:
        El valor indicado ha de ser nmñerico de tipo entero.

    Returns:
        list: Lista de números primos.
    """
    numero = int(input("Escribe un numero: "))
    l = ['Números Primos:']
    def primos(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    for n in range(1, numero + 1):
        if primos(n):
            l.append(n)
    return l

def problema_60():
    """Pide al ususario un número 'n' y devuelve los números primos comprendidos entre 1 y 'n', iclusive.

    Pre:
        El valor indicado ha de ser nmñerico de tipo entero.
    """
    numero = int(input("Escribe un numero: "))
    def primos(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    for j in range(1, numero + 1):
        if primos(j):
            print(f"El numero {j} es primo")
        else:
            print(f"El número {j} no es primo ")

'''60.
Diseña un programa que dibuje el triángulo de Pascal (también llamado de Tartaglia),
para n filas. Numerando las filas y elementos desde 0, la fórmula para obtener el m-ésimo
elemento de la n-ésima fila es:
𝐸 (𝑛, 𝑚) = 𝑛!
𝑚!(𝑛 − 𝑚)!
Un ejemplo de triángulo de Pascal con 5 filas (𝑛 = 4) es:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
def lista_sobre_A(ultima_fila):
    res = [[1]]
    if ultima_fila == 0:
        return res
    for _ in range(ultima_fila):
        f1 = [0] + res[-1]
        f2 = res[-1] + [0]
        fila = []
        for i, f in enumerate(f1):
            fila.append(f2[i] + f)
        res.append(fila)
    return res


def triangulo_A(numeros_filas):
    for fila in lista_sobre_A(numeros_filas - 1):
        for i, f in enumerate(fila):
            fila[i] = f' {f:5}'
        print(''.join(fila).center(60))
