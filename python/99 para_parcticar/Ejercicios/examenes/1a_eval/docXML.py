import xml.etree.ElementTree as ET

def shows():
    """[summary]

    Returns:
        [type]: [description]
    """
    raiz = ET.parse('shows.xml').getroot()
    res = {}

    for show in raiz.findall('pelicula'):
        titulo = show.find('titulo').text
        genero = show.find('genero').text
        if genero == 'fantasia':
            res[titulo] = None

    for show in raiz.findall('serie'):
        titulo = show.find('titulo').text
        genero = show.find('genero').text
        if genero == 'fantasia':
            res[titulo] = len(show.findall('.//episodio'))

    return res
