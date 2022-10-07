
class pila:
    """
    Invariant:
        len(self) == self.get_num_apilar() - self.get_num_desapilar()
        len(pila) == pila.get_num_apilar() - pila.get_num_desapilar()
    """
    def __init__(self, elementos = None) -> None:
        self.__elementos = []
        if elementos is None:
            self.__elementos = []
        else:
            self.__elementos = list(elementos)
        self.__num_apilar = 0
        self.__num_desapilar = 0

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.__elementos == otro.__elementos

    def __len__(self):
        return len(self.__elementos)

    def __repr__(self) -> str:
        return f'Pila({self.__elementos!r}'

    def __iter__(self):
        return iter(self.__elementos)

    def apilar(self, elem):
        self.__elementos.append(elem)
        self.__num_apilar += 1

    def get_num_apilar(self):
        return self.__num_apilar

    def es_vacia(self) -> bool:
        return len(self.__elementos) == 0

    def cima(self):
        self.__comp_no_vacia()
        return self.__elementos[-1]

    def desapilar(self):
        """
        Pre:
            not self.es_vacia()
        Post:
            Devuelve el elemento que estaba en la cima.

        Returns:
            [type]: [description]
        """
        self.__comp_no_vacia()
        self.__num_desapilar += 1
        num_antes = len(self)
        elem_cima = self.cima()
        res = self.__elementos.pop()
        assert len(self) == num_antes - 1 and elem_cima == res
        return res
    def get_num_desapilar(self):
        return self.__num_desapilar

    def __comp_no_vacia(self):
        if self.es_vacia():
            raise ValueError('La pila está vacía')


#TODO: Este metodo pendsó para hacer que la pila fuera iterable pero se ha sustituido
  #TODO: por el metodo por el metodo __iter__(self)
#   def get_elementos(self) -> list:
#       return self.__elementos[:]
