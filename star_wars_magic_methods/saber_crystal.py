class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        checked_color = self.color_check(color) 
        self.red, self.green, self.blue = checked_color
    
    @staticmethod
    def color_check(tuple_in):
        return tuple (map (lambda x: max (min (255, x), 0), tuple_in))
    
    @staticmethod
    def extract_color(input): 
        if isinstance(input, SaberCrystal):
            return input.color
        else: 
            return input

    @property
    def color(self):
        return (self.red, self.green, self.blue)
        
    @color.setter
    def color(self, color_in):
        checked_color = self.color_check(color_in)
        self.red, self.green, self.blue = checked_color
    
    def __eq__(self, other):
        return self.color == other.color

    def add_color(self, other, adj = 1):
        red, green, blue = self.extract_color(other)
        add_red = self.red + (red * adj)
        add_green = self.green + (green * adj)
        add_blue =  self.blue + (blue * adj)
        checked_color = self.color_check((add_red, add_green, add_blue))
        return checked_color
        #other_color = self.extract_color(other)
        #if adj == -1:
        #    other_color = tuple([-item for item in other_color])
        #added_color = tuple([sum(col) for col in list(zip(self.color, other_color))])
        #checked_color = self.color_check(added_color)
        #return checked_color #QUESTION: or would it be poor style to just return self.color_check(added_color)

    def __add__(self, other, adj = 1):
        checked_color = self.add_color(other, adj)
        return SaberCrystal(checked_color)
        
    def __iadd__(self, other, adj = 1):
        checked_color = self.add_color(other, adj)
        self.color = checked_color
        return self

    def __sub__(self, other):
        return self.__add__(other, -1)
        
    def __isub__(self, other):
        return self.__iadd__(other, -1)
        
    def __contains__(self, item):
        red, green, blue = self.extract_color(item)
        if all((self.red >= red, self.green >= green, self.blue >= blue)):
            return True
        else:
            return False
    