class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    def __eq__(self, other):
        return all([self.red == other.red, self.green == other.green, self.blue == other.blue])
    
    def __add__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
        
        new_color = map(lambda x, y: min(x + y, 255), self.color, other.color)
        
        return SaberCrystal(tuple(new_color))

    def __iadd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
        
        new_color = map(lambda x, y: max(x - y, 0), self.color, other.color)
        
        return SaberCrystal(tuple(new_color))
        
    def __isub__(self, other):
        return self.__sub__(other)
        
    def __contains__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
 
        return all([self.red >= other.red, self.green >= other.green, self.blue >= other.blue])
