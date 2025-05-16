class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"\nStudent Name: {self.name} and Student Marks: {self.marks}")

s1 = Student("Saud", 96)
s1.display()