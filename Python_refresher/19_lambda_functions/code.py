# function that doesn't have a name, and only return values
# never used to perform actions
# use to be short functions

# common function
def add(x,y):
    return x + y


print(add(5, 7))
print("-----------------------------------------")

# lambda function
# can be used without a name
result = (lambda x, y: x + y)(5, 7)
print(result)

print("-----------------------------------------")

# common function


def double(x):
    return x*2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)

print(doubled)
# using lambda
print("-----------------------------------------")


def double_2(y):
    return y*2


sequence = [1, 3, 5, 9]
doubled_2 = [(lambda y: y * 2)(y) for y in sequence]
doubled_2 = list(map(lambda y: y * 2, sequence))

print(doubled_2)



