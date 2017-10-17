class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._ds = dark_side
        
    @property
    def dark_side(self):
            return self._ds
            
    @dark_side.setter
    def dark_side(self, state):
        self._ds = state
        
    @property
    def light_side(self):
        return not self.dark_side
        
    def __str__(self):
        return self.name
        
    def __call__(self):
        return 'Help me {}, you\'re my only hope.'.format(self.name)
    
    def __truediv__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        return '{} swings a lightsaber at {}.'.format(self.name, other.name) #
        
    def __mul__(self, other):
        if not isinstance(other, People): 
            raise TypeError()
        return '{} throws a thermal detonator at {}!'.format(self.name, other.name) 

    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError() 
        return '{} uses the force to pull {} towards them.'.format(self.name, other.name) 

    def __rshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        return '{} uses the force to push {} away from them.'.format(self.name, other.name) 

    def __neg__(self):
        if self.dark_side == False:
            return ~self
        
    def __pos__(self): 
        if self.dark_side == True:
            return ~self
    
    def __invert__(self):
        self.dark_side = not self.dark_side
        
    def __xor__(self, other):
        if not isinstance(other, People):
            raise TypeError() 
        return '{} force chokes {}.'.format(self.name, other.name) 
    
    def __eq__(self, other): 
        if not isinstance(other, People):
            raise TypeError()
        if other.name == 'Han Solo':
            return 'Han Solo shoots {}. BECAUSE HAN SHOOTS FIRST.'.format(self.name)
        else:
            return '{} shoots {}.'.format(self.name, other.name) 
            
