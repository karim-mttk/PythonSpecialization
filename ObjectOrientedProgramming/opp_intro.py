class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Bob", (90, 80, 79, 88))
student2 = Student("Rea", (80, 74, 90, 89))

print(student2.name)
print(student2.average_grade())
