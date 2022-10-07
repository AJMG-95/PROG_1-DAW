'''101.
Escribir la función:
Pre : True
buscar_todos(𝑙𝑖𝑠𝑡𝑎 : List[int], 𝑐𝑙𝑎𝑣𝑒 : int) -> List[int]
que crea y devuelve una lista con todos los índices de los elementos donde se encuentra
la clave de búsqueda 𝑐𝑙𝑎𝑣𝑒. En el caso de que 𝑐𝑙𝑎𝑣𝑒 no se encuentre en 𝑙𝑖𝑠𝑡𝑎, la función
devolverá una lista vacía.
'''



'''102.
El ayuntamiento de Sanlúcar te ha encargado una aplicación que ayude a realizar
encuestas estadísticas para conocer el nivel adquisitivo de los sanluqueños. Para ello,
tendrás que preguntar el sueldo a cada persona encuestada. A priori, no se conoce el
número de encuestados. Para finalizar la entrada de datos, introduce un sueldo con
valor −1.
Una vez terminada la entrada de datos, muestra la siguiente información:
Todos los sueldos introducidos, ordenados de forma decreciente.
El sueldo máximo y mínimo.
La media de los sueldos.
'''



'''103.
Debes desarrollar una aplicación que ayude a gestionar las notas de un centro educativo.
Los alumnos se organizan en grupos compuestos por 5 personas. Leer las noas (números
enteros) del primer, segundo y tercer trimestres de un grupo. Debes mostrar al final la
nota media del grupo en cada trimestre y la media del alumno que se encuentra en una
posición dada (que el usuario introduce por teclado).
'''



'''104.
En un juego de rol, el mapa puede implementarse como una matriz donde las filas y las
columnas representan lugares (lugar 0, lugar 1, lugar 2, etc.) que estarán conectados. Si
desde el lugar 𝑥 podemos ir hacia el lugar 𝑦, entonces la matriz en la posición [𝑥][𝑦]
valdrá True; en caso contrario, valdrá False.
Escribe una función que, dados dos lugares y una matriz que representa el mapa, indique
si es posible viajar desde el primer lugar al segundo directamente o pasando por
lugares intermedios.

Matriz De Adyacencia: Ejemplo:

    0   1   2   3
    --------------
0|  F   T   T   F
1|  T   F   F   T
2|  F   T   F   F
3|  F   F   F   F

    0   1   2   3           0   1   2   3           0   1   2   3
    --------------        ----------------         ----------------
0|  0   1   1   0       0|  0   1   1   0      0|   1
1|  1   0   0   1   X   1|  1   0   0   1   =  1|
2|  0   1   0   0       2|  0   1   0   0      2|
3|  0   0   0   0       3|  0   0   0   0      3|
'''
MAPA = [[False],[True],[True],[False],
        [True],[False],[False],[True],
        [False],[True],[False],[False],
        [False],[False],[True],[False]]

camino = []

def rol(mapa, ini, fin):
    if mapa[ini][fin]:
        return True

#   adyacentes = []
#   for nodo, valor in enumerate(mapa[ini]):
#       if valor:
#           adyacentes.append(nodo)

    adyacentes = [nodo for nodo, valor in enumerate(mapa[ini]) if valor]

    for nodo in adyacentes:
        if rol(mapa, nodo, fin):
            return True

    return False


def rol_game(mapa, ini, fin, camino):
    camino.append(ini)

    if mapa[ini][fin]:
        camino.append(fin)
        return True

    adyacentes = [nodo for nodo, valor in enumerate(mapa[ini]) \
                        if valor and nodo not in camino]

    for nodo in adyacentes:
        if rol_game(mapa, nodo, fin, camino):
            return True

    return False


'''105.
Escribir la función:
Pre : True
suma(𝑙𝑖𝑠𝑡𝑎 : List[int], 𝑛𝑢𝑚_𝑒𝑙𝑒𝑚 : int) -> List[int]
que crea y devuelve una lista con las sumas de los 𝑛𝑢𝑚_𝑒𝑙𝑒𝑚 elementos consecutivos
de 𝑙𝑖𝑠𝑡𝑎.
Por ejemplo, sea 𝑙𝑖𝑠𝑡𝑎 = [10, 1, 5, 8, 9, 2]. Si los elementos de 𝑙𝑖𝑠𝑡𝑎 se agrupan de
3 en 3, se harán las sumas:
10 + 1 + 5 = 16.
1 + 5 + 8 = 14.
5 + 8 + 9 = 22.
8 + 9 + 2 = 19.
Por lo tanto, la función devolverá la lista [16, 14, 22, 19].
'''



'''106.
Escribir un programa que solicite los elementos de una matriz de tamaño 4 × 4. La
aplicación debe decidir si la matriz introducida corresponde a un cuadrado mágico,
que es aquel en el que la suma de los elementos de cualquier fila, columna, diagonal
principal y diagonal secundaria valen lo mismo.
'''



'''107.
Hacer el mismo programa del ejercicio anterior pero considerando una matriz cuadrada
de cualquier tamaño (𝑁 × 𝑁 ).
108. Introducir por teclado dos frases e indicar cuál de ellas es la más corta, es decir, la que
tiene menos caracteres.
'''



