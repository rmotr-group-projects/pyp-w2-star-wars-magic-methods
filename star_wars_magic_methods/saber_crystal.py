class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __eq__(self, other):
        if isinstance(other, SaberCrystal):
            return self.color == other.color

    def __add__(self, other):
        if isinstance(other,tuple): # if other is a tuple
            other = SaberCrystal(other) # convert to object. now both self and other are objects
            
        new_color = (
            min(255, self.red + other.red),
            min(255, self.green + other.green),
            min(255, self.blue + other.blue)
            )
        return SaberCrystal(new_color)

    def __sub__(self, other):
        if isinstance(other,tuple):
            other = SaberCrystal(other)
            
        new_color = (
            min(255, self.red - other.red),
            min(255, self.green - other.green),
            min(255, self.blue - other.blue)
            )
        return SaberCrystal(new_color)
    
    def __contains__(self, other):
        if isinstance(other,tuple):
            other = SaberCrystal(other)
            
        # use zip() to convert tuple to list so you can iterate over them
        for x,y in zip(self.color, other.color): 
            if x == y & x != 0:
                return True
                
        return False
    

# red = SaberCrystal()
# green = (0,255,0)
# blue = (0,0,255)
# white = (255,255,255)

# l = red+green
# r = l+blue
# a = red+blue+green

# print('')
# print('----FINAL RESULT----')
# print(a == white)
# print(a.color)