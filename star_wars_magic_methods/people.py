class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
    
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
    
    __truediv__ = __div__
    
    def __mul__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
    
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
    
    def __rshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
    
    def __neg__(self):
        self.dark_side = True
    
    def __pos__(self):
        self.dark_side = False
    
    def __invert__(self):
        self.dark_side = not self.dark_side
    
    def __xor__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return "{} force chokes {}.".format(self.name, other.name)
    
    def __eq__(self, other):
        if self.name == 'Greedo':
            return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name, self.name)
        else:
            return "{} shoots {}.".format(self.name, other.name)
    
    @property
    def light_side(self):
        return not self.dark_side