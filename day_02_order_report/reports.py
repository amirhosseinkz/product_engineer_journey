


def print_order_report(orders , customers):
    print("ORDER REPORT")
    print("=" * 60)

    total_revenue = 0
    total_paid_orders_average = 0
    statuses = {}

    for order in orders:
        total = order.total_amount()
        customer_info = customers.get(order.customer, {})
        city = customer_info.get("city", "Unknown")
        email = customer_info.get("email", "Unknown")

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
            "City:",
            city,
            "|",
            "Email:",
            email,
            "|",
            f"Total: ${total:.2f}",
        )

        if order.status not in statuses:
            statuses[order.status] = 0

        statuses[order.status] += 1

        if order.status == "paid":
            total_revenue += total

        if total_revenue > 0:
           total_paid_orders_average = total_revenue / statuses.get("paid" , 0)

    print(60)
    print("Total orders:", len(orders))
    print("Paid orders:", statuses.get("paid", 0))
    print("Pending orders:", statuses.get("pending", 0))
    print(f"Total revenue from paid orders: ${total_revenue:.2f}")
    print(f"Average paid order amount: ${total_paid_orders_average:.2f}")