class SaberCrystal(object):
    def __init__(self, color=(255,0,0), red=255, green=0, blue=0):
        self.color = color 
        self.red = 255
        self.green = 0 
        self.blue = 0 
    
    def __eq__(self, other):
        return self.color == other.color
    
    def __add__(self, other):
        lst = []
        for el in range(0,3):
            if isinstance(other, tuple): 
                lst.append(self.color[el] + other[el])
            else: 
                lst.append(self.color[el] + other.color[el])
        lst = [255 if el > 255 else el for el in lst]
        return SaberCrystal(tuple(lst))
    
    def __iadd__(self, other):
        lst = []
        for el in range(0,3):
            if isinstance(other, tuple):
                value = self.color[el] + other[el]
                lst.append(value)
            else:
                value = self.color[el] + other.color[el]
                lst.append(value)
        lst = [255 if el > 255 else el for el in lst]
        return SaberCrystal(tuple(lst))
    
    def __sub__(self, other):
        lst = []
        for el in range(0,3):
            if isinstance(other, tuple):
                lst.append(self.color[el] - other[el])
            else:
                lst.append(self.color[el] - other.color[el])
        return SaberCrystal(tuple(lst))

    def __isub__(self, other):
        lst = []
        for el in range(0,3):
            if isinstance(other, tuple):
                value = self.color[el] - other[el]
                lst.append(value)
            else:
                value = self.color[el] - other.color[el]
                lst.append(value)
        return SaberCrystal(tuple(lst))
    
    def __contains__(self, item):
        if isinstance(item, tuple) and isinstance(self, tuple):
            for i in range(0, 3):
                item_idx = [idx for idx, v in enumerate(item) if v == item[i]]
                self_idx = [idx for idx, v in enumerate(self) if v == self[i]]
                if self[i] == item[i] and set(item_idx).issubset(self_idx):
                    return True
            return False
        elif isinstance(item, tuple) and isinstance(self, SaberCrystal):
            for i in range(0, 3):
                item_idx = [idx for idx, v in enumerate(item) if v == item[i]]
                self_idx = [idx for idx, v in enumerate(self.color) if v == self.color[i]]
                if self.color[i] == item[i] and set(item_idx).issubset(self_idx):
                    return True
            return False
        elif isinstance(item, SaberCrystal) and isinstance(self, SaberCrystal):
            for i in range(0, 3):
                item_idx = [idx for idx, v in enumerate(item.color) if v == item.color[i]]
                self_idx = [idx for idx, v in enumerate(self.color) if v == self.color[i]]
                if self.color[i] == item.color[i] and set(item_idx).issubset(self_idx):
                    return True
            return False
        else:
            for i in range(0, 3):
                item_idx = [idx for idx, v in enumerate(item.color) if v == item.color[i]]
                self_idx = [idx for idx, v in enumerate(self) if v == self.color[i]]
                if self[i] == item.color[i] and set(item_idx).issubset(self_idx):
                    return True
            return False