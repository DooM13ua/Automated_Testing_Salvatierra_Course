def add(x, y):
    result = x + y
    print(result)
    # pass  # python do nothing


add(5, 3)

print("-----------------------------------------")


def say_hello(name, surname):
    print(f"Hello, {name} {surname}.")


say_hello(name="Bob", surname="Smith")

print("-----------------------------------------")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=123987)