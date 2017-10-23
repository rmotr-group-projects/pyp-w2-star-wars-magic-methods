def valid_color(other):
    if isinstance(other, tuple) and len(other) == 3:
        if other[0] <= 0:
            x = 0
        elif other[0] >= 255:
            x = 255
        else:
            x = other[0]

        if other[1] <= 0:
            y = 0
        elif other[1] >= 255:
            y = 255
        else:
            y = other[1]

        if other[2] <= 0:
            z = 0
        elif other[2] >= 255:
            z = 255
        else:
            z = other[2]

        return x, y, z

    return 0, 0, 0
    
    
class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.colors = valid_color(color)
        self.red = self.colors[0]
        self.green = self.colors[1]
        self.blue = self.colors[2]
    
    @property
    def color(self):
        return valid_color(self.colors)
    
    def __eq__(self, other):
        if isinstance(other, SaberCrystal):
            return self.colors == valid_color(other.colors)
        return False
    
    
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            colors = other
        elif isinstance(other, tuple):
            colors = SaberCrystal(other)
        
        x = self.red + colors.red
        y = self.green + colors.green
        z = self.blue + colors.blue

        return SaberCrystal(color=(x,y,z))
    
    def __iadd(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            colors = other
        elif isinstance(other, tuple):
            colors = SaberCrystal(other)
        
        x = self.red - colors.red
        y = self.green - colors.green
        z = self.blue - colors.blue

        return SaberCrystal(color=(x,y,z))
    
    def __isub__(self, other):
        return self.__sub__(other)
        
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            colors = other
        elif isinstance(other, tuple):
            colors = SaberCrystal(other)

        #if all(i >= j for i, j in zip(self.color, colors.color)): # This solution work well too!
        if all(self.color[i] >= colors.color[i] for i in range(len(self.color))):
            return True
        return False
