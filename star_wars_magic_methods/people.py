class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side

    @property
    def light_side(self):
        return True if not self.dark_side else self.dark_side

    def __str__(self):
        return self.name

    def __truediv__(self, other):

        if type(other) is float:
            raise TypeError

        # ???: How does method know that other is using the name attribute from the class?
        return "%s swings a lightsaber at %s." % (self.name, other)
