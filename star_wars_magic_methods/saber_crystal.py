class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    def __str__(self):
        return str(self.color)
    
    def __eq__(self, other):
        if isinstance(other, SaberCrystal):
            return self.color == other.color
        else:
            raise TypeError()
        
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            red_statement = (self.red == other.red if self.red > 0 else False)
            green_statement = (self.green == other.green if self.green > 0 else False)
            blue_statement = (self.blue == other.blue if self.blue > 0 else False)
            
            return red_statement or blue_statement or green_statement

        elif isinstance(other, tuple) and len(other) == 3:
            red_statement = (self.red == other[0] if self.red > 0 else False)
            green_statement = (self.green == other[1] if self.green > 0 else False)
            blue_statement = (self.blue == other[2] if self.blue > 0 else False)

            return red_statement or blue_statement or green_statement
        
        else:
            raise TypeError()
        
    
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            red = self.red + other.red 
            if red > 255:
                red = 255
            
            green = self.green + other.green
            if green > 255:
                green = 255
                
            blue = self.blue + other.blue
            if blue > 255:
                blue = 255
            
            new_object = SaberCrystal(color = (red, green, blue))
            return new_object
        
        elif isinstance(other, tuple) and len(other) == 3:
            red = self.red + other[0]
            green = self.green + other[1]
            blue = self.blue + other[2]
            
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
                
            new_object = SaberCrystal(color = (red, green, blue))
            return new_object
        
        else:
            raise TypeError

    
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            red = self.red - other.red 
            if red < 0:
                red = 0
            
            green = self.green - other.green
            if green < 0:
                green = 0
                
            blue = self.blue - other.blue
            if blue < 0:
                blue = 0
            
            new_object = SaberCrystal(color = (red, green, blue))
            return new_object
        
        elif isinstance(other, tuple) and len(other) == 3:
            red = self.red + other[0]
            green = self.green + other[1]
            blue = self.blue + other[2]
            
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
                
            new_object = SaberCrystal(color = (red, green, blue))
            return new_object
        
        else:
            raise TypeError