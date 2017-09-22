class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
        return (self.red,self.green,self.blue)

    def __eq__(self, other):
        if self.color == other.color:
            return True
        else:
            return False
#helper method to check the type of parameter and set color accordingly
    def check_parameter_type(self, other):
        if isinstance(other, SaberCrystal):
            _color = other.color
        elif isinstance(other, tuple):
            _color = other
        else:
            raise TypeError()
        return _color

    def _add(self,other):
        color = self.check_parameter_type(other)

        new_color = (self.red + color[0] if self.red + color[0] <= 255 else 255,
                     self.green + color[1] if self.green + color[1] <= 255 else 255,
                     self.blue + color[2] if self.blue + color[2] <= 255 else 255)
        return new_color

    def _subtract(self, other):
        color = self.check_parameter_type(other)

        new_color = (self.red - color[0] if self.red - color[0] >= 0 else 0,
                     self.green - color[1] if self.green - color[1] >= 0 else 0,
                     self.blue - color[2] if self.blue - color[2] >= 0 else 0)
        return new_color


    def __add__(self, other):
        return SaberCrystal(color=self._add(other))

    def __sub__(self, other):
        return SaberCrystal(color=self._subtract(other))

    def __contains__(self, item):
        n_color = self.check_parameter_type(item)

        for x in range(len(self.color)):
            if self.color[x] == n_color[x] and self.color[x] == 255:
                return True
        return False

    def __iadd__(self, other):
        new_color = self._add(other)
        self.red, self.green, self.blue = new_color
        return self

    def __isub__(self, other):
        new_color = self._subtract(other)
        self.red, self.green, self.blue = new_color
        return self









