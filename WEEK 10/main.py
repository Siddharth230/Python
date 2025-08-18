class Student:
    def __init__(self, roll_no, name, total):
        self.roll_no = roll_no
        self.name = name
        self.total = total

    def display(self):
        print(self.roll_no, self.name, self.total)

    def result(self):
        if self.total > 120:
            print("Pass")
        else:
            print("Fail")


s0 = Student(0, "Siddharth", 100)
s0.display()
s0.result()

s1 = Student(1, "Om", 150)
s1.display()
s1.result()
