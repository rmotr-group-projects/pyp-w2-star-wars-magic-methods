class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
    
    def __eq__(self, other):
        return self.color == other.color
    
    def __add__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = min(self.color[i] + other.color[i], 255)
            
        return SaberCrystal(tuple(new_color))
    
    def __sub__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        new_color = [0,0,0]
        for i in range(0, 3):
            new_color[i] = max(self.color[i] - other.color[i], 0)
            
        return SaberCrystal(tuple(new_color))
    
    def __contains__(self, other):
        if not isinstance(other, SaberCrystal):
            other = SaberCrystal(other)
            
        return all([(s_col >= o_col) for s_col, o_col in zip(self.color,other.color)])