class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        
        # assign default dark_side + light_side values
        self.set_dark_side(dark_side)
        self.set_light_side(not dark_side)
        
    # Create properties for dark + light side
    @property
    def dark_side(self):
        return self._dark_side
        
    @property
    def light_side(self):
        return self._light_side

    # Create setter for dark + light side
    def set_dark_side(self, dark_side):
        self._dark_side = dark_side
    
    def set_light_side(self, light_side):
        self._light_side = light_side
        
    # Create getter for dark + light side
    def get_dark_side(self, dark_side):
        return self.dark_side
        
    def get_light_side(self, light_side):
        return self.light_side
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
        
    def __div__(self,other):
        if isinstance(other, People): # make sure 'other' is a "People" object
            return "{} swings a lightsaber at {}.".format(self.name,other.name)
        raise TypeError()
        
    __truediv__=__div__ # ensure version compatibility
    
    def __mul__(self, other):
        if isinstance(other,People):
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        raise TypeError()
        
    def __rshift__(self,other):
        if isinstance(other,People):
            return '{} uses the force to push {} away from them.'.format(self.name, other.name)
        raise TypeError()
        
    def __lshift__(self,other):
        if isinstance(other,People):
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        raise TypeError()
        
    def __neg__(self):
        self.set_dark_side(True)
        self.set_light_side(False)
        
    def __pos__(self):
        self.set_dark_side(False)
        self.set_light_side(True)
    
    def __invert__(self):
        self.set_dark_side(not self.dark_side) # call getter to access the property
    
    def __xor__(self,other):
        if isinstance(other,People):
            return '{} force chokes {}.'.format(self.name, other.name)
        raise TypeError()
        
    def __eq__(self,other):
        if not isinstance(other,People):
            raise TypeError()
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return '{} shoots {}. BECAUSE HAN SHOOTS FIRST.'.format(other.name, self.name)
        else:
            return '{} shoots {}.'.format(self.name, other.name)
        
    
