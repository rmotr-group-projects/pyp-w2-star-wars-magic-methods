class People(object):
    def __init__(self, name, dark_side = False):
        self.name = name
        self._dark_side = dark_side
        
    @property 
    def dark_side(self):
        return self._dark_side
    
    @property
    def light_side(self):
        return not self._dark_side
        
    def __call__(self):
        return "Help me " + self.name + ", you're my only hope."
        
    def __str__(self):
        return self.name
        
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        return "{self} swings a lightsaber at {other}.".format(self=self, other=other)
    
    __truediv__ = __div__
    
    def __mul__(self, other):
        if type(other) is int:
            raise TypeError('not string')
        else:
            return self.name + " throws a thermal detonator at " + other.name + "!"
    
    def __invert__(self):
        self._dark_side = not self._dark_side
    
    def __pos__(self):
        self._dark_side = False
    
    def __neg__(self):
        self._dark_side = True
    
    def __eq__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        
        if self.name == "Han Solo":
            return self.name + " shoots " + other.name + "."
        return other.name + " shoots " + self.name + ". BECAUSE HAN SHOOTS FIRST."
        
    def __rshift__(self, other):
        if not isinstance(other, People):
            raise TypeError('invalid entry')
        return self.name + " uses the force to push " + other.name + " away from them."
        
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError('invalid entry')
        return self.name + " uses the force to pull " + other.name + " towards them."
    
    def __xor__(self, other):
        return self.name + " force chokes " + other.name + '.'
            
        

vader = People('Darth Vader')
motti = People('Admiral Motti')
print(vader ^ motti)

