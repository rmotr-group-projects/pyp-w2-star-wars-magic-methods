"""rmotr.com Advanced Programming - Practice magic methods and properties using 
a class representing a Person in the Star Wars universe."""

class People(object):
    """A person in the Star Wars universe."""
    def __init__(self, name, dark_side=False):
        self.name = name
        
        # Setting the properties will automaically perform error checking in setter
        self.dark_side = dark_side
        self.light_side = not dark_side
        
    @property
    def dark_side(self):
        return self._dark_side
        
    @dark_side.setter
    def dark_side(self, value):
        if type(value) is not bool:
            raise ValueError("dark_side must be type boolean.")
        self._dark_side = value
        self._light_side = not value
    
    @property
    def light_side(self):
        return self._light_side
    
    @light_side.setter
    def light_side(self, value):
        if type(value) is not bool:
            raise ValueError("light_side must be type boolean.")
        self._light_side = value
        self._dark_side = not value
        
    def __check_for_people_instance(self, other, message):
        if not isinstance(other, People):
            raise TypeError(message)
    
    def __call__(self):
        """Call out for help."""
        return "Help me " + self.name + ", you're my only hope."
    
    def __div__(self, other):
        """Swing lightsaber at someone."""
        self.__check_for_people_instance(other, 'must swing lightsaber at another person')
        return self.name + ' swings a lightsaber at ' + other.name + '.'
    
    __truediv__ = __div__
        
    def __eq__(self, other):
        """Shoot someone... unless that 'someone' is Han Solo."""
        if other.name.lower() == 'han solo':
            return other.name + ' shoots ' + self.name + '. BECAUSE HAN SHOOTS FIRST.'
        return self.name + ' shoots ' + other.name + '.' 
        
    def __invert__(self):
        """Switch to the other side of the force."""
        self.dark_side = not self.dark_side

    def __lshift__(self, other):
        """Use force pull on someone."""
        self.__check_for_people_instance(other, 'must use force pull on another person')
        return self.name + ' uses the force to pull ' + other.name + ' towards them.'
        
    def __mul__(self, other):
        """Throw a thermal detonator at someone."""
        self.__check_for_people_instance(other, 'must throw thermal detonator at another person')
        return self.name + ' throws a thermal detonator at ' + other.name + '!'

    def __neg__(self):
        """Switch to the dark side."""
        self.dark_side = True
        
    def __pos__(self):
        """Switch to the light side."""
        self.dark_side = False
    
    def __rshift__(self, other):
        """Use force push on someone."""
        self.__check_for_people_instance(other, 'must use force push on another person')
        return self.name + ' uses the force to push ' + other.name + ' away from them.'
    
    def __str__(self):
        """Return person's name."""
        return self.name
        
    def __xor__(self, other):
        """Force choke someone."""
        self.__check_for_people_instance(other, 'must use force choke on another person')
        return self.name + ' force chokes ' + other.name + '.'
