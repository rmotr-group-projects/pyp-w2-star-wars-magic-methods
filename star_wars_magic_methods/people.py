from __future__ import division


class People(object):

    def __init__(self, name, dark_side=False):
        self.name = name 
        self._dark_side = dark_side
        if not dark_side:
            self._light_side = True
        else:
            self._light_side = False
        
    @property
    def light_side(self):
         return self._light_side
    
    @property
    def dark_side(self):
         return self._dark_side
    
    @light_side.setter
    def light_side(self,value):
        self._light_side = value    
    
    @dark_side.setter
    def dark_side(self,value):
        self._dark_side = value

    def __str__(self):
        return self.name
    
    def __call__(self):                  
        return "Help me Obi-Wan Kenobi, you're my only hope."

    def __div__(self,other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " swings a lightsaber at "+ other.name + "."
        
    def __truediv__(self,other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " swings a lightsaber at "+ other.name + "."    

    def __mul__(self,other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " throws a thermal detonator at "+ other.name + "!"
    
    def __rshift__(self, other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " uses the force to push "+ other.name + " away from them."

    def __lshift__(self, other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " uses the force to pull "+ other.name + " towards them."

    def __neg__(self):
        self.light_side = False
        self.dark_side = True

    def __pos__(self):
        self.light_side = True
        self.dark_side =  False

    def __invert__(self):
        self.light_side = not self.light_side

    def __xor__(self, other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        return self.name + " force chokes "+ other.name + "."

    def __eq__(self, other):
        if isinstance(other, People) == False: #and isinstance(other, str) == False:
            raise TypeError
        
        if self.name.find('Han') > -1:
            return self.name + " shoots "+ other.name + "."
        else:
            return other.name + " shoots "+ self.name + ". BECAUSE HAN SHOOTS FIRST."



