class People(object):

    def __init__(self, name, dark_side=False):
        self.name = name
        self.ddark_side = dark_side

    @property
    def light_side(self):
        return not self.ddark_side

    @property
    def dark_side(self):
        return self.ddark_side

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

    def __lshift__(self, other):
        '''force pull'''

        if not isinstance(other, People):
            raise TypeError()

        return "%s uses the force to pull %s towards them." % (self.name, other)

    def __neg__(self):
        '''turn to dark side'''

        # ???: Why this does not work if we initialized dark_side like: self.dark_side = dark_side?
        # in this case, why not just self.dark_side = True?
        self.ddark_side = True

    def __pos__(self):
        '''turn to light side'''

        self.ddark_side = False

    def __invert__(self):
        '''change sides'''

        self.ddark_side = self.light_side

    def __xor__(self, other):
        '''force chokes'''
        # return "%s force chokes %s." % (self.name, other)
        return "{0} force chokes {1}.".format(self.name, other)

    def __eq__(self, other):
        '''shoots'''

        # ???: Trick question? Hard coded names in class
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        else:
            return '%s shoots %s.' % (self.name, other)

    # shoots



