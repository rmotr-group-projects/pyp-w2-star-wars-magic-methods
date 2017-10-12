class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not self.dark_side
        
    def __call__(self):
      if self.name == 'Obi-Wan Kenobi':
          return ("Help me Obi-Wan Kenobi, you're my only hope.")    
    
    def __invert__(self):
        self.dark_side = not self.dark_side
        self.light_side = not self.light_side
    
    def __pos__(self):
        self.dark_side = False
        self.light_side = True
    
    def __neg__(self):
        self.dark_side = True
        self.light_side = False
    
    def __str__(self):
        return self.name
    
    def __div__(self, other):
        if not isinstance(other, People):
            raise TypeError
        return self.name + " swings a lightsaber at " + other.name + "."
      
    def __mul__(self, other):
        if not isinstance(other, People):
            raise TypeError
        return self.name + " throws a thermal detonator at " + other.name + "!"
      
    def __rshift__(self, other):
        if not isinstance(other, People):
            raise TypeError
        return self.name + " uses the force to push " + other.name  + " away from them."    
       
    def __lshift__(self, other):
        if not isinstance(other, People):
            raise TypeError
        return self.name + " uses the force to pull " + other.name + " towards them."
      
    def __xor__(self, other):
      return self.name + " force chokes " + other.name + "."
      
    def __eq__(self, other):
      if other.name == 'Han Solo':
        return other.name + " shoots " + self.name + ". BECAUSE " + other.name.split(" ")[0].upper() + " SHOOTS FIRST."
      return self.name + " shoots " + other.name + "."  