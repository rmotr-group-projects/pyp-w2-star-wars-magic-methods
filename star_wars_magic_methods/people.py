
# Function to print Geeco and Han
def format_people(obj, other):
    return "{} shoots {}.".format(obj, other)

class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me {}, you're my only hope.".format(self) 
    
    @property
    def light_side(self):
        if self.dark_side == False:
            return True
        return False
    
    def __neg__(self):
        if self.dark_side:
            self.dark_side = False
        else:
            self.dark_side = True
    
    def __invert__(self):
        self.__neg__()
    
    def __pos__(self):
        self.__neg__()
        
    def __xor__(self, other):
        return "{} force chokes {}.".format(self, other)
    
    
    def __lshift__(self, other):
        return "{} uses the force to pull {} towards them.".format(self, other)
    
    def __rshift__(self, other):
        if isinstance(other, People):
            return "{} uses the force to push {} away from them.".format(self, other)
        raise TypeError()
    
    def __div__(self, other):
        if isinstance(other, People):
            return "{} swings a lightsaber at {}.".format(self, other)
        raise TypeError()
    
    __truediv__ = __div__
    
    def __mul__(self, other):
        if isinstance(other, People):
            return "{} throws a thermal detonator at {}!".format(self, other)
        raise TypeError()
    
    # Method using a function to format people objects
    def __eq__(self, other):
        text = format_people(other, self) + " BECAUSE HAN SHOOTS FIRST." \
                    if other.name == "Han Solo" else format_people(self, other)
        return text

    
        
    
