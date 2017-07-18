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

    # ===================================
    #  TO DO LIST
    # ===================================
    # x() "callable"
    # /
    # *
    # <<
    # >>
    # - unary op
    # + unary op
    # ~
    # ^
    # ===================================

    def __eq__(self, other):
        # overload == operation
        return self.name == other.name
    
