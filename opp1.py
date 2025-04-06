class Student:
    print("Hellow world")
    def __init__(self, height = 164):
        self.height = height

Artem = Student(height=170)
Mark = Student()

print("My height = ", Artem.height)
print("My height = ", Mark.height)