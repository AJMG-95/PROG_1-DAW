'''1
    Escribir un programa que juegue con el usuario a que éste tiene que
    adivinar un número del 0 al 99.

    El programa debe «pensar» un número de forma aleatoria usando la
    función random.randint().

    A continuación, debe pedir al usuario que introduzca un numero diciendo
    «Introduce un número: » (cuidado con los espacios).

        · Si el número es el que había pensado, debe decir «¡Acertaste!»
        y finalizar el programa.
        · Si el número es menor que el que había pensado, debe decir
        «Es demasiado pequeño.» y pedir de nuevo otro número.
        · Si el número es mayor que el que había pensado, debe decir
        «Es demasiado grande.» y pedir de nuevo otro número.

        Test:
        >>> 49
        Introduce un número: 49
        ¡Acertaste!
'''
import random

def adivinar_numero():
    """Juego de adivinar un número aleatorio
    """
    rand = random.randint(0, 99)
    num = int(input('Introduce un número: '))
    while True:
        if num == rand:
            print('¡Acertaste!')
            break
        if num < rand:
            print('Es demasiado pequeño.')
        elif num > rand:
            print('Es demasiado grande.')
        num = int(input('Introduce un número:'))

'''2
    Escribir una función escribir_fecha() que,
    aplicado a los datos 'D', 18, 9 y 60, dé lo siguiente:

    Domingo, 18 de septiembre de 1960

        Test:
        >>> print(escribir_fecha('D', 18, 9, 60))
        Domingo, 18 de septiembre de 1960
        >>> print(escribir_fecha('V', 14, 5, 99))
        Viernes, 14 de mayo de 1999
        >>> print(escribir_fecha('X', 29, 7, 44))
        Miércoles, 29 de julio de 1944
'''
dia = {
    'L': 'Lunes', 'M': 'Martes', 'X': 'Miércoles', 'J': 'Jueves',
    'V': 'Viernes', 'S': 'Sábado', 'D': 'Domingo'
}
mes = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
    7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre',
    12:'diciembre'
}
def escribir_fecha(D, d, m, a):
    """Da formato a la fecha indicada.

    Args:
        D (str): Nombre del día
        d (int): Día
        m (int): Mes
        a (int): Año

    Returns:
        str: Fecha formateada
    """
    DD = str(dia.get(D))
    dd = str(d)
    mm = str(mes.get(m))
    aa = str(a + 1900)
    de = ' de '
    fecha = DD + ', ' + dd + de + mm + de + aa
    return fecha

'''3
    Escribir una función leibnitz() que calcule una aproximación de π

    usando la fórmula de Leibnitz:

    π/4 =1 - 1/3 + 1/5 - 1/7 + ⋯

    hasta que se haya incluido un término menor que ϵ = 10^-4
    en valor absoluto.
'''


'''4
    Escribir una función vieta() que calcule una aproximación de π

    usando la fórmula de Vieta:

    π/2 = 2/√2 * 2/√(2√2) * 2/√(2√(2√2)) * ⋯

    hasta que se haya incluido un término menor que ϵ = 1 + 10^-5
'''


'''5
    Escribir una función wallis() que calcule una aproximación de π

    usando la fórmula de Wallis:

    π/2 = 2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * 8/7 * 8/9 * ⋯

    multiplicando los 5000 primeros factores.
'''


'''6
    Escribir una función hamming() que calcule la distancia Hamming
    entre dos cadenas,

    La distancia Hamming entre dos cadenas se calcula comparando las
    dos cadenas y contando cuántos de sus caracteres son distintos a los
    de sus equivalentes en la otra cadena:

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

    La distancia Hamming entre esas dos cadenas de es 7.
    Importante: sólo se puede calcular la distancia Hamming entre dos
    cadenas de igual longitud.

        test:
        >>> print(hamming('A', 'A'))
        0
        >>> print(hamming('A', 'C'))
        1
        >>> print(hamming('AG', 'CT'))
        2
        >>> print(hamming('GGACG', 'GGTCG'))
        1
'''


'''7
    Escribir una función isograma() que determine si una palabra o frase
    es un isograma.

    Un isograma es una palabra o frase que no tiene ninguna letra repetida.

    Ejemplos de isogramas:

        camino
        campeón
        mutación

    La función debe devolver True si la cadena introducida es un isograma,
    o False en caso contrario.

    Importante: Los espacios en blanco se ignoran, y la función no debe
    distinguir las letras mayúsculas de las minúsculas.

        Test:
        >>> print(isograma('camino'))
        True
        >>> print(isograma('manolo'))
        False
        >>> print(isograma('Ricardo'))
        False
        >>> print(isograma('a b c'))
        True
'''


'''8
    Escribir una función palindromo() que determine si una cadena
    es un palíndromo.

    Un palíndromo es una cadena (palabra o expresión) que es igual si se
    lee de izquierda a derecha que de derecha a izquierda.

    Por ejemplo: «Amar da drama».

    La función debe ignorar los caracteres no alfabéticos y no debe
    distinguir las mayúsculas de las minúsculas.

    Test:
    >>> print(palindromo('Amar da drama.'))
    True
    >>> print(palindromo('Hola, qué tal'))
    False
'''


'''9
    Escribir una función pasa_pasa() que manipule dos números enteros suprimiendo
    la última cifra del primero y añadiéndola al final del segundo.

    Usando esa función, escribir la función invierte() que invierte un número
    (partiendo del propio número y de otro con valor inicial cero) a base de
    repetir la operación pasa_pasa() cuantas veces sea necesario.

    Ambas funciones deben recibir como argumento una lista llamada numeros con
    los dos números sobre los que operan y deben cambiar dicha lista.

    Además, la función invierte() debe mostrar cada paso del proceso, de la
    siguiente manera:

    [12345, 0]
    [1234, 5]
    [123, 54]
    [12, 543]
    [1, 5432]
    [0, 54321]

        Test:
        >>> numeros = [1234, 5]
            pasa_pasa(numeros)
            print(numeros)
            numeros = [12345, 0]
            invierte(numeros)
            print(numeros)
        [123, 54]
        [12345, 0]
        [1234, 5]
        [123, 54]
        [12, 543]
        [1, 5432]
        [0, 54321]
        [0, 54321]
'''
