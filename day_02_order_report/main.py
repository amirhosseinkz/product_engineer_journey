from pathlib import Path
from readers import read_orders, read_customers
from reports import print_order_report


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"



def main():
    orders = read_orders(DATA_DIR / "orders.json")
    customers = read_customers(DATA_DIR / "customers.csv")

    print_order_report(orders , customers)




if __name__ == "__main__":
    main()