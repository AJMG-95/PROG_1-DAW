'''
class Racional:
    """
    Clase Racional
    """
    def __init__(self, num, den):
        """
        Inicializa la instancia al crear un objeto a partir de la clase Racional

        Args:
            num (int): Valor del numerador.
            den (int): Valor del denominador.
        """
        self.num = num
        self.den = den
    def numer(self):
        """
        Accede al valor del numerador del racional.

        Returns:
            int: numerador del racional.
        """
        return self.num
    def denom(self):
        """
        Accede al valor del denominador del racional.

        Returns:
            int: denominador del racional.
        """
        return self.den
    def imprimir(self):
        """
        Imprime por pantalla el racional
        """
        print(self.numer(), '/', self.denom(), sep='')
'''


#! Si se cambia la implementacion de la clase eso no afecta al funcionamiento de los metodos
#!     al llamarlos sobre un objeto instanciado sobre la propia clase

class Racional:
    """
    Clase Racional
    """
    def __init__(self, num, den):
        """
        Inicializa la instancia al crear un objeto a partir de la clase Racional

        Args:
            num (int): Valor del numerador.
            den (int): Valor del denominador.
        """
        self.datos = [num, den]
    def numer(self):
        """
        Accede al valor del numerador del racional.

        Returns:
            int: numerador del racional.
        """
        return self.datos[0]
    def denom(self):
        """
        Accede al valor del denominador del racional.

        Returns:
            int: denominador del racional.
        """
        return self.datos[1]
    def imprimir(self):
        """
        Imprime por pantalla el racional
        """
        print(self.numer(), '/', self.denom(), sep='')
