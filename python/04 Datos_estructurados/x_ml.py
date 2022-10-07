import xml.etree.ElementTree as ET

tree = ET.parse('archivo.xml')  # Esto se usa cuando el doc xml es externo al
# codigo

root = tree.getroot()

for n in root:
    print(n.tag, n.attrib)

root[0][1][0]  # Esto devuelve el nodo propio
root[0][1][0].text  # Esto devuelve el texto cntenido en el nodo
root[0][1][0].attrib  # Esto devuelve elk atributo cntenido en el nodo

'''
escribir una funcion que Dado el nombre raiz del arbol que devuelva el nombre de todos los alumnos
del archivo.xml
'''


def nombre_alumnos(arbol):
    raiz = arbol.getroot()
    for alumno in raiz:
        numero = alumno.attrib['numero']  # Accede al valor atraves de la clave
        nom_prop = alumno[1][0].text
        apellido = alumno[1][1].text
        print(f'{numero} {nom_prop} {apellido}')


# Lo suyoes acceder a los datos a traves de las etiquetas
al = root[0]
al.find('nota').text


def nota_media(arbol):
    raiz = arbol.getroot()
    total = 0
    for i, alumno in enumerate(raiz, 1):
        total += float(alumno.find('nota').text)
    return total / i


for n in root.iter('nota'):
    print(n.text)
    # busca desde la raiz los nodos nota, sin acceder al alumno, y las va
    # devolviedo


documento = '''
<?xml version="1.0"?>

<data>
    <alumno numero="999">
        <dni>95632578L<dni>
        <nombre>
            <propio>Pepe Juán</propio>
            <apellidos>Pérez Lozan</apellidos>
        </nombre>
        <telefono>635489210</telefono>
        <nota>7</nota>
    </alumno>
    <alumnoumero="777">
        <dni>45698521L<dni>
        <nombre>
            <propio>María un</propio>
            <apellidos>Paj Ote</apellidos>
        </nombre>
        <telefono>619555648</telefono>
        <nota>10</nota>
    </alumno>
    <padre>
        <dni>49089354M</dni>
        <nombre>Jesucristo Garcia</nombre>
        <num_hijo>2</num_hijo>
    </padre>
</data>
'''

var = ET.fromstring(documento)  # esto se usa cuando el xml está integrado
# en el codigo
print(type(var))

root[0].attrib  # Muestra los atributos
root[0][0].text  # Dni del primer alumno

# Esto devuelve el
list(map(lambda x: x.attrib['numero'], root.findall('alumno')))
# numero de todos los alumnos

root.find('alumno').attrib['numero']
root.find('alumno').get('numero')  # Esto solo se puede hacer
# sobre objetos de tipo element pero no
# sobre listas por eso no se puede usar
# con el findall que devuelve una lista


root.findall('alumno/dni')  # Asi coge los dni de los alumnos del doc

root.findall('*/dni')  # Asi coge TODOS los dni del doc

root.findall('.//dni')  # devuelve Todos los dni en cualquier nivel a
# partir del acctual

# Devuelve todos los nodos hijos del nodo actual
root.finall("alumno[@numero]")
# que tienen ese atributo
root.finall("alumno[@numero='999']")  # Devuelve los nodos hijos del alumno 999
root.finall("*[@numero='999']")  # Esto tambien valdría

root.findall(".//dni/..")  # Los dos puntos representan alumno

# Busca todos los alumnos que tiene dni como hijo
root.findall(".//alumno[dni]")
root.findall(".//alumno/dni/..")  # Esto es practicamente los mismo que lo
# de antes

root.findall('alumno[1]')  # El primer alumno
root.findall('almuno')[0]  # El primer alumno

root.findall('alumno[last()]')  # El último alumno
root.findall('almuno')[-1]  # El último alumno

root.findall('alumno[last() - 1]')  # El penúltimo alumno
root.findall('almuno')[-2]  # El penúltimo alumno

root.find('alumno/dni').text = '2222222L'  # Cambia el dni del primer alumno

root.find('alumno').get('numero')  # Obtienes el valor del atributo
root.find('alumno').set('numero', '111')  # Cambia el valor del atributo numero


madre = ET.Element('madre')  # Crea el nodo madre
madre.tag >> 'madre'
nombre = ET.Element('nombre')
nombre.text = 'Isabel II'  # Ya se ha creado el nodo que contiene el nombre de la madre
madre.append(nombre)  # Agrego el nombre como elemeno hijo de madre
root.append(madre)  # Y asi la madre pasa a ser un nodo del arbol principal
# Con el append() se añaden como ultimo hijo del nodo raiz

# para insertarlo en una posicion intermedia usamos el metodo .insert()
tio = ET.Element('tio')
# El elemento tio es el segundo nodo que aparece en el arbol
root.insert(1, tio)

ET.SubElement(root, 'tia')  # Lo añade por el final

root.remove(padre)  # Hay que localizar el elemeto a eliminar,
# y ha de ser hijo directo del nodo sobre el que aplicas
# el remove

# Lo que pasa es que se pierde la conexion con el nodo padre, pero la info
# sigue existiendo, de esa forma lo puedo posicionar en otro lugar del arbol

tree  # es el arbol

tree.write('nuevo.xml')  # reescribe el archivo
