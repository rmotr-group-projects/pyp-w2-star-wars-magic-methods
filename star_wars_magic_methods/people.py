class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
        
    @property
    def light_side(self):
        if self._dark_side == False:
            return True
    
    @property
    def dark_side(self):
        if self._dark_side == True:
            return True
            
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self)
    
    def __div__(self, other):
        if isinstance(other, People):
            return '{} swings a lightsaber at {}.'.format(self, other)
        else:
            raise TypeError
    
    def __mul__(self, other):
        if isinstance(other, People):
            return "{} throws a thermal detonator at {}!".format(self, other)
        else:
            raise TypeError
    
    def __lshift__(self, other):
        if isinstance(other, People):
            return '{} uses the force to pull {} towards them.'.format(self, other)
        else:
            raise TypeError
    
    def __rshift__(self, other):
        if isinstance(other, People):
            return '{} uses the force to push {} away from them.'.format(self, other)
        else:
            raise TypeError
    
    def __neg__(self): # -x
        self._dark_side = True

    def __pos__(self): # +x
        self._dark_side = False
    
    def __invert__(self):
        if self._dark_side == True:
            self._dark_side = False
        else:
            self._dark_side = True
    
    def __xor__(self, other):
        return '{} force chokes {}.'.format(self, other)
    
    def __eq__(self, other):
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return '{} shoots {}. BECAUSE HAN SHOOTS FIRST.'.format(other, self)
        else:
            return '{} shoots {}.'.format(self, other)
    
