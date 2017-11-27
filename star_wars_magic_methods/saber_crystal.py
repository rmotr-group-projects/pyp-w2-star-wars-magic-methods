"""rmotr.com Advanced Programming - Practice magic methods and properties using 
a class representing a SaberCrystal in the Star Wars universe."""

class SaberCrystal(object):
    """Power-source of a lightsaber."""
    def __init__(self, color=(255,0,0)):
        # Setting the color property will automaically perform error checking in color.setter
        self.color = color
        
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    @color.setter
    def color(self, value):
        self.__check_argument(value)
        self.red = value[0]
        self.green = value[1]
        self.blue = value[2]
        
    def __check_argument(self, argument):
        """Check SaberCrystal's optional argument - tuple of 
        length 3 containing only integers from 0 to 255."""
        if not isinstance(argument, tuple):
            raise ValueError("color argument must be a tuple.")
        if len(argument) != 3:
            raise ValueError("color argument tuple must have length of 3.")
        for elem in argument:
            if type(elem) != int:
                raise ValueError("elements in color argument tuple must be integers.")
            if elem > 255 or elem < 0:
                raise ValueError("integers in color argument tuple must be between 0 and 255.")
    
    def __validate_other(self, other):
        if isinstance(other, SaberCrystal):
            return other.color
        elif isinstance(other, tuple):
            return other
        else:
            raise ValueError('other type must be SaberCrystal or tuple')
    
    def __add__(self, other):
        """Return sum of 2 tuples representing new SaberCrystal color."""
        new_color = []
        other_tuple = self.__validate_other(other)
        for num1, num2 in zip(self.color, other_tuple):
            if num1 + num2 > 255:
                new_color.append(255)
            else:
                new_color.append(num1 + num2)
        return SaberCrystal(tuple(new_color))

    def __contains__(self, other):
        """Return true if a color tuple is a subset of another color tuple."""
        other_tuple = self.__validate_other(other)
        for num1, num2 in zip(self.color, other_tuple):
            if num2 > num1:
                return False
        return True
    
    def __eq__(self, other):
        """Return true if two SaberCrystal objects' colors are equal."""
        return self.color == other.color
    
    def __iadd__(self, other):
        """Add external color parameters to current object's color."""
        new_color = []
        other_tuple = self.__validate_other(other)
        for num1, num2 in zip(self.color, other_tuple):
            if num1 + num2 > 255:
                new_color.append(255)
            else:
                new_color.append(num1 + num2)
        self.color = tuple(new_color)
        return self
        
    def __isub__(self, other):
        """Subtract external color parameters to current object's color."""
        new_color = []
        other_tuple = self.__validate_other(other)
        for num1, num2 in zip(self.color, other_tuple):
            if num1 - num2 < 0:
                new_color.append(0)
            else:
                new_color.append(num1 - num2)
        self.color = tuple(new_color)
        return self
        
    def __sub__(self, other):
        """Return difference of 2 tuples representing new SaberCrystal color."""
        new_color = []
        other_tuple = self.__validate_other(other)
        for num1, num2 in zip(self.color, other_tuple):
            if num1 - num2 < 0:
                new_color.append(0)
            else:
                new_color.append(num1 - num2)
        return SaberCrystal(tuple(new_color))
