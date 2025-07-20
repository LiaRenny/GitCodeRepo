# The nth highest number of orders made by a single customer.

def nth_highest_order_count(orders, n):
    # Count orders per customer
    order_counts = {}
    for customer in orders:
        order_counts[customer] = order_counts.get(customer, 0) + 1

    # Get unique counts, sort descending
    unique_counts = sorted(set(order_counts.values()), reverse=True)

    if n <= 0 or n > len(unique_counts):
        return None  # n is out of range

    return unique_counts[n - 1]

if __name__ == "__main__":
    # Example: list of customer names (one per order)
    orders = input("Enter customer names for each order, separated by spaces: ").split()
    n = int(input("Enter n (e.g., 2 for 2nd highest): "))
    result = nth_highest_order_count(orders, n)
    if result is not None:
        print(f"The {n}th highest number of orders by a single customer is: {result}")
    else:
        print("Invalid n value.")