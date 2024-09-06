def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(80, 5, operator=divide)
print(result)


print("------------------------------------------------")
from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 26},
    {"name": "Adam Wool", "age": 13},
    {"name": "Anne Run", "age": 56}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"])) # ver. 2 without get_friend_name fction
print(search(friends, "Rolf Smith", itemgetter("name"))) # ver 3 without function and lambda