def named(**kwargs):  # ** collects key arguments
    print(kwargs)


named(name='Bo', age=25)

print("-----------------------------------------")


def names(name, age):
    print(name, age)


details = {'name': 'Bo', 'age': 26}
names(**details)

print("-----------------------------------------")


def namew(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    namew(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name='Bo', age=30)

print("-----------------------------------------")


def both(*args, **kwargs):  # used to accept unlimited number of arguments
    print(args)
    print(kwargs)


both(1, 2, 3, name='Bo', age=30)


