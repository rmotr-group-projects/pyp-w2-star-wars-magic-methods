class People(object):
    def __init__(self, name, dark_side = False):
        self.name = name
        self._dark_side = dark_side
        
    @property
    def light_side(self):
        if self._dark_side == False:
            return True
    
    @property
    def dark_side(self):
        if self._dark_side == True:
            return True
    def __str__(self):
        return self.name

    def __call__(self):
        return "Help me " + self.name + ", you're my only hope."
    
    def __div__(self, other):
        try:
            return self.name + ' swings a lightsaber at ' + other.name + '.'
        except:
            raise TypeError()
    
    def __mul__(self, other):
        try:
            return self.name + ' throws a thermal detonator at ' + other.name + '!'
        except:
            raise TypeError()
    
    def __rshift__(self, other):
        try:
            return self.name + ' uses the force to push ' + other.name + ' away from them.'
        except:
            raise TypeError()
    
    def __lshift__(self, other):
        try:
            return self.name + ' uses the force to pull ' + other.name + ' towards them.'
        except:
            raise TypeError()
    
    def __neg__(self):
        self._dark_side = True
           
    def __pos__(self):
        self._dark_side = False
    
    def __invert__(self):
        if self._dark_side == True:
            self._dark_side = False
        else:
            self._dark_side = True
    
    def __xor__(self, other):
        return self.name + ' force chokes ' + other.name + '.'
    
    def __eq__(self, other):
        if self.name == 'Han Solo':
            return 'Han Solo shoots ' + other.name + '.'
        elif other.name == 'Han Solo':
            return 'Han Solo shoots ' + self.name + '. BECAUSE HAN SHOOTS FIRST.'