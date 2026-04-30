import json


class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def inventory_value(self):
        return self.price * self.stock


def load_products(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    products = []

    for item in data:
        product = Product(
            product_id=item["id"],
            name=item["name"],
            category=item["category"],
            price=item["price"],
            stock=item["stock"],
        )
        products.append(product)

    return products


def print_report(products):
    print("PRODUCT INVENTORY REPORT")
    print("=" * 30)

    total_value = 0
    categories = {}

    for product in products:
        value = product.inventory_value()
        total_value += value

        if product.category not in categories:
            categories[product.category] = 0

        categories[product.category] += 1

        print(f"{product.name} | {product.category} | Stock: {product.stock} | Value: ${value:.2f}")

    print("=" * 30)
    print(f"Total products: {len(products)}")
    print(f"Total inventory value: ${total_value:.2f}")

    print("\nProducts by category:")
    for category, count in categories.items():
        print(f"- {category}: {count}")


def main():
    products = load_products("products.json")
    print_report(products)


if __name__ == "__main__":
    main()