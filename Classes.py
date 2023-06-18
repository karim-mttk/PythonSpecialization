'''
#problem 1:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)
print(p is q)

#problem 2:
class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


t = NumberSet(6, 10)

#problem 3:
class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
    def limbs(self):
        return self.arms + self.legs

spider = Animal(4, 4)
spidlimbs = spider.limbs()

#problem 4:
class Cereal:
    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand,
                                                                                                self.fiber)
c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)

#problem 5:
class AppleBasket():
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return 'A basket of {} {} apples.'.format(self.apple_quantity, self.apple_color)

a1 = AppleBasket('green', 30)
AppleBasket.increase(a1)
print(a1)

#problem 6:
class BankAccount():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return 'Your account, {}, has {} dollars.'.format(self.name, self.amt)

t1 = BankAccount('Bob', 100)
print(t1)

#problem 7:
class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    attack_boost = 10



#problem 8:
def opponent(self):
    if self.p_type == 'Grass':
        return ('Fire', 'Water')
    if self.p_type == 'Ghost':
        return ('Dark', 'Psychic')
    if self.p_type == 'Fire':
        return ('Water', 'Grass')
    if self.p_type == 'Flying':
        return ('Electric', 'Fighting')

'''

#problem 9:
x = 'jello'
print(dir(x))

