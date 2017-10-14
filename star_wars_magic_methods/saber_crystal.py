class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
    
    @property
    def red(self):
        return self.color[0]
    
    @property
    def green(self):
        return self.color[1]
    
    @property
    def blue(self):
        return self.color[2]
    
    @classmethod
    def safe_rgb_addition(self, val1, val2):
        ret = val1 + val2
        if ret > 255:
            ret = 255
        return ret
    
    @classmethod
    def safe_rgb_subtraction(self, val1, val2):
        ret = val1 - val2
        if ret < 0:
            ret = 0
        return ret
    
    def __eq__(self, other):
        return (self.red == other.red and self.green == other.green and self.blue == other.blue)
    
    @classmethod
    def add_rgb_tuples(self, tuple1, tuple2):
        return tuple([SaberCrystal.safe_rgb_addition(*x) for x in zip(tuple1, tuple2)])
    
    @classmethod
    def subtract_rgb_tuples(self, tuple1, tuple2):
        return tuple([SaberCrystal.safe_rgb_subtraction(*x) for x in zip(tuple1, tuple2)])
        
    def __add__(self, other):
        if isinstance(other, tuple):
            otherTuple = other
        elif isinstance(other, SaberCrystal):
            otherTuple = other.color
        else:
            raise TypeError
        return SaberCrystal(color=SaberCrystal.add_rgb_tuples(self.color, otherTuple))
        
    def __sub__(self, other):
        if isinstance(other, tuple):
            otherTuple = other
        elif isinstance(other, SaberCrystal):
            otherTuple = other.color
        else:
            raise TypeError
        return SaberCrystal(color=SaberCrystal.subtract_rgb_tuples(self.color, otherTuple))
    
    def __iter__(self):
        self.position = 0
        return self
        
    def next(self):
        if self.position >= len(self.color):
            raise StopIteration
        ret = self.color[self.position]
        self.position +=1
        return ret
    
    __next__ = next
    
    def __contains__(self, value):
        for v, s in zip(value, self.color):
            if v > s:
                return False
        return True
        
        