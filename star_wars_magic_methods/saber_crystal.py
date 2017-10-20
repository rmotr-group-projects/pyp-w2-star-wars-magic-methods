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

    @property
    def red(self):
        return self.color[0]

    @property
    def green(self):
        return self.color[1]

    @property
    def blue(self):
        return self.color[2]
