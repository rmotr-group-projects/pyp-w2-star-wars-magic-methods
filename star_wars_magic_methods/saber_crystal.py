class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self._color = color
        self.red = self._color[0]
        self.green = self._color[1]
        self.blue = self._color[2]
        
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __eq__(self, other):
        return self.color == other.color
        
    def __add__(self, other):
        if type(other) == tuple:
            other = SaberCrystal((other[0], other[1], other[2]))
        self.red += other.red
        if self.red > 255:
            self.red = 255

        self.green += other.green
        if self.green > 255:
            self.green = 255

        self.blue += other.blue
        if self.blue > 255:
            self.blue = 255
        
        return self

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        if type(other) == tuple:
            other = SaberCrystal((other[0], other[1], other[2]))
        
        self.red -= other.red
        if self.red < 0:
            self.red = 0

        self.green -= other.green
        if self.green < 0:
            self.green = 0
            
        self.blue -= other.blue
        if self.blue < 0:
            self.blue = 0

        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __contains__(self, other):
        if (isinstance(other, SaberCrystal)):
            return(self.red >= other.red and self.green >= other.green and self.blue >= other.blue)
        else:
            return(self.red >= other[0] and self.green >= other[1] and self.blue >= other[2])
            