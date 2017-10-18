class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self._red = color[0]
        self._green = color[1]
        self._blue = color[2]

    @property
    def color(self):
        return (self._red,self._green,self._blue)

    @color.setter
    def color(self,value):
        self._red = value[0]
        self._green = value[1]
        self._blue = value[2]

    def __eq__(self,other):
        return self.color == other.color

    def __add__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        return SaberCrystal(color=(r1+r2,g1+g2,b1+b2))

    def __iadd__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        self.color = (r1+r2,g1+g2,b1+b2)

    def __sub__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        return SaberCrystal(color=(r1-r2,g1-g2,b1-b2))

    def __isub__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        self.color = (r1-r2,g1-g2,b1-b2)

white_crystal = SaberCrystal(color=(255,255,255))
red_crystal = SaberCrystal()
print(white_crystal.color)
print(red_crystal.color)
red_crystal += white_crystal
#assert red_crystal == white_crystal
