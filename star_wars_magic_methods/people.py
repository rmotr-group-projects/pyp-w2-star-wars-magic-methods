class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.light_side = not dark_side
        self.dark_side =  dark_side
        
    def __str__(self):
        return "{name}".format(name = self.name)
        
    def __call__(self):
        return "Help me {hero}, you're my only hope.".format(hero = self.name)
        
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        return "{first} swings a lightsaber at {second}.".format(first = self.name, second = other.name)
        
    def __mul__(self, other):
        if not isinstance(self, People) or not isinstance(other, People):
            raise TypeError()
        return "{first} throws a thermal detonator at {second}!".format(first = self.name, second = other.name)
        
    def __rshift__(self, other):
        if not isinstance(self, People) or not isinstance(other, People):
            raise TypeError()
        return '{first} uses the force to push {second} away from them.'.format(first = self.name, second = other.name)
        

    def __lshift__(self, other):
        if not isinstance(self, People) or not isinstance(other, People):
            raise TypeError()
        return '{first} uses the force to pull {second} towards them.'.format(first = self.name, second = other.name)
        
    def __neg__(self):
        if not isinstance(self, People):
            raise TypeError()
        if self.light_side:
            self.light_side = False
            self.dark_side = True 
            
    def __pos__(self):
        if not isinstance(self, People):
            raise TypeError()
        if self.dark_side:
            self.light_side = True
            self.dark_side = False 
            
    def __invert__(self):
        if self.light_side:
            self.light_side = False
            self.dark_side = True
        else:
            self.light_side = True
            self.dark_side = False

    def __xor__(self, other):
        if not isinstance(self, People) or not isinstance(other, People):
            raise TypeError()
        return '{first} force chokes {second}.'.format(first = self.name, second = other.name)
        
    def __eq__(self, other):
        if not isinstance(self, People) or not isinstance(other, People):
            raise TypeError()
        if self.name == 'Han Solo':
            return 'Han Solo shoots Greedo.'
        else:
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
    
    __truediv__ = __div__
        
            
    
        
        