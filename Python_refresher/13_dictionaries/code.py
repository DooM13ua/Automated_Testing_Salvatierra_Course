friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages)

print("-----------------------------------------------")

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1]["name"])

print("-----------------------------------------------")

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

print("-----------------------------------------------")

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
if "Bob" in student_attendance:
    print(f"Bob:{student_attendance['Bob']}")

else:
    print("Bob is not student in this class.")

print("-----------------------------------------------")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

attendance_values = student_attendance.values()
print(sum(attendance_values)/len(attendance_values))