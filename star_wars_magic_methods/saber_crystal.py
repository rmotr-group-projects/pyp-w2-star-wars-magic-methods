class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    def __str__(self):
        return self.color
    
    def __eq__(self, other):
        if isinstance(other, SaberCrystal):
            return self.color == other.color
        else:
            raise TypeError()
        
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            red = self.red + other.red
            green = self.green + other.green
            blue = self.blue + other.blue
            return (red, green, blue)
        
        elif (isinstance(other, tuple) and len(other) == 3):
            red = self.red + other[0]
            green = self.green + other[1]
            blue = self.blue + other[2]
        
        else:
            raise TypeError