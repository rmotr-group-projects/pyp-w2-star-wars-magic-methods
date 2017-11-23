class SaberCrystal(object):
    def __init__(self, color=(255, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
        return self.red, self.green, self.blue

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        return SaberCrystal(
            color=[min(255, x + y) for x, y in zip(self.color, other.color if type(other) is SaberCrystal else other)])

    def __sub__(self, other):
        return SaberCrystal(
            color=[max(0, x - y) for x, y in zip(self.color, other.color if type(other) is SaberCrystal else other)])

    def __contains__(self, item):
        if type(item) is SaberCrystal:
            item = item.color
        for index, val in enumerate(item):
            if val != 0 and self.color[index] != val:
                return False
        return True
