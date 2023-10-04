class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"<Name: {self.name}, age: {self.age}>"


person1 = Person("Heisenberg", 50)
print(person1.__repr__())


