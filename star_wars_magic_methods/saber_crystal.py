class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    @property
    def color(self):
        return(self.red, self.green, self.blue)
    
    def __eq__(self, other):
        if isinstance(other, SaberCrystal):
            return self.color == other.color 
        else:
            return False
            
    def __ne__(self, other):
        return not self.__eq__(other)
    
    
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError()
        return SaberCrystal(color=self._color_add(color))
    
    def __iadd__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError()
        self.red, self.green, self.blue = self._color_add(color)
        return self
    
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError()
        return SaberCrystal(color=self._color_sub(color))
    
    def __isub(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError()
        self.red, self.green, self.blue = self._color_sub(color)
        return self
    
    def _color_sub(self, color):
        red, green, blue = color
        new_color = (self.red - red if self.red + red >= 0 else 0,
                    self.green - green if self.green + green >= 0 else 0,
                    self.blue - blue if self.blue + blue >= 0 else 0)
        return new_color
    
    def _color_add(self, color):
        red, green, blue = color 
        new_color = (self.red + red if self.red + red <= 255 else 255,
                    self.green + green if self.green + green <= 255 else 255,
                    self.blue + blue if self.blue + blue <= 255 else 255)
        return new_color
    
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            color = other.color
        elif isinstance(other, tuple):
            color = other
        else:
            raise TypeError()
        red, green, blue = color
        if all((red <= self.red,
                green <= self.green,
                blue <= self.blue)):
            return True
        else:
            return False
    
red_crystal = SaberCrystal()
green = (0,255,0)
green_crystal = SaberCrystal(color=green)
blue = (0,0,255)
blue_crystal = SaberCrystal(color=blue)
white_crystal = SaberCrystal(color=(255,255,255))
print(red_crystal.color)