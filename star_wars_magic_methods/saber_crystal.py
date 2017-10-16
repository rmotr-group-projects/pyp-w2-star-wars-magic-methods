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
            other = SaberCrystal(color=other)
        return SaberCrystal(
            color=(
                min(self.red + other.red, 255),
                min(self.green + other.green, 255),
                min(self.blue + other.blue, 255),
            ),
        )

    def __iadd__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(color=other)
        self.red = min(self.red + other.red, 255)
        self.green = min(self.green + other.green, 255) 
        self.blue = min(self.blue + other.blue, 255)
        return self
        
    def __sub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(color=other)
        return SaberCrystal(
            color=(
                max(self.red - other.red, 0),
                max(self.green - other.green, 0),
                max(self.blue - other.blue, 0),
            ),
        )

    def __isub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(color=other)
        self.red = max(self.red - other.red, 0)
        self.green = max(self.green - other.green, 0) 
        self.blue = max(self.blue - other.blue, 0)
        return self
        
    def __contains__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(color=other)
        return self.red >= other.red and self.green >= other.green and self.blue >= other.blue
        
        