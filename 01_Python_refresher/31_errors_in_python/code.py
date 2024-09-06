def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0!")
    return dividend/divisor


grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank You!")


print("----------------------------------------------")


def divide_2(dividend2, divisor2):
    if divisor2 == 0:
        raise ZeroDivisionError("Divisor2 cannot be 0!")

    return dividend2 / divisor2


students = [
    {"name": "Bo", "grades": [75, 90]},
    {"name": "Rolf", "grades": [5]},
    {"name": "Jen", "grades": [90, 100]}
]

name_2 = None

try:
    for student in students:
        name_2 = student["name"]
        grades_2 = student["grades"]
        average_2 = divide_2(sum(grades_2), len(grades_2))
        print(f"{name_2} averaged {average_2}.")

except ZeroDivisionError:
    print(f"ERROR: {name_2} has no grades!")

else:
    print("-- All students' averages calculated --")
finally:
    print("-- End of student average calculating --")