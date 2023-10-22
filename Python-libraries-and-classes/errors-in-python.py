def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be zero!!")

    return dividend / divisor


students = [{"name": "Drake", "grades": [55, 75, 34]},
            {"name": "Alice", "grades": [78, 90, 86]},
            {"name": "Bob", "grades": [56]}]


print("Welcome to the average grade problem")
try:
    for s in students:
        name = s["name"]
        grades = s["grades"]
        avg = divide(sum(grades), len(grades))
        print(f"{name}'s average grade is: {avg} ")
except ZeroDivisionError:
    print(f"ERROR: {name} has EMPTY LIST")
else:
    print("All students' grades are calculated")
finally:
    print("End of program")


