class SaberCrystal(object):
    def __init__(self, color=(255, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
        return self.red, self.green, self.blue

    def __eq__(self, other):
        if not isinstance(other, SaberCrystal):
            raise TypeError()

        return self.color == other.color

    def __add__(self, other):
        return SaberCrystal(
            [min(255, x + y) for x, y in zip(self.color, other.color if isinstance(other, SaberCrystal) else other)])

    def __sub__(self, other):
        return SaberCrystal(
            [max(0, x - y) for x, y in zip(self.color, other.color if isinstance(other, SaberCrystal) else other)])

    # def __contains__(self, item):
    #     if isinstance(item, SaberCrystal):
    #         item = item.color
    #     for index, val in enumerate(item):
    #         if val != 0 and self.color[index] != val:
    #             return False
    #     return True

    def __contains__(self, item):
        """
        Returns true if all non-0 fields in the other item
        match with this crystal's corresponding fields

        Would probably actually go with the above implementation for better readability,
        but I wanted to see if I could make it a one-liner :)
        """

        return all(val == 0 or self.color[index] == val for index, val in
                   enumerate(item.color if isinstance(item, SaberCrystal) else item))
