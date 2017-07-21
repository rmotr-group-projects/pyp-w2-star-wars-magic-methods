class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        if self.dark_side is True:
            self.light_side = False
        else:
            self.light_side = True

   def__div__(self,other):
    def __str__(self):
        return self.name
    
    def __call__(self): 
        return "Help me {}, you're my only hope.".format(self.name)
   
    def __div__(self,other):
        try:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        except: 
            raise TypeError
    
    def __mul__(self,other):
        try: 
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        except:
            raise TypeError
            
    
    def __rshift__(self, other): 
        try: 
            return '{} uses the force to push {} away from them.'.format(self.name, other.name)
        except: 
            raise TypeError
    
    def __lshift__(self, other): 
        try: 
            return '{} uses the force to pull {} towards them.'.format(self.name, other.name)
        except: 
            raise TypeError


    def __neg__(self): 
        self.light_side = False
        self.dark_side = True

    
    def __pos__(self):
        self.light_side = True
        self.dark_side = False

    def __invert__(self): 
        if self.light_side is True:
            self.light_side = False
            self.dark_side = True
        else:
            self.light_side = True
            self.dark_side = False
            
    def __xor__(self, other): 
        return "{} force chokes {}.".format(self.name, other.name)
        
    
    def __eq__(self,other):
        self.name==other.name:
            return '{} shoots {}'.format(self.name, other.name)
        if other.name==self.name:
            first_name = self.name.split(' ', 1)[0]
            return '{} shoots {}. BECAUSE {} SHOOTS FIRST.'.format(self.name, other.name, first_name.upper())
    '''
    def __eq__(self, other):
	return self.name==other.name
    '''