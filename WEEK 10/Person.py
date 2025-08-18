class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__age = age  #? Private member of the class

    def display(self):
        print(self.name, self.age)
