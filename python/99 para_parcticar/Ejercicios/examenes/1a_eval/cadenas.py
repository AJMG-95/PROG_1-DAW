"""
Crear una funcion que invierte el orden de la cadena compuesta por nombre y
apellido y devuelve la cadena como apellido y nombre
"""
def intercambiar_persona(persona):
    """Invierte el orden de las subcadenas de una cadena compuesta

    Args:
        persona (str): nombre  apellido

    Returns:
        str: apellido, nombre
    """
    return ', '.join(persona.split('  ')[::-1])


"""
persona.index('  ')
persona[:12] # Nombre
persona[14:] # Los apellidos
"""
