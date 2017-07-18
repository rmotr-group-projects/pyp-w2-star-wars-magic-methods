class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        
        self.color = color
        
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    def __add__(self, other):
        col = []
        for i in range(len(self.color)):
            col.append(self.color[i] + other.color[i])
        return tuple(col)
    
        
        
    