from __future__ import division
class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
    
    @property
    def light_side(self):
        return not self.dark_side
    
    @property
    def dark_side(self):
        return self._dark_side
    
    @light_side.setter
    def light_side(self, value):
        self._dark_side = not value
    
    @dark_side.setter
    def dark_side(self, value):
        self._dark_side = value
    
    def __str__(self):
        return self.name
        
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
    
    def __div__(self, other):
        if isinstance(other, self.__class__):
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        else:
            raise TypeError
            
    __truediv__ = __div__
        
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        else:
            raise TypeError
    
    __rmul__ = __mul__
    __lmul__ = __rmul__
    
    def __rshift__(self, other):
        if isinstance(other, self.__class__): 
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
        else:
            raise TypeError

    __rrshift__ = __rshift__
    
    def __lshift__(self, other):
        if isinstance(other, self.__class__): 
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        else:
            raise TypeError

    __rlshift__ = __lshift__
    
    def __neg__(self):
        self.dark_side = True
    
    def __pos__(self):
        self.dark_side = False
    
    def __invert__(self):
        self.dark_side = ~self.dark_side
        
    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)
    
    def __eq__(self, other):
        actionString = "{} shoots {}."
        if other.name == 'Han Solo':
            return actionString.format(other.name, self.name) + " BECAUSE HAN SHOOTS FIRST."
        else:
            return actionString.format(self.name, other.name)
        
    

    
    
