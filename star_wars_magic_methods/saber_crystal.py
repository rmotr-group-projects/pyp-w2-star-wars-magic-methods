class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    @color.setter
    def color(self):
        self.color = color
        