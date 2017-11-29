
from __future__ import division

class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
 
         
    @property
    def color(self):
        return (self.red, self.green, self.blue)
    
    def __eq__(self,other):
        match = [(a==b) for a,b  in zip(self.color, other.color)]
        return all(match)
        
    def check_max(self, color_list):
        return [255 if color > 255 else color for color in color_list ]
    
    def __add__(self, other):
        if isinstance(other, tuple) ==True:
            color_list = self.check_max(map( lambda x: x[0] + x[1], zip(self.color, other)))
            return SaberCrystal((tuple(color_list)))
        else:
            color_list = self.check_max(map( lambda x: x[0] + x[1], zip(self.color, other.color)))
            return SaberCrystal((tuple(color_list)))

    def __iadd__(self, other):
        if isinstance(other, tuple) ==True:
            color_list = self.check_max(map( lambda x: x[0] + x[1], zip(self.color, other)))
            return SaberCrystal((tuple(color_list)))
        else:
            color_list = self.check_max(map( lambda x: x[0] + x[1], zip(self.color, other.color)))
            return SaberCrystal((tuple(color_list)))

    def __sub__(self, other):
        if isinstance(other, tuple) ==True:
            color_list = self.check_max(map( lambda x: x[0] - x[1], zip(self.color, other)))
            return SaberCrystal((tuple(color_list)))
        else:
            color_list = self.check_max(map( lambda x: x[0] - x[1], zip(self.color, other.color)))
            return SaberCrystal((tuple(color_list)))

    def __str__(self):
        return str(self.color)
        
        
    def __isub__(self, other):
        if isinstance(other, tuple) ==True:
            color_list = self.check_max(map( lambda x: x[0] - x[1], zip(self.color, other)))
            return SaberCrystal((tuple(color_list)))
        else:
            color_list = self.check_max(map( lambda x: x[0] - x[1], zip(self.color, other.color)))
            return SaberCrystal((tuple(color_list)))

    def __contains__(self, other):
        if isinstance(other, tuple) ==True:
            color_match = [a==b if a != 0 and b!=0 else False for a,b in zip(self.color, other)]
            return any(color_match)
        else:
            color_match = [a==b if a != 0 and b!=0 else False for a,b in zip(self.color, other.color)]
            return any(color_match)
        

# red_crystal = SaberCrystal()
# green = (0,0,0)
# green_crystal = SaberCrystal(color=green)
# print(red_crystal in green_crystal)

# # blue = (0,0,255)
# # blue_crystal = SaberCrystal(color=blue)
# # white_crystal = SaberCrystal(color=(255,255,255))
# # self.assertTrue(red_crystal in white_crystal)
# # self.assertFalse(red_crystal in green_crystal)
# # self.assertTrue(green in white_crystal)
# # self.assertFalse(blue in red_crystal)



