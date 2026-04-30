import json


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


def read_orders(file_path):
    with open(file_path, "r") as file:
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


def print_orders(orders):
    print("ORDER REPORT")
    print("=" * 30)

    total_revenue = 0
    statuses = {}

    for order in orders:
        total = order.total_amount()

        print(
            "Order #",
            order.id,
            "|",
            "Customer:",
            order.customer,
            "|",
            "Status:",
            order.status,
            "|",
            f"Total: ${total:.2f}",
        )

        if order.status not in statuses:
            statuses[order.status] = 0

        statuses[order.status] += 1

        if order.status == "paid":
            total_revenue += total

    print("=" * 30)
    print("Total orders:", len(orders))
    print("Paid orders:", statuses.get("paid", 0))
    print("Pending orders:", statuses.get("pending", 0))
    print(f"Total revenue from paid orders: ${total_revenue:.2f}")


def main():
    orders = read_orders("orders.json")
    print_orders(orders)


if __name__ == "__main__":
    main()