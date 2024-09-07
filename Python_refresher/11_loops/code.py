# number = 7
#
# while True:
#     user_input = input("Would like to play?(y/n): ").lower()
#     if user_input == "n":
#         break
#
#     user_number = int(input("Guess out number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong!")

print("-----------------------------------------------")

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

print("-----------------------------------------------")
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total/amount)

print("-----------------------------------------------")
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total/amount)