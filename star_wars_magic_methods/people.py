class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not self.dark_side

    def __str__(self):
        return self.name
        
    def __neg__(self):
        self.dark_side = True
        self.light_side = False
        
    def __pos__(self):
        self.dark_side = False
        self.light_side = True
        
    def __invert__(self):
        self.dark_side = not self.dark_side
        self.light_side = not self.light_side
        
    def __rxor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)
        
    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)
        
    def __eq__(self, other):
        
        if other.name == 'Han Solo':
            return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name, self.name)
        
        return "{} shoots {}.".format(self.name, other.name)
        
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
        
    def __truediv__(self, other):
        if type(other) is not People:
            raise TypeError()
            
        return '{} swings a lightsaber at {}.'.format(self.name, other.name)
        
    def __div__(self, other):
        if type(other) is not People:
            raise TypeError()
            
        return '{} swings a lightsaber at {}.'.format(self.name, other.name)
        
    def __mul__(self, other):
        if type(other) is not People:
            raise TypeError
            
        return '{} throws a thermal detonator at {}!'.format(self.name, other.name)
        
    def __rshift__(self, other):
        if type(other) is not People:
            raise TypeError
            
        return '{} uses the force to push {} away from them.'.format(self.name, other.name)
        
    def __lshift__(self, other):
        if type(other) is not People:
            raise TypeError
            
        return '{} uses the force to pull {} towards them.'.format(self.name, other.name)