class My_Calc:

    def __init__(self, num1, num2):
        #object attributes
        self.num1 = num1
        self.num2 = num2

    #declaring class attributes
    def total(self):
        return self.num1 + self.num2

    def diff(self):
        return self.num1 - self.num2


def main():
    print("This is main()!")
    calc1 = My_Calc(10, 20)
    total1 = calc1.total()
    diff1 = calc1.diff()

    print(f"Total1: {total1}")
    print(f"Diff1: {diff1}")

if __name__ == '__main__':
    main()