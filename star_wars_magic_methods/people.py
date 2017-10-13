class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
        
    @property
    def light_side(self):
        return not self._dark_side
    
    @property
    def dark_side(self):
        return self._dark_side
    
    def __str__(self):
        return self.name
        
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
        
    def __div__(self, other):
        if type(self) is not People or type(other) is not People:
            raise TypeError()
        return "{} swings a lightsaber at {}.".format(self.name, other.name)
        
