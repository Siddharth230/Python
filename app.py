class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


sid = Person("Siddharth Lokhande")
sid.talk()

om = Person("Om")
om.talk()
