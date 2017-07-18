class SaberCrystal(object):
    """
    SaberCrystal
    Init should take one optional parameter, color, which
    defaults to (255,0,0), which is a tuple representing red,
    green, blue. There should be 3 instance attributes, red,
    green, and blue. There needs to also be a *property* 'color'
    that returns a tuple with the values of red, green, and blue
    Finally you need to implement methods for the following
    operators: addition '+', in place addition '+=', subtraction
    '-', in place subtraction '-=', and contains 'x in y'
    """

    # red = (255, 0, 0)
    # green = (0, 255, 0)
    # blue = (0, 0, 255)

    def __init__(self, color=(255,0,0)):
        self._color = color
        self.red = self._color[0]
        self.green = self._color[1]
        self.blue = self._color[2]

    @property
    def color(self):
        return (self.red, self.green, self.blue)

    def alter_color(self, alteration):
        curr_color = self.color()
        print(curr_color)

    def __add__(self, other):
        self.red += other.red
        if self.red > 255:
            self.red = 255

        self.green += other.green
        if self.green > 255:
            self.green = 255

        self.blue += other.blue
        if self.blue > 255:
            self.blue = 255
        
        return self
    
    def __eq__(self, other):
        if self.red != other.red:
            return False
        if self.green != other.green:
            return False
        if self.blue != other.blue:
            return False
        return True


    def __sub__(self, args):
        pass

    def __iadd__(self, args):
        pass

    def __isub__(self, args):
        pass
    
    def __contains__(self, other):
        pass
