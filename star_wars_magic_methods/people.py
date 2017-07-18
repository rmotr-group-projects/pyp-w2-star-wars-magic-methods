class People(object):
    """
    People
    The init for the people class should take two parameters:
    name and dark_side (this one is an optional parameter that
    should have a default value of False) You need to implement
    methods for the following operators: callable(x()), /, *, <<,
    >>, negative(-x), positive(+x), invert(~x), ^, == You should
    also have two properties light_side and dark_side
    """

    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side

        if self.dark_side:
            self.light_side = False
        else:
            self.light_side = True
    
    def __str__(self):
        return self.name

    def __eq__(self, other):
        # overload == operation
        return self.name == other.name

    # def callable
    # x() "callable"
    #    if self.name == 'Obi-Wan Kenobi':
    #       return "Help me Obi-Wan Kenobi, you're my only hope."

    # def __div__(self, other):
    #     ahsoka / ventress, 
    #     return "{} swings a lightsaber at {}.".format(self.name, other.name)
    # with self.assertRaises(TypeError):
    #     ahsoka / 2.5

    # def __mult__(self, other):
    #     return "{} throws a thermal detonator at {}!".format(self.name, other.name)
    
    # def __shift_left__(self, other):
    # TODO find name for <<
    
    # def __shift_right__(self, other):
    # TODO find name for >>

    # def __neg__(self):
    #     pass

    # def __pos__(self):
    #     pass

    # def __tilde__(self):
    #     pass
    
    # def __or__(self):
    #     pass
