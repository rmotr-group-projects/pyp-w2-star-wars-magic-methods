class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
   
    @property
    def light_side(self):
        return not self._dark_side
        
    @property
    def dark_side(self):
        return self._dark_side
        
        
    def __str__(self):
        return self.name
        
    def __call__(self):
        return  "Help me {}, you're my only hope.".format(self.__str__())
        
    def __div__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
        
        message = "{self} swings a lightsaber at {secondParm}.".format(
            self=self, secondParm=secondParm)     
        return message 
        
    def __mul__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
        
        message = "{self} throws a thermal detonator at {secondParm}!".format(
            self=self, secondParm=secondParm)     
        return message 

    def __rshift__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
        
        return '{self} uses the force to push {secondParm} away from them.'.format(
            self = self, secondParm = secondParm)

    def __lshift__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
        
        return '{self} uses the force to pull {secondParm} towards them.'.format(
            self = self, secondParm = secondParm)
            
    def __neg__(self):
        self._dark_side = True

    def __pos__(self):
        self._dark_side = False

    def __invert__(self):
        self._dark_side = not self._dark_side
        
    def __xor__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
        
        return "{self} force chokes {secondParm}.".format(self = self,
                                                    secondParm = secondParm)
                                                    
    def __eq__(self, secondParm):
        if not isinstance(secondParm, People):
            raise TypeError()
            
        if self.name == "Han Solo":
            return'Han Solo shoots Greedo.'
        else:
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
