class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __eq__(self, other):
        return self.color == other.color
    
    def __add__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = min(self.color[i] + other.color[i], 255)
  
        return SaberCrystal(tuple(new_color))
    
    def __iadd(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = max(self.color[i] - other.color[i], 0)
  
        return SaberCrystal(tuple(new_color))
    
    def __isub(self, other):
        return self.__sub__(other)
        
    def __contains__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(color=other)

        return self.red >= other.red and self.green >= other.green and self.blue >= other.blue
