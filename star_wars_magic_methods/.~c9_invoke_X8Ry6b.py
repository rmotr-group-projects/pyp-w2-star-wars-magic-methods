
class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
       return (self.red, self.green, self.blue)
       
    
        crystal_lis
        
        if isinstance (other,object): 
            final_crystal_tuple = (self.red + other.red, self.green + other.green, self.blue + other.blue)
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            return final_crystal
        else:
            final_crystal_tuple = (self.red + other[0], self.green + other[1], self.blue + other.[2])
            final_crystal = SaberCrystal(color=final_crystal_tuple)
            
            
            self.assertEquals(red_crystal + blue + green, white_crystal)
            
             green = (0,255,0)

        blue = (0,0,255)
        
# inplace addition should adjust the self object
#return self in inplace 