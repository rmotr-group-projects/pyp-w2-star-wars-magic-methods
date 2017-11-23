class People(object):
    def __init__(self, name, dark_side=False):
        self.__name = name
        self.__dark_side = dark_side

    @property
    def light_side(self):
        return self.__dark_side is False

    @property
    def dark_side(self):
        return self.__dark_side is True

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        return "Help me {}, you're my only hope.".format(self.name)

    def __div__(self, other):
        if type(other) is People:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        else:
            raise TypeError

    __truediv__ = __div__

    def __mul__(self, other):
        if type(other) is People:
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        else:
            raise TypeError

    def __rshift__(self, other):
        if type(other) is People:
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
        else:
            raise TypeError

    def __lshift__(self, other):
        if type(other) is People:
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        else:
            raise TypeError

    def __neg__(self):
        self.__dark_side = True

    def __pos__(self):
        self.__dark_side = False

    def __invert__(self):
        self.__dark_side = not self.__dark_side

    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)

    def __eq__(self, other):
        if self.name == "Greedo" and other.name == "Han Solo":
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        return "{} shoots {}.".format(self.name, other.name)
