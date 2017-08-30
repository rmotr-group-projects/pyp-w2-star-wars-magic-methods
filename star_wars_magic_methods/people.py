class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not dark_side
        
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self)
    
    def __div__(self, other):
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

    
    def __neg__(self):
        self.dark_side = True
        self.light_side = False

    def __pos__(self):
        self.light_side = True
        self.dark_side = False
    
    def __invert__(self):
        self.dark_side = not self.dark_side
        self.light_side = not self.light_side

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
