class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    def __eq__(self, other):
        return self.color == other.color
        
    def __add__(self, other):
        
        if type(other) is tuple:
            other = SaberCrystal(other)
        
        red = self.max_min_color(self.red + other.red)
        green = self.max_min_color(self.green + other.green)
        blue = self.max_min_color(self.blue + other.blue)
        color = (red, green, blue)
        return SaberCrystal(color)
        
    def __sub__(self, other):
        
        if type(other) is tuple:
            other = SaberCrystal(other)
        
        red = self.max_min_color(self.red - other.red)
        green = self.max_min_color(self.green - other.green)
        blue = self.max_min_color(self.blue - other.blue)
        color = (red, green, blue)
        return SaberCrystal(color)
        
    def __contains__(self, other):
        
        if type(other) is tuple:
            other = SaberCrystal(other)
        
        for a, b in zip(self.color, other.color):
            if a == b and a != 0:
                return True
                
        return False
        
    def max_min_color(self, color):
        if color > 255:
            return 255
        elif color < 0:
            return 0
        else:
            return color