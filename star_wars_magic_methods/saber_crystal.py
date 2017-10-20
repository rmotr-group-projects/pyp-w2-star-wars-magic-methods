class SaberCrystal(object):
    def __init__(self, color=(255, 0, 0)):
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, SaberCrystal):
            return False
        return self.color == other.color

    def __add__(self, other):
        other_color = other
        if isinstance(other, tuple):
            other_crystal = SaberCrystal(color=other)
        else:
            if not isinstance(other, SaberCrystal):
                raise TypeError("Can't perform operation with SaberCrystal "
                                "object and {}".format(type(other).__name__))
            other_crystal = other
        colors = {}
        colors['red'] = self.red + other_crystal.red
        colors['green'] = self.green + other_crystal.green
        colors['blue'] = self.blue + other_crystal.blue

        for color, value in colors.items():
            if value > 255:
                colors[color] = 255

        result_crystal = SaberCrystal(color=(colors["red"],
                                             colors["green"],
                                             colors["blue"]))
        return result_crystal

    def __iadd__(self, other):
        print self, other
        return self + (self + other)

    def __sub__(self, other):
        other_color = other
        if isinstance(other, tuple):
            other_crystal = SaberCrystal(color=other)
        else:
            if not isinstance(other, SaberCrystal):
                raise TypeError("Can't perform operation with SaberCrystal "
                                "object and {}".format(type(other).__name__))
            other_crystal = other
        colors = {}
        colors['red'] = self.red - other_crystal.red
        colors['green'] = self.green - other_crystal.green
        colors['blue'] = self.blue - other_crystal.blue
        for color, value in colors.items():
            if value < 0:
                colors[color] = 0

        result_crystal = SaberCrystal(color=(colors["red"],
                                             colors["green"],
                                             colors["blue"]))
        return result_crystal


    @property
    def red(self):
        return self.color[0]

    @property
    def green(self):
        return self.color[1]

    @property
    def blue(self):
        return self.color[2]


green = (0,255,0)
green_crystal = SaberCrystal(color=green)
blue = (0,0,255)
blue_crystal = SaberCrystal(color=blue)
white_crystal = SaberCrystal(color=(255,255,255))
print((white_crystal - blue_crystal - green_crystal).color)
print((white_crystal - blue - green).color)

'''
    def test_subtraction(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        self.assertEquals(white_crystal - blue_crystal - green_crystal, red_crystal)
        self.assertEquals(white_crystal - blue - green, red_crystal)
'''