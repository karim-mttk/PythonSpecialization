class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        res = 2 + 3
        print(f"Testing the static method: {res}")


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book: {self.name}, type: {self.book_type}, weight: {self.weight}grams>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


"""
test = ClassTest()
# there are two different ways to use the instance methods:
test.instance_method()
ClassTest.instance_method(test)

# python will automatically pass the class ClassTest as cls as the argument
ClassTest.class_method()

# the static method does not take in instances or class, just a regular method
ClassTest.static_method()
"""

# book1 = Book("Harry Potter", "hardcover", 1200)
# print(book1.name)

book2 = Book.hardcover("Jason Bourne", 900)
book3 = Book.paperback("Goosebumps", 300)
print(book2)
print(book3)

