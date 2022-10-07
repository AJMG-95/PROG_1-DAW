'''121.
Escribir un programa que lea del teclado una frase e indique, para cada carácter que
aparece en la frase, cuántas veces aparece. Se consideran iguales las letras mayúsculas
y minúsculas para realizar la cuenta. Por ejemplo:
Frase: En un lugar de La Mancha.
Resultado:
a: 4 veces
c: 1 vez
d: 1 vez
e: 2 veces
'''



'''122.
Realizar el juego del ahorcado. Las reglas del juego son:
a. El jugador A teclea una palabra, sin que el jugador B la vea.
b. Ahora se le muestran tantos guiones como letras tenga la palabra secreta. Por
ejemplo, para «hola» se mostraría «----».
c. El jugador B intentará acertar, letra a letra, la palabra secreta.
d. Cada acierto muestra la letra en su lugar, y las letras no acertadas seguirán ocul-
tas como guiones. Siguiendo con el ejemplo anterior, y suponiendo que se ha
introducido la «o», la «j» y la «a», se mostrará «-o-a».
e. El jugador B sólo tiene 7 intentos.
f. La partida terminará al acertar todas las letras que forman la palabra secreta (gana
el jugador B) o cuando se agoten todos los intentos (gana el jugador A).
'''



'''123.
Escribir un programa que pida un entero por la consola, leyéndolo del teclado, y lo
imprime. Si la cadena introducida por consola no tiene el formato correcto, muestra un
mensaje de error y vuelve a pedirlo.
'''



#! EJERCICIOS DE DOC TXT

'''124.
Escribir un programa que lea un archivo de texto (cuyo nombre lo solicitará por teclado
al usuario) y muestre su contenido por pantalla.
'''
from ast import parse


def lee_txt():
    archivo = input('introduzca el archivo que desea ver: ')
    with open(archivo, 'r') as f:
        print(f.read())

def problema_124():
    nombre = input("Escribe el archivo que quieres abrir y leer: ")
    f = open(f'{nombre}', 'r')
    print(f.read())

'''125.
Crear el archivo de texto «numeros_reales.txt» en el directorio de trabajo actual
que contenga una sola línea de texto con números reales separados por espacios. A
continuación, escribir un programa que abre ese archivo, lea los números que contiene
y calcule la suma y la media aritmética, mostrando los resultados por pantalla.
'''
def numeros_reales_linea_txt():
    l = []
    with open('numeros_reales.txt', 'w') as archivo:
        for i in range(0, 10):
            archivo.write(f'{i} ')
    with open('numeros_reales.txt', 'r') as f:
        for i in f.readline():
            if i not in (' ', '\n'):
                l.append(int(i))
        return f'Suma: {sum(l)}, Media: {sum(l)/len(l)}'

def problema_125():
    numeros = input("Indica el archivo: ")
    lista = []
    f = open(numeros, 'r')
    for i in f.readline():
        if i != " " and i != "\n":
            lista.append(int(i))

    return f"La suma es {sum(lista)} y la media es {round(sum(lista) / len(lista))}"


'''126.
Pedir por teclado el nombre, la edad (un entero) y la estatura en metros (un real) de
un deportista. Si algún dato tiene un formato incorrecto, deberá indicarse. En caso
contrario, se deberá mostrar todos los datos en pantalla.
'''
def edad_altura():
    a = input('Indique el nombre: ')
    try:
        b = int(input('Indique la edad: '))
        c = float(input('Indique la estatura en metros: '))
    except ValueError:
        print('La edad ha de ser de tipo int y la altura de tipo float')
    print(f'Nombre: {a}\n \
          Edad: {b}\n \
          Estatura: {c}')

'''127.
Crear un archivo de texto con una colección de números reales, uno por línea. A
continuación, escribir un programa que:
    a. Abra el archivo para lectura.
    b. Lo lea línea a línea.
    c. Muestre finalmente la suma de todos ellos.
'''
def numeros_reales_txt():
    acc = 0
    with open('coleccion_reales.txt', 'w') as f:
        for i in range(0, 10):
            f.write(f'{i}\n')
    with open('coleccion_reales.txt', 'r') as f:
        for line in f.readlines():
            acc += int(line)
    print(acc)

'''128.
Crear un programa que escriba en un archivo de texto, línea a línea, frases introducidas
por el teclado hasta que se introduzca la cadena «fin».
'''
def escribe_lineas_txt():
    with open('frases.txt', 'w') as f:
        while True:
            frs = input('Introduzca su frase: ')
            if frs not in ('fin', 'Fin'):
                f.write(f'{frs}\n')
            else:
                break

'''129.
Escribir un programa que duplique el contenido de un archivo cuyo nombre se pide al
usuario. El archivo copia tendrá el mismo nombre con el prefijo «copia_de_».
'''
def copy_doc_txt():
    l = []
    n = input('Introduzca el archivo a copiar: ')
    with open(n, 'r') as f:
        for line in f.readlines():
           l.append(line)
    with open(f'copia_d_{n}', 'w') as f:
        for i in l:
            f.write(f'{i}')

'''130.
Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
usará por defecto prueba.txt.
'''
def mostrar_txt():
    n = input('Indique el nombre del archivo que desea leer: ')
    if n == '':
        with open('prueba.txt', 'w') as f:
            f.write('Esto es la opción por defecto (Archivo Prueba.txt)')
        with open('prueba.txt', 'r') as f:
            for line in f.readlines():
                print(line)
    else:
        with open(n, 'r') as f:
            for line in f.readlines():
                print(line)

'''131.
Hacer el mismo ejercicio anterior, pero recogiendo el nombre del archivo desde la línea
de órdenes del sistema operativo. (Indicación: usar sys.argv).
'''
def problema_131():
    import sys
    archivo = sys.argv[1]
    if archivo != "":
        f = open(f"{archivo}", 'r')
        for i in f.readlines():
            print(i)
    else:
        print("Este es el de prueba: ")
        w = open("prueba.txt", 'r')
        for q in w.readlines():
            print(q)

'''132.
Escribir un programa que pida al usuario su nombre y su edad. Esos datos deben
guardarse en el archivo datos.txt. Si ese archivo existe, debe añadirse al final en una
nueva línea, y en caso de no existir, debe crearse.
'''
def nombre_edad_txt():
    l = []
    n = input('Indique su nombre: ')
    m = input('Indique su edad: ')
    l.append(n)
    l.append(m)
    with open('datos.txt', 'a+') as f:
        for i in l:
            f.write(f'{i} ')
        f.write('\n')

'''133.
Escribir un programa que lea dos listas de números enteros no ordenados de sendos
archivos con un número por línea, los reúna en una lista única y los guarde en orden
creciente en un tercer archivo, de nuevo uno por línea.
'''
def combina_archivo_txt():
    l = []
    with open('prueba.txt', 'r') as f:
        for line in f.readlines():
            l.append(line)
    with open('prueba2.txt', 'r') as a:
        for line in a.readlines():
            l.append(line)
    l.sort()
    with open('nuevo.txt', 'w') as n:
        for i in l:
            n.write(f'{i}')


'''134.
Escribir un programa que lea un archivo de texto llamado carta.txt. Tenemos que
contar los caracteres, las líneas y las palabras. Para simplificar, supondremos que cada
palabra está separada de otra por un único espacio en blanco o por un salto de línea.
'''
def cuenta_line_caract_txt():
    c, l = 0, 0
    p = []
    with open('carta.txt', 'r') as f:
        for _ in f.readlines():
            l += 1
    with open('carta.txt', 'r') as f:
        for caracter in f.readlines():
            if caracter != ' ':
                c += len(caracter)
    with open('carta.txt', 'r') as f:
        for palabra in f.readlines():
            p += palabra.split()
    print(c, len(p), l)

def problema_134():
    f = open('carta.txt', 'r')
    cont_lineas = 0
    cont_caracteres = 0
    lista = []
    for _ in f.readlines():
        cont_lineas += 1
    print(cont_lineas)
    f = open("carta.txt", 'r')
    for w in f.readlines():
        if w != " ":
            cont_caracteres += len(w)
    print(cont_caracteres)
    f = open("carta.txt", 'r')
    for q in f.readlines():
        lista += q.split()
    print(len(lista))

'''135.
En el archivo numeros.txt disponemos de una serie de números (uno por línea). Diseñar
un programa que procese el archivo y nos muestre el menor y el mayor.
'''
def problema_135():
    l = []
    with open('numeros.txt', 'r') as f:
        for line in f.readlines():
            l.append(int(line))
    print(f'El menor es: {min(l)}.', f'\nEl mayor es: {max(l)}.')

'''136.
Un libro de firmas es útil para recoger los nombres de todas las personas que han pasado
por un determinado lugar. Escribir un programa que permita mostrar el libro de firmas
e insertar un nuevo nombre (comprobando que no se encuentre repetido). El archivo se
deberá llamar firmas.txt.
'''
def lista_asistentes_txt():
    l = []
    n = input('Indique su nombre: ')
    with open('firmas.txt', 'r') as f:
        for line in f.readlines():
            l.append(line)
    if f'{n}\n' not in l:
        with open('firmas.txt', 'a') as f:
            f.write(f'{n}\n')

'''137.
En los sistemas Unix (como GNU/Linux) disponemos del comando more, al que se le
pasa un archivo y nos lo muestra poco a poco, cada 24 líneas. Implementar un programa
que funcione de forma similar.
'''
def mostrar_n_lineas_txt():
    archivo = input("Inserte el archivo que quieras ver: ")
    f = open(archivo, 'r')
    dato = "more"
    texto = ""
    while dato == "more":
        for i in f.readlines(24):
            texto += i
        print(texto)
        dato = input("Quiere ver más?: ")

