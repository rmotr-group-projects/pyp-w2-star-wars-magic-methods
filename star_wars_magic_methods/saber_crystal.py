class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        checked_color = self.color_check(color) # not required for tests but may as well pop in
        self.red, self.green, self.blue = checked_color
    
    @staticmethod
    def color_check(tuple_in):
        # this seems a tad opaque though it does the trick
        return tuple(map(lambda x: max(min(255, x), 0), tuple_in))
    
    @staticmethod
    def extract_color(input): # either put the check up here
        if isinstance(input, SaberCrystal):
            return input.color
        else: 
            return input

    @property
    def color(self):
        return (self.red, self.green, self.blue)
        
    @color.setter
    def color(self, color_in):
        checked_color = self.color_check(color_in)
        self.red, self.green, self.blue = checked_color
    
    def __eq__(self, other):
        for i in range(3):
            if self.color[i] != other.color[i]:
                return False
        return True

    def add_color(self, other, adj = 1):
        # QUESTION: eventually i've opted for putting the logic up here because it lets me not have to repeat in __add__ and __iadd__
        # does that sound like a good idea or no?
        other_color = self.extract_color(other)
        if adj == -1:
            other_color = tuple([-item for item in other_color])
        added_color = tuple([sum(col) for col in list(zip(self.color, other_color))])
        checked_color = self.color_check(added_color)
        return checked_color

    def __add__(self, other, adj = 1):
        checked_color = self.add_color(other, adj)
        return SaberCrystal(checked_color)
        
    def __iadd__(self, other, adj = 1):
        checked_color = self.add_color(other, adj)
        self.color = checked_color
        return self
        #QUESTION: I don't quite understand why we need to return self - though i appreciate it doesn't work without it
        
    def __sub__(self, other):
        return self.__add__(other, -1)
        
    def __isub__(self, other):
        return self.__iadd__(other, -1)
        
    def __contains__(self, item):
        item_color = self.extract_color(item)
        for i in range(3):
            if self.color[i] > 0 and self.color[i] == item_color[i]:
                return True
        return False
    