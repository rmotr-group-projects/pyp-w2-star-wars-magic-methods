
class SaberCrystal(object):

    def __init__(self, color=(255, 0, 0)):
        self.color = color
        self.red = self.color[0]
        self.green = self.color[1]
        self.blue = self.color[2]

    def __eq__(self, other):
        return (self.color == other)

    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        r, g, b = color_attr

        color_sum = (self.red + r,
                     self.green + g,
                     self.blue + b)

        return SaberCrystal(color=color_sum)

    def __iadd__(self, other):

        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        r, g, b = color_attr

        color_sum = (self.red + r,
                     self.green + g,
                     self.blue + b)

        return SaberCrystal(color=color_sum)

    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        r, g, b = color_attr

        color_sub = (self.red - r,
                     self.green - g,
                     self.blue - b)

        return SaberCrystal(color=color_sub)

    def __isub__(self, other):
        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        r, g, b = color_attr

        color_sub = (self.red - r,
                     self.green - g,
                     self.blue - b)

        return SaberCrystal(color=color_sub)



# red_crystal = SaberCrystal()

# green = (0, 255, 0)
# green_crystal = SaberCrystal(color=green)

# blue = (0, 0, 255)
# blue_crystal = SaberCrystal(color=blue)
# white_crystal = SaberCrystal(color=(255, 255, 255))

# red_crystal + blue_crystal
