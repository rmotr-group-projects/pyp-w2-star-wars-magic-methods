class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.color = color
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    def __eq__(self, other):
        return self.color == other.color

    def __add__(self, other):
        sum = []
        for i in range(len(self.color)):
                if type(other) == tuple:
                    sum.append(self.color[i] + other[i])
                else:
                    sum.append(self.color[i] + other.color[i])
                
                if sum[-1] > 255:
                    sum[-1] = 255

        return SaberCrystal(color=tuple(sum))

    def __sub__(self, other):
        sum = []
        for i in range(len(self.color)):
                if type(other) == tuple:
                    sum.append(self.color[i] - other[i])
                else:
                    sum.append(self.color[i] - other.color[i])
                
                if sum[-1] < 0:
                    sum[-1] = 0

        return SaberCrystal(color=tuple(sum))

    def __contains__(self, other):
        sum = []
        for i in range(len(self.color)):
            if type(other) == tuple:
                if self.color[i] < other[i]:
                    return False
            else:
                if self.color[i] < other.color[i]:
                    return False
        return True
        
