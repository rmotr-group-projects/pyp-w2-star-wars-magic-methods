#from __future__ import division 

class People(object):
    def __init__(self, name, dark_side=False,light_side=True):
        self.name=name
        self.dark_side=dark_side
        self.light_side=light_side
        if self.dark_side==True:
            self.light_side=False
        
    def __str__(self):
        return self.name
        
    def __call__(self):
        return "Help me "+self.name+", you're my only hope."
        
    def __div__(self,other):
        if isinstance(other,People):
            return self.name+" swings a lightsaber at "+other.name+"."
        else:
            raise TypeError()
            
    def __mul__(self,other):
        if isinstance(other,People):
            return self.name+" throws a thermal detonator at "+other.name+"!"
        else:
            raise TypeError()
            
    def __rshift__(self,other):
        if isinstance(other,People):
            return self.name+" uses the force to push "+other.name+" away from them."
        else:
            raise TypeError()

    def __lshift__(self,other):
        if isinstance(other,People):
            return self.name+" uses the force to pull "+other.name+" towards them."
        else:
            raise TypeError()
            
    def __eq__(self,other):
        if self.name=="Han Solo":
            return self.name+" shoots "+other.name+"."
        else:
            return other.name+" shoots "+self.name+". BECAUSE HAN SHOOTS FIRST."
            
    def __neg__(self):
        self.dark_side=True
        self.light_side=False
        
    def __pos__(self):
        self.dark_side=False
        self.light_side=True