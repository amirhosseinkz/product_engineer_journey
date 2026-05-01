



class Order:
    def __init__(self, id, customer, status, items):
        self.id = id
        self.customer = customer
        self.status = status
        self.items = items

    def total_amount(self):
        return sum(item.total_price() for item in self.items)


class OrderItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price