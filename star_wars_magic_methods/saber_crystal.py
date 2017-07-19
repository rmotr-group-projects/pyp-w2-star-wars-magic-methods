class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red=color[0]
        self.green=color[1]
        self.blue=color[2]
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)
        
    def __eq__(self,other):
        return self.color == other.color
    
    def __add__(self,other):
        if isinstance(other,SaberCrystal):
            return SaberCrystal(color = (self.red+other.red, self.green + other.green, self.blue + other.blue))
        else:
            return SaberCrystal(color = (self.red+other[0], self.green+other[1],self.blue+other[2]))
            
    def __sub__(self,other):
        if isinstance(other,SaberCrystal):
            return SaberCrystal(color = (self.red-other.red, self.green-other.green, self.blue-other.blue))
        else:
            return SaberCrystal(color = (self.red-other[0], self.green-other[1],self.blue-other[2]))
