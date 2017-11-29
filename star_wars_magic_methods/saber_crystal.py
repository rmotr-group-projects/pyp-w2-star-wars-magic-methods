class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)
        
    def __eq__(self, other):
        if isinstance(other, SaberCrystal) and self.color == other.color:
            return True
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def _add_color(self, color):
        r, g, b = color
        return (self.red + r if self.red +r  <=255 else 255, 
                self.green + g if self.green + g  <=255 else 255, 
                self.blue + b if self.blue +b <=255 else 255)
    
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError
        return SaberCrystal(self._add_color(color))
        
    __iadd__ = __add__      
        
    def _sub_color(self, color):
        r, g, b = color
        return (self.red - r if self.red - r >=0 else 0, 
                self.green - g if self.green - g >=0 else 0,
                self.blue - b if self.blue - b >=0 else 0)

    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError
        return SaberCrystal(self._sub_color(color))
        
    __isub__ = __sub__

    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError
        r, g, b = color
        if all((r <= self.red,
                g <= self.green,
                b <= self.blue)):
            return True
        else:
            return False        