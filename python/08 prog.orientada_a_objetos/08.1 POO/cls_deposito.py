class Deposito:
    """ Description:


    Invariant:
        saldo >= 0
    """
    __interes = 0.02 # Variable de clase

    def __init__(self, fondos, historial=None) -> None:
        """
        Pre: fondos >= 0
        Post: self.__saldo() == fondos

        Args:
            fondos ([type]): [description]
            historial ([type], optional): [description]. Defaults to None.

        Raises:
            ValueError: [description]
        """
        if fondos < 0:
            raise ValueError('Los fondos deben ser posotivos.')
#       assert fondos >= 0 -> Esta linea "sustituye" al if Pero no tiene mensaje de error.
                        # Los assert se pueden saltar. (arrancar el interprete con la opcion -O)
        self.__fondos = fondos
        if historial is None:
            self.__historial = []
        else:
            self.__historial = historial
        assert self.saldo() == fondos # Se usa generalmente para comprobar las post-condiciones

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented

        return self.saldo() == otro.saldo() and self.__historial == otro.historal

    def __repr__(self) -> str:
        return f'Deposito({self.saldo()!r}, {self.__historial!r})'

    def __str__(self) -> str:
        return f'Deposito con saldo {self.saldo()}. \n Movimientos: \n' + \
                '\n'.join(self.__historial)

    def saldo(self) -> int or float:
        return self.__fondos

    def ingresar(self, cantidad) -> None:
        """
        Pre: cantidad >= 0
        Post: saldo_nuevo == saldo_viejo + cantidad

        Args:
            cantidad ([type]): [description]
        """
        self.__cantidad_posotiva(cantidad)
        saldo_viejo = self.saldo()
        self.__fondos += cantidad
        self.__historial.append(f'Ingresa: {cantidad}')
        assert self.saldo() == saldo_viejo + cantidad

    def retirar(self, cantidad) -> None:
        """
        Pre: cantidad >= 0 and cantidad <= fondos
        Post: saldo_nuevo == saldo_viejo - cantidad

        Args:
            cantidad ([type]): [description]

        Raises:
            ValueError: [description]
        """
        self.__cantidad_posotiva(cantidad)
        if self.__fondos < cantidad: # Precondicion
            raise ValueError('No hay fondos suficientes.')
        saldo_viejo = self.saldo()
        self.__fondos -= cantidad
        self.__historial.append(f'Retira: {cantidad}')
        assert self.saldo() == saldo_viejo - cantidad

    @staticmethod
    def __cantidad_posotiva(cantidad) -> None: # No tiene self porque es un metodo estatico y no lo necesita
        if cantidad < 0:
            raise ValueError('La cantidad ha de ser porsitiva.')

    def total(self):
        return self.saldo() * (1 + Deposito.get_interes())

    @staticmethod
    def get_interes():
        return Deposito.__interes

#! Interfaz de la clase Deposito
    """
    Nombre: Deposito
    __init__(fondos: Number) -> None
    __eq__(otro: Any) -> bool
    __repr__() -> str
    __str__()-> str
    saldo() -> Number
    ingresar(cantidad: Number) -> None
    retirar(cantidad: Numbre) -> None
    """

#! Especificación de la clase Deposito:
    #* Interfaz: ver arriba
    #? Invariantes: saldo() >= 0

#! Especificaciones funcioneales de las operaciones:
    #*  Pre: fondos >=0
    #* __init__()
    #*  Post: saldo >= 0

    #*   Pre: True
    #*__eq__()
    #* Post: self=otro <=> self.__eq__(otro)

    #?  Pre: cantidad > 0
    #?ingresar() = saldo()viejo + cantidad
    #?  Post: saldo()nuevo

    #?  Pre: cantidad > 0
    #?retirar()
    #?  Post: saldo()nuevo = saldo()viejo - cantidad
