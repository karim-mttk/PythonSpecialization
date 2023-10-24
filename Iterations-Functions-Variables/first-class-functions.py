def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


res = calculate(20, 4, operator=divide)
print(res)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 23},
    {"name": "Bob Dylan", "age": 52},
    {"name": "Alice Jackson", "age": 42},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Bob Dylan", get_friend_name))

