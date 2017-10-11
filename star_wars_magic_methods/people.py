class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not self.dark_side
        
    def __str__(self):
        return(self.name)
        
    def __call__(self):
        return("Help me %s, you're my only hope." % self.name)
        
    def __div__(self, other):
        if(isinstance(self,People) == False or isinstance(other, People) == False):
            raise TypeError
        return("{0} swings a lightsaber at {1}.".format(self.name, other.name)) 
    
    def __mul__(self, other):
        if(isinstance(self,People) == False or isinstance(other, People) == False):
            raise TypeError
        return("{0} throws a thermal detonator at {1}!".format(self.name, other.name))
        
    def __rshift__(self, other):
        if(isinstance(self,People) == False or isinstance(other, People) == False):
            raise TypeError
        return("{0} uses the force to push {1} away from them.".format(self.name, other.name))
        
    def __lshift__(self, other):
        if(isinstance(self,People) == False or isinstance(other, People) == False):
            raise TypeError
        return("{0} uses the force to pull {1} towards them.".format(self.name, other.name))
        
    def __neg__(self):
        self.dark_side = True
        self.light_side = False
        
    def __pos__(self):
        self.dark_side = False
        self.light_side = True
        
    def __invert__(self):
        self.dark_side = not self.dark_side
        self.light_side = not self.light_side

    def __xor__(self, other):
        return("{0} force chokes {1}.".format(self.name, other.name))
        
    def __eq__(self, other):
        if (other.name == "Han Solo"):
            return("{0} shoots {1}. BECAUSE HAN SHOOTS FIRST.".format(other.name, self.name))
        else:
            return("{0} shoots {1}.".format(self.name, other.name))
        
    
