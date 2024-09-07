class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bo", (90, 90, 90, 78, 90))
print(student.name)
print(student.grades)
print(student.average_grade())