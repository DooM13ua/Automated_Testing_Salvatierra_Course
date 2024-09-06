from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad! never make a parameter equal to a mutable
        # value by default
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

# Just one student take exam, but both get grades!

print("--------------------------------")
# Way to fix it:
from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        # value by default
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

