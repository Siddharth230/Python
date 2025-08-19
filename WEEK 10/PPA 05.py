class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_info(self):
        print(f"({self.x},{self.y})")

    def scale(self, s):
        self.x *= s
        self.y *= s

    def reflect_about_X(self):
        self.y = -(self.y)

    def reflect_about_Y(self):
        self.x = -(self.x)

    def add(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
