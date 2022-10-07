import xml.etree.ElementTree as ET

def clinica(arbol, socio, especialidad):
    # Crea el acceso a la raiz
    raiz = arbol.getroot()

    # Crea la variable socio que accede al id de socio
    socio = raiz.find(f'.//socios/socio[@id="{socio}"]')

    # Accede al valor del nodo compañia dentro del nodo padre <socio>
    compania = socio.find('./compania').text

    # Recorre todo el arbol buscando los nodos medico
    for medico in raiz.findall('.//medicos/medico'):
        # Recorre el arbol desde el nodo medico busacando el valor del nodo especialidad
        if medico.find('./especialidad').text == especialidad:
            # Busca el nodo compañia dentro del nodo padre <medico>
            for compania_medico in medico.findall('.//compañias/compania'):
                # Compara los valores de los dos compañia de los socios con los de los medicos
                if compania_medico.text == compania:
                    # Si se cumple la condición crea el nodo cita dentro del nodo socio
                    ET.SubElement(socio, 'cita', {'med': medico.get('id')})
                    return arbol
    return arbol

# Crea el acceso al arbol
arbol = ET.parse('clinica.xml')
