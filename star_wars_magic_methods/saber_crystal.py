
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

        sum_color_list = [self.red + r,
                          self.green + g,
                          self.blue + b]

        color_sum = [s if s <= 255 else 255 for s in sum_color_list]

        return SaberCrystal(color=tuple(color_sum))

    def __iadd__(self, other):

        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        r, g, b = color_attr

        sum_color_list = [self.red + r,
                          self.green + g,
                          self.blue + b]

        color_sum = [s if s <= 255 else 255 for s in sum_color_list]

        return SaberCrystal(color=tuple(color_sum))

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

    def __contains__(self, other):
        if isinstance(other, SaberCrystal):
            color_attr = other.color
        elif isinstance(other, tuple):
            color_attr = other

        color_match = [c1 == c2 for c1, c2
                       in zip(self.color, color_attr)
                       if any([c1, c2])]

        return any(color_match)
