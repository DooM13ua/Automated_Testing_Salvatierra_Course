def add(x, y=8):
    print(x + y)


add(x=5)


print("-----------------------------------------")

default_y = 3


def add(x, y=default_y):
    f_sum = x + y
    print(f_sum)


add(2)
default_y = 4 # can't change default parameter
add(2)