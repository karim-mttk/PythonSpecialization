def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(2, 3, 4))


# destructure arguments form a list
def add(x, y):
    return x + y


nums = [3, 5]
nums2 = {"x": 1, "y": 2}

print(add(*nums))
print(add(**nums2))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        print("Undefined operator!")


print("Testing the add operator:")
print(apply(1, 2, 3, 4, operator="+"))

print("Testing the multiplication operator:")
print(apply(2, 3, 4, operator="*"))


def named(**kwargs):
    print(f"Basic print: {kwargs}")


def print_nicely(**kwargs):
    named(**kwargs)
    print("Nice print: ")
    for arg, val in kwargs.items():
        print(f"{arg}: {val}")


print_nicely(name="Bob", age=24)


