class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side

    def __str__(self):
        return self.name

    def __call__(self):
        return "Help me {self}, you're my only hope.".format(self=self)

    def __truediv__(self, other): # /
        if not isinstance(other, People):
            raise TypeError()
        return "{self} swings a lightsaber at {other}.".format(self=self, other=other)
    
    __div__=__truediv__

    def __mul__(self, other): # *
        if not isinstance(other, People):
            raise TypeError()
        return "{self} throws a thermal detonator at {other}!".format(self=self, other=other)

    def __lshift__(self, other): # <<
        if not isinstance(other, People):
            raise TypeError()
        return "{self} uses the force to pull {other} towards them.".format(self=self, other=other)

    def __rshift__(self, other): # >>
        if not isinstance(other, People):
            raise TypeError()
        return "{self} uses the force to push {other} away from them.".format(self=self, other=other)

    @property
    def dark_side(self):
        return self._dark_side

    @property
    def light_side(self):
        return not self._dark_side

    def __neg__(self): # -x
        self._dark_side = True

    def __pos__(self): # +x
        self._dark_side = False

    def __invert__(self): # ~x
        self._dark_side = not self._dark_side

    def __xor__(self, other): # ^
        if not isinstance(other, People):
            raise TypeError()
        return "{self} force chokes {other}.".format(self=self, other=other)

    def __eq__(self, other): # ==
        if not isinstance(other, People):
            raise TypeError()
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        else:
            return '{self} shoots {other}.'.format(self=self, other=other)
