class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self._red = color[0]
        self._green = color[1]
        self._blue = color[2]

    def __contains__(self, other):
        r1,g1,b1 = other.color if isinstance(other,SaberCrystal) else other
        r2,g2,b2 = self.color if isinstance(self,SaberCrystal) else self
        if r1 <= r2 and g1 <= g2 and b1 <= b2:
            return True
        return False

    @property
    def color(self):
        return (self._red,self._green,self._blue)

    @color.setter
    def color(self,value):
        self._red = value[0]
        self._green = value[1]
        self._blue = value[2]

    @property
    def red(self):
        return self._red
    @property
    def green(self):
        return self._green
    @property
    def blue(self):
        return self._blue

    def __eq__(self,other):
        return self.color == other.color

    def __add__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        if (r1,g1,b1) == (255,255,255):
            return self
        elif (r2,g2,b2) ==  (255,255,255):
            return other
        return SaberCrystal(color=(r1+r2,g1+g2,b1+b2))

    def __iadd__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        if (r1,g1,b1) == (255,255,255):
            return self
        elif (r2,g2,b2) ==  (255,255,255):
            return other
        self.color = (r1+r2,g1+g2,b1+b2)
        return self

    def __sub__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        return SaberCrystal(color=(r1-r2,g1-g2,b1-b2))

    def __isub__(self,other):
        r1,g1,b1 = self.color if isinstance(self,SaberCrystal) else self
        r2,g2,b2 = other.color if isinstance(other,SaberCrystal) else other
        self.color = (r1-r2,g1-g2,b1-b2)
        return self
