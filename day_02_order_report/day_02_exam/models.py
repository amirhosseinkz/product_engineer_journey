

class Book:
    def __init__(self, id, title, author, category , price , stock):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.stock = stock

    def inventory_value(self):
        return self.price * self.stock
      