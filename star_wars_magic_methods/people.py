class People(object):

    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side

    @property
    def light_side(self):
        return True if not self.dark_side else self.dark_side

    def __str__(self):
        '''string'''
        return self.name

    def __call__(self):
        '''call for help'''
        return "Help me %s, you're my only hope." % self.name

    def __truediv__(self, other):
        '''lightsaber'''
        if not isinstance(other, People):
            raise TypeError()

        # ???: How does method know that other is using the name attribute from the class?
        return "%s swings a lightsaber at %s." % (self.name, other)

    def __mul__(self, other):
        '''thermal detonator'''

        # ???: why does this raise exception not work
        # if type(other) is not str:
        #     raise TypeError()
        if not isinstance(other, People):
            raise TypeError()

        return "%s throws a thermal detonator at %s!" % (self.name, other)

    def __rshift__(self, other):
        '''force push'''

        if not isinstance(other, People):
            raise TypeError()

        return "%s uses the force to push %s away from them." % (self.name, other)
