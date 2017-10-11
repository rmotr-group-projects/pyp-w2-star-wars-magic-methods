#Init should take one optional parameter, color, which defaults to (255,0,0), which is a tuple representing red, green, blue. There should be 3 instance attributes, red, green, and blue. There needs to also be a property color that returns a tuple with the values of red, green, and blue Finally you need to implement methods for the following operators: equality ==, addition +, in place addition +=, subtraction -, in place subtraction -=, and contains x in y
class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    def __eq__(self, other):
        return self.color == other.color
    
    def __add__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = min(self.color[i] + other.color[i], 255)
            
        return SaberCrystal(tuple(new_color))
    
    def __iadd__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        self.red = min(self.red + other.red, 255)
        self.green = min(self.green + other.green, 255)
        self.blue = min(self.blue + other.blue, 255)
        self.color = (self.red, self.green, self.blue)
        return self
    
    def __sub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = max(self.color[i] - other.color[i], 0)
            
        return SaberCrystal(tuple(new_color))
    
    def __isub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        self.red = max(self.red - other.red, 0)
        self.green = max(self.green - other.green, 0)
        self.blue = max(self.blue - other.blue, 0)
        self.color = (self.red, self.green, self.blue)
        return self
    
    def __contains__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        return all([(s_col >= o_col) for s_col, o_col in zip(self.color,other.color)])