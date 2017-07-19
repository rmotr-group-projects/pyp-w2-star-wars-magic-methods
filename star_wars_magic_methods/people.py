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
        try:
            if self.name == "Greedo" and other.name == "Han Solo":
                return "Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST."
            else:
                return "{} shoots {}.".format(self.name, other.name)
        except:
            raise TypeError

    def __call__(self):
        # x() "callable"
        if self.name == 'Obi-Wan Kenobi':
            return "Help me Obi-Wan Kenobi, you're my only hope."
        else:
            return "You're not Obi-Wan. Where's Obi-Wan? We need him."

    def __invert__(self):
        # overload ~ operator
        if self.dark_side:
            self.light_side = True
            self.dark_side = False
        else:
            self.light_side = False
            self.dark_side = True
        
    def __xor__(self, other):
        # overload ^ operator
        try:
            return "{} force chokes {}.".format(self.name, other.name)
        except:
            raise TypeError


    def __lshift__(self, other):
        # overload <<
        try:
            return "{} uses the force to pull {} towards them.".format(self.name, other.name)
        except:
            raise TypeError

    def __rshift__(self, other):
        # overload >>
        try:
            return "{} uses the force to push {} away from them.".format(self.name, other.name)
        except:
            raise TypeError

    def __div__(self, other):
        # overload /
        try:
            return "{} swings a lightsaber at {}.".format(self.name, other.name)
        except:
            raise TypeError

    def __mul__(self, other):
        try:
            return "{} throws a thermal detonator at {}!".format(self.name, other.name)
        except:
            raise TypeError

    def __neg__(self):
        self.dark_side = True
        self.light_side = False

    def __pos__(self):
        self.light_side = True
        self.dark_side = False
