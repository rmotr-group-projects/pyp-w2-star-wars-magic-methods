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
        try:
            isinstance(other, People)
            return '{} swings a lightsaber at {}.'.format(self.name, other.name) #
        except:
            raise TypeError()
            #is it good enough to stop here?
        
    def __mul__(self, other):
        try:
            isinstance(other, People)
            return '{} throws a thermal detonator at {}!'.format(self.name, other.name) 
        except:
            raise TypeError()

    def __lshift__(self, other):
        try: #type checking not required here to pass tests but keep for consistency
            isinstance(other, People)
            return '{} uses the force to pull {} towards them.'.format(self.name, other.name) 
        except:
            raise TypeError() 

    def __rshift__(self, other):
        try:
            isinstance(other, People)
            return '{} uses the force to push {} away from them.'.format(self.name, other.name) 
        except:
            raise TypeError()
    
    def __neg__(self):
        if self.dark_side == False:
            return ~self
        
    def __pos__(self): 
        if self.dark_side == True:
            return ~self
    
    def __invert__(self):
        self.dark_side = not self.dark_side
        
    def __xor__(self, other):
        try: #type checking not required here to pass tests but keep for consistency
            isinstance(other, People)
            return '{} force chokes {}.'.format(self.name, other.name) 
        except:
            raise TypeError() 
    
    def __eq__(self, other): 
        try: #type checking not required here to pass tests but keep for consistency
            isinstance(other, People)
            if other.name == 'Han Solo':
                return 'Han Solo shoots {}. BECAUSE HAN SHOOTS FIRST.'.format(self.name)
            return '{} shoots {}.'.format(self.name, other.name) 
        except:
            raise TypeError() 
