class Cliente:
    """Invariant:
            El telefono ha de tener 9 digitos.
    """
    def __init__(self, dni, nombre, apellidos, telefono):
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_telefono(telefono)

        """def __eq__(self, otro):
                if type(self) != type(otro):
                    return NotImplemented
                return self.dni() == otro.dni()
            """

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented

        return self.dni() == otro.dni()

    def __hash__(self):
        return hash(self.dni())

    """ def __repr__(self) -> str:
        d = repr(self.__dni)
        n = repr(self.__nombre)
        a = repr(self.__apellidos)
        t = repr(self.__telefono)
        return f'Cliente({d}, {n}, {a}, {t})'
    """

    def __repr__(self) -> str:
            d = self.__dni
            n = self.__nombre
            a = self.__apellidos
            t = self.__telefono
            return f'Cliente({d!r}, {n!r}, {a!r}, {t})'

    def dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        """
        Pre:
            True
        Post:
            self.apellidos() == apellidos

        Args:
            apellidos ([type]): [description]
        """
        self.__apellidos = apellidos
        assert self.apellidos() == apellidos

    def telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        """
        Pre:
            El telefono ha de tener 9 digitos.

        Args:
            telefono ([type]): [description]

        Raises:
            ValueError: [description]
        """
        if len(str(telefono)) != 9:
            raise ValueError('El telefono debe tener 9.')
        self.__telefono = telefono
