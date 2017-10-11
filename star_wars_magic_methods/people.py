# The init for the people class should take two parameters: name and dark_side (this one is an optional parameter that should have a default value of False) You need to implement methods for the following operators: callable(x()), /, *, <<, >>, negative(-x), positive(+x), invert(~x), ^, == You should also have two properties light_side and dark_side

class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return "Help me Obi-Wan Kenobi, you're my only hope."
    
    @property
    def light_side(self):
        return not self.dark_side