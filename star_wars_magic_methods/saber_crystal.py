class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    @property
    def color(self):
        return (self.red, self.green, self.blue)

    def __eq__(self, other):
        other.red = self.red
        other.green = self.green
        other.blue = self.blue
        return other
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index <= 2:
            return_color = self.color[self.index]
            self.index += 1
            return return_color
        else:
            raise StopIteration
    
    def next(self):
        return self.__next__()
    
    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            if (other.red <= self.red) & (other.green <= self.green) & (other.red <= self.red):
                return True
        elif isinstance(other, tuple):
            if (other[0] <= self.color[0]) & (other[1] <= self.color[1]) & (other[2] <= self.color[2]):
                return True
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            red = self.red + other.red
            green = self.green + other.green
            blue = self.blue + other.blue
            return SaberCrystal((red, green, blue))
        elif isinstance(other, tuple):
            red = self.red + other[0]
            green = self.green + other[1]
            blue = self.blue + other[2]
            return SaberCrystal((red, green, blue))
        else: 
            raise TypeError
         
    
    def  __iadd__(self, other):
        if isinstance(other, SaberCrystal):
            self.red += other.red
            self.green += other.green
            self.blue += other.blue
            return self 
        elif isinstance(other, tuple):
            self.red += other[0]
            self.green += other[1]
            self.blue += other[2]
            return self
        else:
            raise TypeError
    
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            red = self.red - other.red
            green = self.green - other.green
            blue = self.blue - other.blue
            return SaberCrystal((red, green, blue))
        elif isinstance(other, tuple):
            red = self.red - other[0]
            green = self.green - other[1]
            blue = self.blue - other[2]
            return SaberCrystal((red, green, blue))
        else: 
            raise TypeError
