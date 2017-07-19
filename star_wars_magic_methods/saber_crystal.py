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
        newCrystal = SaberCrystal(color = (0,0,0))
        if (isinstance(other, SaberCrystal)):
            newCrystal.red = self.red + other.red
            newCrystal.green = self.green + other.green
            newCrystal.blue = self.blue + other.blue
        else:
            newCrystal.red = self.red + other[0]
            newCrystal.green = self.green + other[1]
            newCrystal.blue = self.blue + other[2]
            
        return newCrystal
            
                
    def __iadd__(self, other):
        if (isinstance(other, SaberCrystal)):
            self.red += other.red
            self.green += other.green
            self.blue += other.blue
        else:
            self.red += other[0]
            self.green += other[1]
            self.blue += other[2]
        
        return self
    
    def __sub__(self, other):
        newCrystal = SaberCrystal(color = (0,0,0))
        if (isinstance(other, SaberCrystal)):
            newCrystal.red = self.red - other.red
            newCrystal.green = self.green - other.green
            newCrystal.blue = self.blue - other.blue
        else:
            newCrystal.red = self.red - other[0]
            newCrystal.green = self.green - other[1]
            newCrystal.blue = self.blue - other[2]
            
        return newCrystal
                
    def __isub__(self, other):
        if (isinstance(other, SaberCrystal)):
            self.red -= other.red
            self.green -= other.green
            self.blue -= other.blue
        else:
            self.red -= other[0]
            self.green -= other[1]
            self.blue -= other[2]
        
        return self
                
    def __contains__(self, other):
        if (isinstance(other, SaberCrystal)):
            return(self.red >= other.red and self.green >= other.green and self.blue >= other.blue)
        else:
            return(self.red >= other[0] and self.green >= other[1] and self.blue >= other[2])
            
