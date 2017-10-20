class SaberCrystal(object):
    def __init__(self, color=(255, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[-1]

    @property
    def color(self):
        return (self.red, self.green, self.blue)

    def __eq__(self, other):
        return self.color == other.color

    def __add__(self, other):
        try:
            return SaberCrystal((min(255, self.red + other.red),
                                min(255, self.green + other.green),
                                min(255, self.blue + other.blue)))
        except:
            return SaberCrystal((self.red + other[0],
                                self.green + other[1],
                                self.blue + other[2]))

    def __sub__(self, other):
        try:
            return SaberCrystal((self.red - other.red,
                                self.green - other.green,
                                self.blue - other.blue))
        except:
            return SaberCrystal((self.red - other[0],
                                self.green - other[1],
                                self.blue - other[2]))

    def __contains__(self, other):
        for index in range(len(self.color)):
            try:
                if (self.color[index] > 0 and
                   self.color[index] == other.color[index]):
                    return True
            except:
                if self.color[index] > 0 and self.color[index] == other[index]:
                    return True
        return False
