import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0, f"Price {price} must be greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greater than or equal to zero!"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @staticmethod
    def is_integer(num):
        #count out the floats that are point zero 5.0, 10.0
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

print(Item.is_integer(7.0))