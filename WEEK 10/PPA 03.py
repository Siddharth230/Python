import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    def is_origin(self):
        return self.x == 0 and self.y == 0

    def on_xaxis(self):
        return self.y == 0

    def on_yaxis(self):
        return self.x == 0

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return "first"
        elif self.x < 0 and self.y > 0:
            return "second"
        elif self.x < 0 and self.y < 0:
            return "third"
        else:
            return "fourth"

    def slope(self):
        return self.y / self.x
