class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side

    @property
    def light_side(self):
        return not self._dark_side

    @property
    def dark_side(self):
        return self._dark_side

    def test_class(self, other):
        if type(other) is not People:
            raise TypeError()

    def __str__(self):
        return self.name

    # Call for only hope
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)

    # Swings lightsaber
    def __div__(self, other):
        People.test_class(self, other)
        return "{} swings a lightsaber at {}.".format(self.name, other.name)

    __truediv__ = __div__

    def __mul__(self, other):
        # Thermal detonator
        People.test_class(self, other)
        return '{} throws a thermal detonator at {}!'.format(self.name,
                                                             other.name)

    def __rshift__(self, other):
        # Force Push
        People.test_class(self, other)
        return'{} uses the force to push {} away from them.'.format(self.name,
                                                                    other.name)

    def __lshift__(self, other):
        # Force Pull
        People.test_class(self, other)
        return '{} uses the force to pull {} towards them.'.format(self.name,
                                                                   other.name)

    # To the dark side
    def __neg__(self):
        self._dark_side = True

    # To the light side
    def __pos__(self):
        self._dark_side = False

    # Flip sides
    def __invert__(self):
        self._dark_side = not self._dark_side

    # Force choke
    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)

    # shoots
    def __eq__(self, other):
        if str(self) == 'Han Solo':
            return '{} shoots {}.'.format(self.name, other.name)
        return ('{} shoots {}. ' +
                'BECAUSE {} SHOOTS FIRST.').format(other.name, self.name,
                                                   str(other)[:3].upper())
