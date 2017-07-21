
class SaberCrystal(object):
    
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
       return (self.red, self.green, self.blue)
       
    def __eq__(self, other): 
        return self.color == other.color
        
    
    def __add__(self, other):
        
        if isinstance (other,SaberCrystal): 
            final_crystal_tuple = (self.red + other.red, self.green + other.green, self.blue + other.blue)
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            return final_crystal
        else:
            final_crystal_tuple = (self.red + other[0], self.green + other[1], self.blue + other[2])
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            return final_crystal
    
            
    def __iadd__(self, other): 
        
        if isinstance (other,SaberCrystal): 
            updated_crystal_tuple = (self.red + other.red, self.green + other.green, self.blue + other.blue)
            self.red = updated_crystal_tuple[0]
            self.green = updated_crystal_tuple[1]
            self.blue = updated_crystal_tuple[2]
        else:
            updated_crystal_tuple = (self.red + other[0], self.green + other[1], self.blue + other[2])
            self.red = updated_crystal_tuple[0]
            self.green = updated_crystal_tuple[1]
            self.blue = updated_crystal_tuple[2]
        return self
        
    def __sub__(self, other):
        if isinstance (other,SaberCrystal): 
            final_crystal_tuple = (self.red - other.red, self.green - other.green, self.blue - other.blue)
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            return final_crystal
        else:
            final_crystal_tuple = (self.red - other[0], self.green - other[1], self.blue - other[2])
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            return final_crystal    
    
    def __isub__(self, other): 
        if isinstance (other,SaberCrystal): 
            updated_crystal_tuple = (self.red - other.red, self.green - other.green, self.blue - other.blue)
            self.red = updated_crystal_tuple[0]
            self.green = updated_crystal_tuple[1]
            self.blue = updated_crystal_tuple[2]
        else:
            updated_crystal_tuple = (self.red - other[0], self.green - other[1], self.blue - other[2])
            self.red = updated_crystal_tuple[0]
            self.green = updated_crystal_tuple[1]
            self.blue = updated_crystal_tuple[2]
        return self
        
    def __contains__(self, other): 
        if isinstance (other,SaberCrystal):
            return (self.red >= other.red and self.green >= other.green and self.blue >= other.blue)
        else:
            return (self.red >= other[0] and self.green >= other[1] and self.blue >= other[2])