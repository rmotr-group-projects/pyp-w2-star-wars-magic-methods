#from __future__ import division 

class People(object):
    def __init__(self, name, dark_side=False,light_side=True):
        self.name=name
        self.dark_side=dark_side
        self.light_side=light_side
        
    def __str__(self):
        return self.name
        
    def __call__(self):
        return "Help me "+self.name+", you're my only hope."
        
    def __div__(self,other):
        if isinstance(other,People):
            return self.name+" swings a lightsaber at "+other.name+"."
        else:
            raise TypeError()

