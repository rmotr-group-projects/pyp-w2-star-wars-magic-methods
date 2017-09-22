class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
        
    @property
    def color(self):
        return (self.red, self.green, self.blue)
        
    def __eq__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            if self.color == secondParm.color:
                return True
        else:
            return False
            
    def __add__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            color = secondParm.color
        
        elif isinstance(secondParm, tuple):
            color = secondParm
        else:
            raise TypeError()
            
        newCrystal = SaberCrystal(color = self.add_color(color))
        return newCrystal
        
    def add_color(self, color):
        red = color[0]
        green = color[1]
        blue = color[2]
        
        addedColor = (self.red + red if self.red + red <= 255 else 255, 
                        self.green + green if self.green + green <= 255 else 255, 
                        self.blue + blue if self.blue + blue <= 255 else 255)
        return addedColor
        
    def __iadd__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            color = secondParm.color
        
        elif isinstance(secondParm, tuple):
            color = secondParm
        else:
            raise TypeError()
        
        self.red, self.green, self.blue = self.add_color(color)
        
        return self
        
        
    def __sub__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            color = secondParm.color
        
        elif isinstance(secondParm, tuple):
            color = secondParm
        else:
            raise TypeError()
            
        newCrystal = SaberCrystal(color = self.sub_color(color))
        return newCrystal
        
    def sub_color(self, color):
        red = color[0]
        green = color[1]
        blue = color[2]
        
        addedColor = (self.red - red if self.red - red >= 0 else 0, 
                        self.green - green if self.green - green >= 0 else 0, 
                        self.blue - blue if self.blue - blue >= 0 else 0)
        return addedColor 
        
    def __isub__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            color = secondParm.color
        
        elif isinstance(secondParm, tuple):
            color = secondParm
        else:
            raise TypeError()
        
        self.red, self.green, self.blue = self.sub_color(color)
        
        return self
            
    def __contains__(self, secondParm):
        if isinstance(secondParm, SaberCrystal):
            color = secondParm.color
        
        elif isinstance(secondParm, tuple):
            color = secondParm
        else:
            raise TypeError()
        
        if all((color[0] <= self.red, color[1] <= self.green, color[2] <= self.blue)):
            return True
        else:
            return False