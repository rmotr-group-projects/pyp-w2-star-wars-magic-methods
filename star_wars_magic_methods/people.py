class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not self.dark_side
        
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self)
        
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError()        
        return "{} swings a lightsaber at {}.".format(self, other)
    
    __truediv__ = __div__
    
    def __mul__(self, other):
        if not isinstance(other, People):
            raise TypeError()           
        return "{} throws a thermal detonator at {}!".format(self, other)

    def __rshift__(self, other): # >>
        if not isinstance(other, People):
            raise TypeError()
        return "{} uses the force to push {} away from them.".format(self, other)
        
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError()           
        return "{self} uses the force to pull {other} towards them.".format(self=self, other=other)
        
    def __neg__(self):
       self.dark_side = True
       self.light_side = not self.dark_side

    def __pos__(self):
       self.dark_side = False
       self.light_side = not self.dark_side

    def __invert__(self):
       self.dark_side = not self.dark_side
       self.light_side = not self.light_side

    def __xor__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        return "{self} force chokes {other}.".format(self=self, other=other)

    def __eq__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        if self.name == 'Han Solo' and other.name == 'Greedo':
            return '{self} shoots {other}.'.format(self=self, other=other)
        elif self.name == 'Greedo' and other.name == 'Han Solo':
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'            
