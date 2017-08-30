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
        
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            red_statement = (self.red == other.red if self.red > 0 else False)
            green_statement = (self.green == other.green if self.green > 0 else False)
            blue_statement = (self.blue == other.blue if self.blue > 0 else False)
            
            return red_statement or blue_statement or green_statement

        elif isinstance(other, tuple):
            red_statement = (self.red == other[0] if self.red > 0 else False)
            green_statement = (self.green == other[1] if self.green > 0 else False)
            blue_statement = (self.blue == other[2] if self.blue > 0 else False)

            return red_statement or blue_statement or green_statement
        
        else:
            raise TypeError()
        
        
'''    def __add__(self, *args):
        if isinstance(args, SaberCrystal):
            red = self.red + args.red
            green = self.green + args.green
            blue = self.blue + args.blue
            return (red, green, blue)
        
        elif (isinstance(args, tuple) and len(args) == 3):
            red = self.red + args[0]
            green = self.green + args[1]
            blue = self.blue + args[2]
            return (red, green, blue)
        
        else:
            raise TypeError'''