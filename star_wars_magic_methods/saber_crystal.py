#import pdb; pdb.set_trace()

class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __eq__(self, other):
        if self.color == other.color:
            return True
    
    def __add__(self, other):
        
        red = other.red if isinstance(other, SaberCrystal) else other[0]
        green = other.green if isinstance(other, SaberCrystal) else other[1]
        blue = other.blue if isinstance(other, SaberCrystal) else other[2]
        
        new_red = self.red + red
        if new_red > 255:
            new_red = 255
        new_green = self.green + green
        if new_green > 255:
            new_green = 255
        new_blue = self.blue + blue
        if new_blue > 255:
            new_blue = 255
            
        thing = SaberCrystal(color=(new_red, new_green, new_blue))
        
        return thing
    
    def __iadd(self, other):
        
        red = other.red if isinstance(other, SaberCrystal) else other[0]
        green = other.green if isinstance(other, SaberCrystal) else other[1]
        blue = other.blue if isinstance(other, SaberCrystal) else other[2]
    
        new_red = self.red + red
        if new_red > 255:
            new_red = 255
        new_green = self.green + green
        if new_green > 255:
            new_green = 255
        new_blue = self.blue + blue
        if new_blue > 255:
            new_blue = 255
            
        thing = SaberCrystal(color=(new_red, new_green, new_blue))
        
        return thing
    
    def __sub__(self, other):
        
        red = other.red if isinstance(other, SaberCrystal) else other[0]
        green = other.green if isinstance(other, SaberCrystal) else other[1]
        blue = other.blue if isinstance(other, SaberCrystal) else other[2]
        
        new_red = self.red - red
        if new_red <= 0:
            new_red = 0
        new_green = self.green - green
        if new_green <= 0:
            new_green = 0
        new_blue = self.blue - blue
        if new_blue <= 0:
            new_blue = 0
            
        thing = SaberCrystal(color=(new_red, new_green, new_blue))
        
        return thing

    def __isub__(self, other):
        
        red = other.red if isinstance(other, SaberCrystal) else other[0]
        green = other.green if isinstance(other, SaberCrystal) else other[1]
        blue = other.blue if isinstance(other, SaberCrystal) else other[2]
        
        new_red = self.red - red
        if new_red <= 0:
            new_red = 0
        new_green = self.green - green
        if new_green <= 0:
            new_green = 0
        new_blue = self.blue - blue
        if new_blue <= 0:
            new_blue = 0
            
        thing = SaberCrystal(color=(new_red, new_green, new_blue))
        
        return thing
    
    def __contains__(self, other):
        
        red = other.red if isinstance(other, SaberCrystal) else other[0]
        green = other.green if isinstance(other, SaberCrystal) else other[1]
        blue = other.blue if isinstance(other, SaberCrystal) else other[2]
        
        if self.red >= red and self.green >= green and self.blue >= blue:
            return True
        else: 
            return False
            
        