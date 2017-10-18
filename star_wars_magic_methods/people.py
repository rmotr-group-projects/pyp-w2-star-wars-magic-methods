class People(object):
    shoots = False

    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
        self._light_side = not dark_side

    # def property light side
    @property
    def light_side(self):
        return self._light_side

    @light_side.setter
    def light_side(self,value):
        self._light_side = value
        self._dark_side = not value

    # def
    @property
    def dark_side(self):
        return self._dark_side

    @dark_side.setter
    def dark_side(self,value):
        self._dark_side = value
        self._light_side = not value

    # multiplication
    def __mul__(self,other):
        if isinstance(other,People):
            return '{} {} {}!'.format(self.name, "throws a thermal detonator at", other.name)
        raise TypeError

    # division
    def __truediv__(self,other):
        if isinstance(other,People):
            return '{} {} {}.'.format(self.name,'swings a lightsaber at',other.name)
        raise TypeError
    # negative number
    def __neg__(self):
        self.dark_side = True

    # positive number
    def __pos__(self):
        self.dark_side = False

    # invert
    def __invert__(self):
        previous = self.dark_side
        self.dark_side = not previous

    def __eq__(self,other):
        if not People.shoots:
            People.shoots = True
            return '{} {} {}.'.format(self.name,'shoots', other.name)
        return '{} {} {}. {}.'.format(other.name,'shoots', self.name,'BECAUSE HAN SHOOTS FIRST')

    def __call__(self):
        return '{} {}, {}.'.format('Help me',self.name,"you're my only hope")

    def __xor__(self,other):
        return '{} {} {}.'.format(self.name, 'force chokes', other.name)

    def __lshift__(self,other):
        return '{} {} {} {}.'.format(self.name, 'uses the force to pull', other.name, 'towards them')

    def __rshift__(self,other):
        if isinstance(other,People):
            return '{} {} {} {}.'.format(self.name, 'uses the force to push', other.name,'away from them')
        raise TypeError

    def __str__(self):
        return self.name
