def sumas():
    """Recibe un dlea un archivo de texto llamado «entrada.txt» con un texto formado por
    líneas donde en cada una habrá un númeroocumento de texto con valores numericos uno por
    linea y devuelve la suma.
    """
    acc = 0
    f = open('entrada.txt', 'r')
    t = open('salida.txt', 'w')
    for line in f.readlines():
        t.write(f"{int(line):>3} {int(line) + acc:>9}\n")
        acc += int(line)
    t.write('-------------\n')
    t.write(f"SUMA:{acc:>8}")
    f.close()
    t.close()

def sumas2():
    """Ejercicio 2"""
    with open('entrada.txt') as f:
        entrada = [int(x.split()[0]) for x in f.readlines()]
    res = []
    suma = 0
    for e in entrada:
        suma += e
        res.append(f'{e:4} {suma:9}\n')
    res.append('-' * 14 + '\n')
    res.append(f'SUMA: {suma:8}\n')
    with open('salida.txt', 'w') as f:
        f.writelines(res)


def adn_a_arn(adn):
    """Convierte una cadena de adn en una cadena de arn mensajero

    Args:
        adn (str)): Cadena de adn.

    Returns:
        str: Cadena de arn mensajero.
    """
    d = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
    l = []
    for i in adn:
        if i in d:
            l.append(d[i])
    return ''.join(l)


def adn_a_arn2(adn):
    """Ejercicio 1"""
    codigo = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    return ''.join(codigo[x] for x in adn)

import xml.etree.ElementTree as ET

def agrupar(arbol):
    """Ejercicio 3"""
    raiz = arbol.getroot()
    alumnos = raiz.find('alumnos')
    grupos = ET.SubElement(raiz, 'grupos')
    for alumno in raiz.findall('./alumnos/alumno'):
        nivel = int(alumno.get('edad')) - 5
        grupo = raiz.find(f"./grupos/grupo[@nivel='{nivel}']")
        if grupo is None:
            grupo = ET.SubElement(grupos, 'grupo', {'nivel': str(nivel)})
        grupo.append(alumno)
        alumnos.remove(alumno)
    raiz.remove(alumnos)
    return arbol
