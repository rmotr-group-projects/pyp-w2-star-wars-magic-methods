class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = 255
        self.green = 0
        self.blue = 0
        
    @property
    def color(self):
        return (self.red,self.green,self.blue)
    
    def __eq__(self, other):
        return self.color == other.color
        
    def __add__(self,other):
        return self.color + other.color
        
        <bYp2i8uLB7jP3izLz8b