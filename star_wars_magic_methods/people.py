class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark = dark_side
        
    def __str__(self):
        return self.name
        
    @property
    def dark_side(self):
        return self.dark
    
    @property
    def light_side(self):
        return not self.dark

    def __call__(self):
        return "Help me {self}, you're my only hope.".format(self = self)
    
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError
        return "{self} swings a lightsaber at {other}.".format(self = self, other = other)
        
    __truediv__ = __div__
    
    def __mul__(self, other):
        if isinstance(other, People):
            return "{self} throws a thermal detonator at {other}!".format(self = self, other = other)
        else:
            raise TypeError
        
    def __rshift__(self, other):    
        if not isinstance(other, People):
            raise TypeError
        return '{self} uses the force to push {other} away from them.'.format(self = self, other = other)
        
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError() 
        return '{self} uses the force to pull {other} towards them.'.format(self = self, other = other)

    def __neg__(self):
       self.dark = True  
       
    def __pos__(self):
        self.dark = False
    
    def __invert__(self):
        self.dark = not self.dark
            
    def __eq__(self, other): 
        if not isinstance(other, People):
            raise TypeError()
        if other.name == 'Han Solo':
            return 'Han Solo shoots {self}. BECAUSE HAN SHOOTS FIRST.'.format(self = self)
        else:
            return '{self} shoots {other}.'.format(self = self, other = other) 

    def __xor__(self, other):
        return '{self} force chokes {other}.'.format(self = self, other = other)