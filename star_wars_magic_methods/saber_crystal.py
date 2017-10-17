class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color

    def __add__(self,other):
        if isinstance(other, SaberCrystal):
            add_crystal = tuple(map(lambda x,y: min(x + y, 255), self.color, other.color))
        else:
            add_crystal = tuple(map(lambda x,y: min(x + y, 255), self.color, other))
        return SaberCrystal(color=add_crystal)
    
    def __sub__(self,other):
        if isinstance(other, SaberCrystal):
            sub_crystal = tuple(map(lambda x,y: x - y, self.color, other.color))
        else:
            sub_crystal = tuple(map(lambda x,y: x - y, self.color, other))
        return SaberCrystal(color=sub_crystal)
    
    def __eq__(self,other):
        if self.color == other.color:
            return True
        else:
            return False
    
    def __contains__(self,other):
        sub_crystal = self - other
        if any(x < 0 for x in sub_crystal.color):
            return False
        else:
            return True
    
    @property
    def red(self):
        return self.color[0]
    
    @property
    def green(self):
        return self.color[1]
        
    @property
    def blue(self):
        return self.color[2]
    
    
    