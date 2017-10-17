class People(object):

    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark = dark_side
       
    def __call__(self):
        return 'Help me {sName}, you\'re my only hope.'.format(
                sName = self.name)
    
    def __neg__(self):
        self.dark = True
    
    def __pos__(self):
        self.dark = False
    
    def __invert__(self):
        if self.dark == False:
            self.dark = True
        else:
            self.dark = False
    
    def __str__(self):
        return str(self.name)
    
    def __truediv__(self, other):
        if isinstance(other, People):
            return '{sName} swings a lightsaber at {oName}.'.format(
                sName = self.name,
                oName = other.name)
        else:
            raise TypeError
            
    __div__ = __truediv__
        
    def __mul__(self, other):
        if isinstance(other, People):
            return '{sName} throws a thermal detonator at {oName}!'.format(
                sName = self.name,
                oName = other.name)
        else:
            raise TypeError
            
    def __rshift__(self, other):
        if isinstance(other, People):
            return '{sName} uses the force to push {oName} away from them.'.format(
                sName = self.name,
                oName = other.name)
        else:
            raise TypeError

    def __lshift__(self, other):
        if isinstance(other, People):
            return '{sName} uses the force to pull {oName} towards them.'.format(
                sName = self.name,
                oName = other.name)
        else:
            raise TypeError
    
    def __eq__(self, other):
        if other.name == 'Han Solo':
            return '{oName} shoots {sName}. BECAUSE HAN SHOOTS FIRST.'.format(
                sName = self.name,
                oName = other.name)
        else:
            return '{sName} shoots {oName}.'.format(
                sName = self.name,
                oName = other.name)
    
    def __xor__(self, other):
        return '{sName} force chokes {oName}.'.format(
            sName = self.name,
            oName = other.name)
    
    @property
    def light_side(self):
        if self.dark == False:
            return True
        else:
            return False
    
    @property
    def dark_side(self):
        return self.dark