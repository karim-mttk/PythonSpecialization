class Car:
    #Class Attributes
    no_of_tries = 4

    #class constructor
    def __init__(self):
        #object attributes
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""
        self.moon_roof = ""
        self.engine_running = ""

        def start_the_engine():
            self.engine_running = True

        def stop_the_engine():
            self.engine_running = False

        """__del__ method is called is managed by Python's garbage 
        collector and may vary depending 
        on the Python implementation and system specifics."""
        #destructor
        def __del__(self):
            print(f"{self.make} {self.model} Destructor Invoked!")

def main():
    print("The main() method")
    car1 = Car()
    car2 = Car()

    #assign values
    car1.make = "Tesla"
    car1.model = "Model3"
    car1.color = "Red"
    car1.year = 2020
    car1.moon_roof = True

    #accessing attributes of car1:
    print("Printing car1 details:".center(50, "-"))
    print(f"Make: {car1.make}")
    print(f"Model: {car1.model}")
    print(f"Year: {car1.year}")
    print(f"Color: {car1.color}")
    print(f"Moon Roof: {car1.moon_roof}")

    #class attributes
    print("Class Attributes:".center(50, "-"))
    
    #overwriting the attributes of Car class
    Car.no_of_tries = 25
    print("car1:", car1.no_of_tries)

    #delete objects
    print("Objects Deleted".center(50, "-"))
    del car1
    del car2
    del car2

if __name__ == '__main__':
    main()



