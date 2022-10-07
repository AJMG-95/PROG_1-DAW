'''Puertas y llaves (P = 3 puntos)
  Programar en Python un modelo orientado a objetos del problema de
    representar puertas y llaves.
  Para ello, hay que programar las clases Puerta y Llave. Las puertas y
    las llaves tienen un color (una cadena).

  Una puerta puede estar abierta o cerrada.
  Una puerta puede tener puesta una llave o ninguna.
  Para abrir una puerta, debe tener puesta una llave del mismo color
    que la puerta.
  Para cerrar una puerta no se necesita ninguna llave
    (si la tiene puesta, da igual).

  La clase Puerta debe contar, al menos, con los siguientes métodos además
    del constructor:
  poner(llave ): pone una llave en la cerradura de la puerta;
    devuelve el propio objeto Puerta.
  quitar(): quita la llave de la puerta; devuelve la llave que estaba
    puesta en la puerta, o None si no tenía ninguna llave puesta.
  abrir(): abre la puerta, si es posible; devuelve True si se
    ha podido abrir (o ya estaba abierta) o False en caso contrario.
  cerrar(): cierra la puerta; no devuelve ningún valor.

  La clase Llave debe contar, al menos, con los siguientes métodos además
    del constructor:
  color(): devuelve el color de la llave.

  Tests:

  Puerta('rojo').poner(Llave('rojo')).abrir() == True
  Puerta('rojo').poner(Llave('verde')).abrir() == False
  Puerta('rojo').abrir() == False
'''


class Llave:
    def __init__(self, color) -> None:
        self.__color = color

    def color(self):
        return self.__color


class Puerta:
    def __init__(self, color) -> None:
        self.__color = color
        self.__abierta = False
        self.__llave = None

    def quitar(self) -> object:
        """Retira la llave de la puerta

                Returns:
                        Llave: Devuelva la llave de la puerta si estaba puesta,
                                en caso contrario devuelve None
                """
        l = self.__llave
        if l is not None:
            self.__llave = None
            return l
        return self.__llave

    def abrir(self):
        if self.__llave is not None:
            cl = self.__llave.color()
            if cl == self.__color:
                self.__abierta = True
                return self.__abierta
        return False

    def cerrar(self):
        self.__abierta = False

    def poner(self, llave: object):
        self.__llave = llave
        return self
