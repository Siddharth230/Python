class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a  # first attribute
        self.b = b  # second attribute

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

    def subtract(self):
        return self.a - self.b

    def quotient(self):
        return self.a // self.b  # returns float division

    def remainder(self):
        return self.a % self.b
