import json
import csv
from pathlib import Path
from models import Order, OrderItem

def read_orders(file_path):
    path = Path(file_path)
    with path.open("r") as file:
        data = json.load(file)

    orders = []

    for order in data:
        order_items = []

        for item in order["items"]:
            order_item = OrderItem(
                name=item["name"],
                quantity=item["quantity"],
                price=item["price"],
            )
            order_items.append(order_item)

        order_obj = Order(
            id=order["id"],
            customer=order["customer"],
            status=order["status"],
            items=order_items,
        )
        orders.append(order_obj)

    return orders


def read_customers(file_path):
    path = Path(file_path)
    customers = {}
    with path.open("r") as file:
        data = csv.DictReader(file)

        for row in data:
    
         customers[row["customer"]] = {
           "email": row["email"],
           "city": row["city"]
       }

    return customers
