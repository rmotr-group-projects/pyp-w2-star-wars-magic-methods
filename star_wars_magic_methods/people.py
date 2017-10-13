class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me " + self.name + ", you're my only hope."
    
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return self.name + " swings a lightsaber at " + other.name + "."
    
    def __mul__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return self.name + " throws a thermal detonator at " + other.name + "!"
    
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return self.name + " uses the force to pull " + other.name + " towards them."
    
    def __rshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return self.name + " uses the force to push " + other.name + " away from them."
    
    def __neg__(self):
        self.dark_side = True
        return self
    
    def __pos__(self):
        self.dark_side = False
        return self
    
    def __invert__(self):
        self.dark_side = not self.dark_side
        return self
    
    def __xor__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        else:
            return self.name + " force chokes " + other.name + "."
    
    def __eq__(self, other):
        if self.name == 'Greedo':
            return other.name + " shoots " + self.name + ". BECAUSE HAN SHOOTS FIRST."
        else:
            return self.name + " shoots " + other.name + "."
    
    @property
    def light_side(self):
        return not self.dark_side