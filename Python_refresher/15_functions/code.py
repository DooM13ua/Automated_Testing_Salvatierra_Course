def hello():
    print("Hello!")


hello()

print("-----------------------------------------")


def user_age_in_seconds():
    user_age = 30
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in second is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()
print("Goodbye!")

print("-----------------------------------------")


def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends)