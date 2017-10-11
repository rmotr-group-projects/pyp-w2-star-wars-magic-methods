class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side

    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self)
    
    def __truediv__(self, other):
        if isinstance(other, People):
            return "{} swings a lightsaber at {}.".format(self, other)
        raise TypeError()


    def __mul__(self, other):
        if isinstance(other, People):
            return "{} throws a thermal detonator at {}!".format(self, other)
        raise TypeError()
    
    def __rshift__(self, other):
        if isinstance(other, People):
            return "{} uses the force to push {} away from them.".format(self, other)
        raise TypeError()

    def __lshift__(self, other):
        if isinstance(other, People):
            return "{} uses the force to pull {} towards them.".format(self, other)
        raise TypeError()

    @property
    def dark_side(self):
        return self._dark_side
    
    @property
    def light_side(self):
        return not self._dark_side
        
    def __neg__(self):
        self._dark_side = True

    def __pos__(self):
        self._dark_side = False
    
    def __invert__(self):
        self._dark_side = not self._dark_side

    def __xor__(self, other):
        if isinstance(other, People):
            return "{} force chokes {}.".format(self, other)
        raise TypeError()

    
    def __eq__(self, other):
        if isinstance(other, People):
            if other.name == 'Han Solo':
                return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other, self)
            else:
                return "{} shoots {}.".format(self, other)
        raise TypeError()
    
    __div__ = __truediv__