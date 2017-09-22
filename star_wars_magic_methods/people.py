class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        if self.dark_side:
            self.light_side = False
        else:
            self.light_side = True

    def __call__(self):
        message = "Help me {}, you're my only hope.".format(self.name)
        return message


    def __str__(self):
        return self.name

    def __pos__(self):
        self.light_side = True
        self.dark_side = False

    def __neg__(self):
        self.light_side = False
        self.dark_side = True

    def __eq__(self, other):
        if not isinstance(other, People):
            raise TypeError()
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        else:
            return '{self} shoots {other}.'.format(self=self, other=other)

    def __invert__(self):
        if self.light_side:
            self.light_side = False
            self.dark_side = True
        else:
            self.light_side = True
            self.dark_side = False


    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name,other.name)

    def __mul__(self, other):
        if type(other) != People:
            raise TypeError
        return "{} throws a thermal detonator at {}!".format(self.name, other.name)

    def __div__(self, other):
        if type(other) != People:
            raise TypeError

        return "{} swings a lightsaber at {}.".format(self.name,other.name)

    def __lshift__(self, other):
        if type(other) != People:
            raise TypeError
        return "{} uses the force to pull {} towards them.".format(self.name,other.name)



    def __rshift__(self, other):
        if type(other) != People:
            raise TypeError
        return "{} uses the force to push {} away from them.".format(self.name,other.name)


if __name__ == "__main__":
    leia = People('Leia Organa')
    mary = People('Leia Organa')
    print(str(leia))
    print(type(mary) == str)

