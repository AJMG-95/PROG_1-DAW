"""Lampara (3Pts)
Programar en Python un modelo orientado a objetos del funcionamiento de una lámpara. Para ello, se deberán crear, al menos, las clases Lampara y Bombilla.

Las lámparas pueden tener uno o varios casquillos, en cada uno de los cuales puede ir una bombilla.
Cada casquillo tiene un tamaño, que puede ser pequeño o mediano.
Cada bombilla tiene una determinada potencia (medida en vatios) y un tamaño.
Cada lámpara está diseñada para soportar una potencia máxima en vatios, por lo que la suma de las potencias de todas las bombillas que tenga colocadas no debe superar esa potencia máxima.
El constructor de la clase Bombilla recibe la potencia (medida en vatios, un número real) y el tamaño de la bombilla (que puede ser 'P' para pequeño o 'M' para mediano). Esos valores son inmutables.

La clase Bombilla deberá contar, al menos, con los siguientes métodos:

potencia(): devuelve la potencia de la bombilla en vatios.
tamanyo(): devuelve el tamaño de la bombilla.
El constructor de la clase Lampara recibe el número de casquillos pequeños y el número de casquillos medianos que tiene, así como la potencia máxima que admite. Todos esos valores son inmutables.

La clase Lampara deberá contar, al menos, con los siguientes métodos:

poner(bombilla): pone una bombilla en la lámpara, en alguno de los casquillos que haya libres y que sea del mismo tamaño que la bombilla. De no haber ningún casquillo adecuado libre, o si al poner la nueva bombilla se supera la potencia máxima permitida en la lámpara, el método no hará nada. Devuelve el objeto lámpara.
quitar(tamaño): quita una bombilla cualquiera de la lámpara con el tamaño indicado, y la devuelve. En caso de no haber ninguna de ese tamaño, devolverá None.
potencia_total(): devuelve la potencia total consumida por la lámpara en vatios, calculada con la suma de las potencias de cada bombilla puesta en la lámpara.

TEST:
print(Lampara(3, 0, 20).poner(Bombilla(10, 'P')).potencia_total()) # 10
print(Lampara(3, 0, 20).poner(Bombilla(10, 'M')).potencia_total()) # 0
print(Lampara(3, 2, 20).poner(Bombilla(10, 'P')).poner(Bombilla(10, 'M')).quitar('M').tamanyo()) # "M"

"""


class Bombilla:
    """Define la clase bombilla. Esta clase contiene los atributos potencia y tamanyo, que son inmutables."""

    def __init__(self, potencia, tamanyo):
        """Constructor de la clase bombilla."""
        self._potencia = potencia
        self._tamanyo = tamanyo

    def potencia(self):
        """Devuelve la potencia de la bombilla en vatios."""
        return self._potencia

    def tamanyo(self):
        """Devuelve el tamaño de la bombilla."""
        return self._tamanyo


class Lampara:
    """Define la clase lampara."""

    def __init__(self, peque, medio, potencia):
        """Constructor de la clase lampara."""
        self.peque = peque
        self.medio = medio
        self._potencia = potencia
        self.bombillas = []

    def poner(self, bombilla):
        """Pone una bombilla en la lámpara, en alguno de los casquillos que haya libres y que sea del mismo tamaño que la bombilla."""
        if self.potencia_total() + bombilla.potencia() <= self._potencia:
            if bombilla.tamanyo() == 'P':
                if self.peque > 0:
                    self.bombillas.append(bombilla)
                    self.peque -= 1
            elif bombilla.tamanyo() == 'M':
                if self.medio > 0:
                    self.bombillas.append(bombilla)
                    self.medio -= 1
        return self

    def quitar(self, tamanyo):
        """Quita una bombilla cualquiera de la lámpara con el tamaño indicado, y la devuelve (el objeto).
        Si no existe ninguna bombilla, este método devolverá None."""
        if tamanyo == 'P':
            if self.peque > 0:
                self.peque += 1
                return self.bombillas.pop()
        elif tamanyo == 'M':
            if self.medio > 0:
                self.medio += 1
                return self.bombillas.pop()
        return None

    def potencia_total(self):
        """Devuelve la potencia total consumida por la lámpara en vatios, calculada con la suma de las potencias de cada bombilla puesta en la lámpara."""
        total_vatios = 0
        for bombilla in self.bombillas:
            total_vatios += bombilla.potencia()
        return total_vatios
