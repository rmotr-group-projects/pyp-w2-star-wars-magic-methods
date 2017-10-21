class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    def __eq__(self,other):
      return self.color == other.color    
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def add_color(self, other):
        red,blue,green = other[0], other[1], other[2]
        
        if self.red + red <= 255:
          new_red = self.red + red
        else:
          new_red = 255
          
        if self.green + green <= 255:
          new_green = self.green + green
        else:
          new_green = 255
          
        if self.blue + blue <= 255:
          new_blue = self.blue + blue
        else:
          new_blue = 255
          
        new_color = (new_red, new_green, new_blue)
        return new_color 
        
    def __add__(self, other):
        if type(other) == tuple:
            other = SaberCrystal((other[0], other[1], other[2]))
        self.red += other.red
        if self.red >= 255:
            self.red = 255

        self.green += other.green
        if self.green >= 255:
            self.green = 255

        self.blue += other.blue
        if self.blue >= 255:
            self.blue = 255

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
    
    def __contains__(self, other):
        if type(other) == tuple:
            other = SaberCrystal((other[0], other[1], other[2]))
        if self.red == 255 and other.red == 255:
          return True
        if self.green == 255 and other.green == 255:
          return True
        if self.blue  == 255 and other.blue == 255:
          return True
        return False
        