'''138.
Escribir la función:
    Pre : True
    lee_enteros(𝑡𝑒𝑥𝑡𝑜 : str) -> List[int]
a la que se le pasa una cadena y devuelve una lista con todos los enteros que aparecen
en ella.
'''
def lee_enteros(cadena):
    c = '0123456789'
    return [int(x) for x in cadena if x in c]

def problema_138():
    lista = []
    cadena = input("Dime una cadena de numeros: ")
    for i in cadena:
        if i.isdigit():
            lista.append(int(i))
    print(lista)


#! EJERCIIOS XML
import xml.etree.ElementTree as ET
'''139.
Dado un documento XML similar a éste (es decir, con la misma estructura pero no
necesariamente con el mismo contenido) y almacenado en el archivo club.xml:
escribir un programa que muestre los socios del club de forma similar a la siguiente:
    [1] Sherlock Holmes
    [51] Winston Churchill
'''
def obten_socio():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()

    for socio in raiz.iter('socio'):
        nombre = socio.find('nombre').text
        id_soc = socio.get('id')
        print([int(id_soc)], nombre)

'''140.
Dado el documento XML del ejercicio anterior, escribir un programa que cuente cuántos
socios tiene el club y lo muestre por pantalla.
'''
def problema_140():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    cont = 0
    for _ in raiz.iter('socio'):
        cont += 1
    print(cont)

'''141.
Dado el documento XML del ejercicio anterior, escribir un programa que cambie la
dirección de todos los socios por «Avda. de Huelva, s/n» y guarde los cambios en el
mismo archivo.
'''
def problema_141():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    for direccion in raiz.iter("direccion"):
        direccion.text = 'Avda. de Huelva, s/n'
    arbol.write('club.xml')


'''142.
Dado el documento XML del ejercicio anterior, escribir un programa que cambie la
dirección del socio cuyo id sea 1 por «Calle Ancha, 35» y guarde los cambios en el
mismo archivo.
'''
def problema_142():
    import xml.etree.ElementTree as ET
    tree = ET. parse('club.xml')
    root = tree.getroot()
    direccion = root.find('./socios/socio[@id = "1"]/direccion')
    direccion.text = 'Calle Ancha, 35'
    tree.write('club.xml')
    ET.dump(tree)

'''143.
Dado el documento XML del ejercicio anterior, escribir un programa que elimine al
socio cuyo id sea 51 y guarde los cambios en el mismo archivo.
'''
def elimina_elemento():
    import xml.etree.ElementTree as ET
    tree = ET.parse('club.xml')
    root = tree.getroot()
    socios = root.find('./socios')
    socio_51 = root.find('./socios/socio[@id = "51"]')
    socios.remove(socio_51)
    tree.write('club.xml')
    ET.dump(tree)


def problema_143():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()

    for elemento in raiz.findall("socios/socio"):
        socio_id = elemento.get("id")
        if socio_id == "51":
            raiz.find("socios").remove(elemento)
        arbol.write("club.xml")

'''144.
Dado el documento XML del ejercicio anterior, escribir un programa que añada
el teléfono del socio cuyo id sea 1 creándole al socio un nodo hijo que sea
<telefono>666555444</telefono> y guarde los cambios en el mismo archivo.
'''
def añade_nodo():
    import xml.etree.ElementTree as ET
    tree = ET.parse('club.xml')
    root = tree.getroot()
    socio_1 = root.find('./socios/socio[@id = "1"]')
    ET.SubElement(socio_1, 'telefono')
    telefono = root.find('./socios/socio[@id = "1"]/telefono')
    telefono.text = '666555444'
    tree.write('club.xml')
    ET.dump(tree)

def problema_144():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    telefono = ET.Element('telefono')
    telefono.text = "666555444"
    for elemento in raiz.findall("socios/socio"):
        socio_id = elemento.get("id")
        if socio_id == "1":
            elemento.append(telefono)
    arbol.write("club.xml")

'''145.
Dado el documento XML del ejercicio anterior, escribir un programa que muestre el
nombre de los socios por orden cronológico según su fecha de alta, de más antiguo a
más reciente.
'''
def orden_socio():
    import xml.etree.ElementTree as ET
    tree = ET.parse('club copy.xml')
    root = tree.getroot()
    for socio in root.iter('socio'):
        fecha = socio.find('./alta').text
        print(fecha)
        #! TERMINAR


def ejercicio_145():
    import xml.etree.ElementTree as ET
    tree = ET.parse('club copy.xml')
    root = tree.getroot()
    dic = {}

    for socio in root.findall('./socios/socio'):
        nombre = socio.find('nombre').text
        fecha = socio.find('./alta').text
        dic[fecha] = nombre

    for fecha in sorted(dic):
        print(dic[fecha])

def ejer_145():
    import xml.etree.ElementTree as ET
    tree = ET.parse('club copy.xml')
    root = tree.getroot()
    lista = []

    for socio in root.findall('./socios/socio'):
        nombre = socio.find('nombre').text
        fecha = socio.find('./alta').text
        lista.append((fecha, nombre))

    sorted(lista, key=lambda t: t[0])
    sorted(lista, key=lambda t: t[1])
