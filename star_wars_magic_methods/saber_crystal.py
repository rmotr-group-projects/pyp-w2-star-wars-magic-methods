import operator

class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        
        
        
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    @property   
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            first = self.color
            second = other.color
            return SaberCrystal(color = tuple(map(operator.sub, first, second)))
        else:
            first = self.color
            second = other
            return SaberCrystal(color = tuple(map(operator.sub, first, second)))
            
    def __isub__(self, other):
        if isinstance(other, SaberCrystal):
            first = self.color
            second = other.color
            return SaberCrystal(color = tuple(map(operator.sub, first, second)))
        else:
            first = self.color
            second = other
            return SaberCrystal(color = tuple(map(operator.sub, first, second)))
            
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            first = self.color
            second = other.color
            return SaberCrystal(color = tuple(map(operator.add, first, second)))
        else:
            first = self.color
            second = other
            return SaberCrystal(color = tuple(map(operator.add, first, second)))
            
    def __iadd__(self, other):
        first = self.color
        if isinstance(other, SaberCrystal):
            second = other.color
        else:
            second = other
        return SaberCrystal(color = tuple(map(operator.add, first, second)))
        
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            return all((self.red >= other.red, self.green >= other.green, self.blue >= other.blue))
        else:
            return all((self.red >= other[0], self.green >= other[1], self.blue >= other[2]))
        
            
        
        
    def __eq__(self, other):
        if self.color == other.color:
            return True
        else:
            return False
    
    
        
    