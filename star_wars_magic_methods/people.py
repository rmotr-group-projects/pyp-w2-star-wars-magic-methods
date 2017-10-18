class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side

    def __str__(self):
        return self.name

    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)

    def __truediv__(self, other):
        if type(other) == People:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        else:
            raise TypeError()

    def __div__(self, other):
        if type(other) == People:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        else:
            raise TypeError()
            
    def __mul__(self, other):
        if type(other) == People:
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        else:
            raise TypeError()

    def __rshift__(self, other):
        if type(other) == People:
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
        else:
            raise TypeError()

    def __lshift__(self, other):
        if type(other) == People:
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        else:
            raise TypeError()

    def __neg__(self):
        self.dark_side = True

    def __pos__(self):
        self.dark_side = False

    def __invert__(self):
        self.dark_side = ~self.dark_side

    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)

    def __eq__(self, other):
        if other.name == "Han Solo":
            return "Han Solo shoots {}. BECAUSE HAN SHOOTS FIRST.".format(self.name)
        return "{} shoots {}.".format(self.name, other.name)

    @property
    def light_side(self):
        return not self.dark_side