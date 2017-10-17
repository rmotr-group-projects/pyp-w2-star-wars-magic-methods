class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        
        if self.dark_side is False:
            self.light_side = True
        else:
            self.light_side = False
        
    def __str__(self):
        return '{}'.format(self.name)
        
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self.name)
        
    def __div__(self, other):
        try:
            return '{} swings a lightsaber at {}.'.format(self.name, other.name)
        except: 
            raise TypeError
    
    # multiplication - x.__mul__(y)
    def __mul__(self, other):
        try:
            return '{} throws a thermal detonator at {}!'.format(self.name, other.name)
        except: 
            raise TypeError
    
    # x >> y x.__rshift__(y) - right bit-shift
    def __rshift__(self, other):
        try:
            return '{} uses the force to push {} away from them.'.format(self.name, other.name)
        except: 
            raise TypeError
    
    # x << y x.__lshift__(y) - left bit-shift
    def __lshift__(self, other):
        try: 
            return '{} uses the force to pull {} towards them.'.format(self.name, other.name)
        except: 
            raise TypeError
        
    # negative number
    def __neg__(self):
        self.light_side = False
        self.dark_side = True
        
    # positive number    
    def __pos__(self):
        self.light_side = True
        self.dark_side = False
        
    # inverse
    def __invert__(self): 
        if self.light_side is True:
            self.light_side = False
            self.dark_side = True
        else:
            self.light_side = True
            self.dark_side = False
        
    # x ^ y - bitwise xor
    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name, other.name)
        
    # x.__eq__(y) equality
    def __eq__(self, other):
        if other.name != "Greedo":
            return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name, self.name)
        return '{} shoots {}.'.format(self.name, other.name)
