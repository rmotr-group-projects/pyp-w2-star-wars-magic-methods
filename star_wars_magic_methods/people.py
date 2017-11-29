class People(object):
    def __init__(self, name, dark_side=False, light_side=True):
        self.name = name 
        self.dark_side = dark_side 
        self.light_side = light_side
        if dark_side == True:
            self.light_side = False
    
    def __str__(self):
        return '{}'.format(self.name)
    
    def __call__(self):
        if self.name == 'Obi-Wan Kenobi':
            return "Help me Obi-Wan Kenobi, you're my only hope."
    
    def __div__(self, other): 
        try:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        except: 
            raise TypeError()
            
    def __mul__(self, other):
        try:
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        except: 
            raise TypeError()
    
    def __rshift__(self, other):
        try: 
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
        except:
            raise TypeError()
        
    def __lshift__(self, other):
        try:
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        except:
            raise TypeError()
    
    def __pos__(self):
        if self.dark_side == True:
            self.dark_side = False
            self.light_side = True
            
    def __neg__(self):
        if self.light_side == True and self.dark_side == False:
            self.dark_side = True
            self.light_side = False
    
    def __invert__(self):
        if self.dark_side == True and self.light_side == False: 
            self.dark_side = False 
            self.light_side = True
        else: 
            self.dark_side = True
            self.light_side = False
    
    def __xor__(self, other): 
        try:
            return "{} force chokes {}.".format(self.name, other.name) 
        except:
            raise TypeError() 
    
    def __eq__(self, other):
        try: 
            if other.name == "Han Solo": 
                return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name, self.name)
            else:
                return "{} shoots {}.".format(self.name, other.name)
        except:
            raise TypeError()