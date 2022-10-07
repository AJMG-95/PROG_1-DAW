"""Lamparas y Bombillas (P = 3 puntos)
  Programar en Python un modelo orientado a objetos del funcionamiento de una lámpara.
  Para ello, se deberán crear, al menos, las clases Lampara y Bombilla.

  Las lámparas pueden tener uno o varios casquillos, en cada uno de los cuales puede
    ir una bombilla.
  Cada casquillo tiene un tamaño, que puede ser pequeño o mediano.
  Cada bombilla tiene una determinada potencia (medida en vatios) y un tamaño.
  Cada lámpara está diseñada para soportar una potencia máxima en vatios,
    por lo que la suma de las potencias de todas las bombillas que tenga colocadas
    no debe superar esa potencia máxima.
  El constructor de la clase Bombilla recibe la potencia (medida en vatios, un número real)
    y el tamaño de la bombilla (que puede ser 'P' para pequeño o 'M' para mediano).
    Esos valores son inmutables.

  La clase Bombilla deberá contar, al menos, con los siguientes métodos:

  potencia(): devuelve la potencia de la bombilla en vatios.
  tamanyo(): devuelve el tamaño de la bombilla.

  El constructor de la clase Lampara recibe el número de casquillos pequeños y
    el número de casquillos medianos que tiene, así como la potencia máxima que
    admite. Todos esos valores son inmutables.

  La clase Lampara deberá contar, al menos, con los siguientes métodos:

  poner(bombilla): pone una bombilla en la lámpara, en alguno de los casquillos que haya
    libres y que sea del mismo tamaño que la bombilla.
    De no haber ningún casquillo adecuado libre, o si al poner la nueva bombilla
    se supera la potencia máxima permitida en la lámpara, el método no hará nada.
    Devuelve el objeto lámpara.
  quitar(tamaño): quita una bombilla cualquiera de la lámpara con el tamaño indicado,
    y la devuelve. En caso de no haber ninguna de ese tamaño, devolverá None.
  potencia_total(): devuelve la potencia total consumida por la lámpara en vatios,
    calculada con la suma de las potencias de cada bombilla puesta en la lámpara.

  TEST:
  print(Lampara(3, 0, 20).poner(Bombilla(10, 'P')).potencia_total()) # 10
  print(Lampara(3, 0, 20).poner(Bombilla(10, 'M')).potencia_total()) # 0
  print(Lampara(3, 2, 20).poner(Bombilla(10, 'P')).poner(
      Bombilla(10, 'M')).quitar('M').tamanyo()) # "M"
"""


from abc import abstractmethod
from webbrowser import get


class Bombilla:
    def __init__(self, potencia, tamanyo) -> None:
        self.__potencia = potencia
        if tamanyo not in ("P", "M"):
            raise ValueError("Tamaño incorrecto.")
        self.__tamanyo = tamanyo

    def potencia(self):
        return self.__potencia

    def tamanyo(self):
        return self.__tamanyo


class Lampara:
    def __init__(self, peq, med, pmax) -> None:
        self.__casquillos = {"P": peq, "M": med}
        self.__bombillas = {"P": [], "M": []}
        self.__pmax = pmax

    def quitar(self, tamanyo):
        for i in self.__bombillas:
            if tamanyo == i:
                if self.__bombillas[i] == []:
                    return None
                return self.__bombillas[i].pop()

    def __potencia_total(self):
        ptotal = 0
        for tamanyo in self.__bombillas:
            for bombilla in self.__bombillas[tamanyo]:
                ptotal += bombilla.potencia()
        return ptotal

    def poner(self, bombilla):
        t = bombilla.tamanyo()
        if (self.__potencia_total() + bombilla.potencia()) <= self.__pmax:
            if len(self.__bombillas[t]) < self.__casquillos[t]:
                self.__bombillas[t].append(bombilla)
        return self
