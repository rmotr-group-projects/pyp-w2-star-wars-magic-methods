
class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.eq_message = None
    
    @property
    def light_side(self):
        if self.dark_side == False:
            return True
        else:
            return False
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me " + self.name + ", you're my only hope."

    
    def __div__(self, other):
        if isinstance(other, People):
            return self.name + ' swings a lightsaber at ' + other.name + '.'
        else:
            raise TypeError
    __truediv__ = __div__
    
    def __mul__(self, other):
        if isinstance(other, People):
            return self.name + ' throws a thermal detonator at ' + other.name + '!'
        else:
            raise TypeError

    def __rshift__(self, other):
        if isinstance(other, People):
            return self.name + ' uses the force to push ' + other.name + ' away from them.'
        else:
            raise TypeError
    
    def __lshift__(self, other):
        if isinstance(other, People):
            return self.name + ' uses the force to pull ' + other.name + ' towards them.'
        else:
            raise TypeError

    def __neg__(self):
        self.dark_side = True

    def __pos__(self):
        self.dark_side = False
        
    def __invert__(self): 
        if self.dark_side == False:
            self.dark_side = True
        else:
            self.dark_side = False
    
    def __xor__(self, other):
        if isinstance(other, People):
            return self.name + ' force chokes ' + other.name + '.'
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, People):
            if self.eq_message == None:
                self.eq_message = self.name + ' shoots ' + other.name + '.'
            if other.eq_message != None:
                first_name_caps = other.name.split()[0].upper()
                second_message = ' BECAUSE ' + first_name_caps + ' SHOOTS FIRST.'
                self.eq_message = other.eq_message + second_message
            return self.eq_message

        else:
            raise TypeError