'''109.
Diseñar el juego «acierta la contraseña». La mecánica del juego es la siguiente: el primer
jugador introduce la contraseña sin que la vea el segundo jugador; a continuación, el
segundo jugador debe teclear palabras hasta que la acierte. El programa deberá indicar
en cada intento si la palabra introducida es mayor o menor (alfabéticamente) que la
contraseña.
'''



'''110.
Hacer el mismo programa del ejercicio anterior pero con la siguiente variante: en lugar
de indicar si la palabra es mayor o menor que la contraseña, deberá mostrar la longitud
de la contraseña y una cadena con los caracteres acertados en sus lugares respectivos y
asteriscos en los no acertados.
'''



'''111.
Diseñar un programa que pida al usuario que introduzca una frase por teclado e indique
cuántos espacios en blanco tiene. Hacer dos versiones: una recorriendo la cadena y otra
sin recorrido.
'''



'''112.
Diseñar una función a la que se le pase una cadena de caracteres y la devuelva invertida.
Por ejemplo, la cadena «Hola mundo» quedaría «odnum aloH».
'''



'''113.
Escribir un programa que pida el nombre completo al usuario y lo muestre sin vocales
(mayúsculas, minúsculas y acentuadas). Por ejemplo, «Álvaro Pérez» se mostraría «lvr
Prz».
'''
def problema_113():
    n = input('Introduzca su nombre: ')
    v = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    print(''.join([x for x in n if x not in v and x.lower() != ' ']))

#TODO: Es igual que la anterior pero converte las consonates a minuscula.
def quita_vocales():
    """Pide al ususario un nombre y devuelve las consonates del nombre
    """
    n = input('Introduzca su nombre: ')
    v = 'aeiouáéíóú'
    print(''.join([x for x in n if x.lower() not in v and x.lower() != ' ']))

'''114.
Los habitantes de Pythonlandia tienen un idioma algo extraño: cuando hablan, siempre
comienzan sus frases con «Pythonín, pythonón», para después hacer una pausa más
o menos larga (la pausa se representa mediante espacios en blanco o tabuladores) y a
continuación expresan el mensaje. Existe un dialecto que no comienza sus frases con la
muletilla anterior, pero siempre las terminan con un silencio, más o menos prolongado,
y la coletilla «pythonén, nen, nen». Se pide diseñar un traductor que, en primer lugar,
nos diga si la frase introducida está escrita en el idioma de Pythonlandia (en cualquiera
de sus dialectos) y, en caso afirmativo, nos muestre sólo el mensaje sin muletillas.
'''



'''115.
Introducir por teclado una frase palabra a palabra, y mostrar la frase completa separando
las palabras introducidas con espacios en blanco. Terminar de leer la frase cuando alguna
de las palabras introducidas sea la cadena «fin» esritsa con cualquier combinación de
mayúsculas y minúsculas. La cadena «fin» no aparecerá en la frase final.
'''



'''116.
Escribir un programa que lea una frase del teclado y nos indique si es palíndroma, es
decir, que la frase sea igual leyendo de izquierda a derecha, que de derecha a izquierda,
sin tener en cuenta los espacios ni las tildes. Por ejemplo: «Dábale arroz a la zorra el
abad».
'''



'''117.
Se dispone de las siguientes secuencias de caracteres:
Secuencia 1: e i k m p q r s t u v
Secuencia 2: p v i u m t e r k q s
Con ellas, es posible codificar un texto convirtiendo cada letra de la secuencia 1 en
su correspondiente de la secuencia 2. El resto de los caracteres no se modifican. Las
secuencias se utilizan tanto para codificar mayúsculas como minúsculas, mostrando
siempre la codificación en minúsculas.
Por ejemplo, la palabra «PaquiTo» se codifica como «matqvko».
Escribir un programa que codifique un texto. Para ello, se debe implementar la siguiente
función:
Pre : len(𝑐) = 1
codifica(𝑠𝑒𝑐1 : str, 𝑠𝑒𝑐2 : str, 𝑐 : str) -> str
Post : len(codifica(𝑠𝑒𝑐1, 𝑠𝑒𝑐2, 𝑐)) = 1
que devuelve el carácter 𝑐 codificado según las secuencias 1 y 2 que se le pasan.
'''



'''118.
Un anagrama es una palabra que resulta del cambio del orden de los caracteres de
otra. Ejemplos de anagramas para la palabra roma son: amor, ramo o mora. Escribir un
programa que solicite al usuario dos palabras e indique si son anagramas una de otra.
'''



'''119.
Implementar el juego del anagrama, que consiste en que un jugador escribe una palabra
y el programa muestra un anagrama suyo generado al azar. A continuación, otro jugador
tiene que acertar cuál es el texto original. El programa no debe permitir que el texto
introducido por el primer jugador sea la cadena vacía. Por ejemplo, si el primer jugador
escribe «teclado», el programa muestra como pista un anagrama al azar, digamos,
«etcloda».
'''



'''120.
Modificar el programa anterior para que indique al segundo jugador cuántas letras
coinciden (son iguales y están en la misma posición) entre el texto introducido por él y
el original.
'''
