# Day 1 to Day 14 - One Mini Project Assignment
# Project: Smart Store Sales Analyzer
#
# This one assignment uses the main topics from Day 1 to Day 14:
# - Day 1: print()
# - Day 2: variables
# - Day 3: operators
# - Day 4: strings
# - Day 5: lists
# - Day 6: tuples
# - Day 7: sets
# - Day 8: dictionaries
# - Day 9: conditionals
# - Day 10: loops
# - Day 11: functions
# - Day 12: modules
# - Day 13: list comprehension
# - Day 14: higher order functions, lambda, map, filter, reduce
#
# Real-world problem:
# A small store wants to analyze daily sales.
# The store needs to:
# 1. Clean customer names.
# 2. Calculate each order total.
# 3. Apply discounts.
# 4. Add GST.
# 5. Find unique product categories.
# 6. Find high-value orders.
# 7. Calculate total store revenue.
# 8. Print a simple daily report.


from functools import reduce
import statistics


print("Smart Store Sales Analyzer")
print("=" * 40)


# Store details
store_name = "Fresh Mart"
store_location = ("Delhi", "India")
gst_percent = 18
discount_limit = 2000
discount_percent = 10


# Daily sales data
orders = [
    {
        "order_id": "ORD1001",
        "customer_name": "  hArSh shArMa ",
        "items": [
            {"name": "Rice", "category": "Grocery", "price": 1200, "quantity": 1},
            {"name": "Tea", "category": "Beverage", "price": 250, "quantity": 2},
        ],
    },
    {
        "order_id": "ORD1002",
        "customer_name": " PRIYA singh",
        "items": [
            {"name": "Keyboard", "category": "Electronics", "price": 1299, "quantity": 1},
            {"name": "Mouse", "category": "Electronics", "price": 799, "quantity": 1},
        ],
    },
    {
        "order_id": "ORD1003",
        "customer_name": "amit KUMAR  ",
        "items": [
            {"name": "Soap", "category": "Personal Care", "price": 80, "quantity": 3},
            {"name": "Shampoo", "category": "Personal Care", "price": 180, "quantity": 2},
        ],
    },
]


# Function to clean customer names
def clean_name(name):
    return name.strip().title()


# Function to calculate item total
def calculate_item_total(item):
    return item["price"] * item["quantity"]


# Function to calculate subtotal for one order
def calculate_subtotal(items):
    item_totals = [calculate_item_total(item) for item in items]
    return sum(item_totals)


# Function to apply discount
def apply_discount(amount):
    if amount >= discount_limit:
        return amount * discount_percent / 100
    return 0


# Function to add GST
def add_gst(amount):
    return amount + (amount * gst_percent / 100)


# Higher order function example
# This function receives another function as an argument.
def process_amount(amount, amount_function):
    return amount_function(amount)


# Analyze all orders
processed_orders = []
all_categories = set()

for order in orders:
    customer_name = clean_name(order["customer_name"])
    subtotal = calculate_subtotal(order["items"])
    discount = apply_discount(subtotal)
    amount_after_discount = subtotal - discount
    final_amount = process_amount(amount_after_discount, add_gst)

    for item in order["items"]:
        all_categories.add(item["category"])

    processed_order = {
        "order_id": order["order_id"],
        "customer_name": customer_name,
        "subtotal": subtotal,
        "discount": discount,
        "final_amount": final_amount,
    }

    processed_orders.append(processed_order)


# List comprehension example
customer_names = [order["customer_name"] for order in processed_orders]


# filter() with lambda example
high_value_orders = list(
    filter(lambda order: order["final_amount"] >= 2000, processed_orders)
)


# map() with lambda example
rounded_final_amounts = list(
    map(lambda order: round(order["final_amount"], 2), processed_orders)
)


# reduce() with lambda example
total_revenue = reduce(
    lambda total, order: total + order["final_amount"],
    processed_orders,
    0,
)


average_order_value = statistics.mean(rounded_final_amounts)


# Print final report
print("Store:", store_name)
print("Location:", store_location[0] + ", " + store_location[1])
print("GST Percent:", gst_percent)
print("Discount Rule:", str(discount_percent) + "% discount on orders above", discount_limit)
print("-" * 40)

for order in processed_orders:
    print("Order ID:", order["order_id"])
    print("Customer:", order["customer_name"])
    print("Subtotal:", order["subtotal"])
    print("Discount:", order["discount"])
    print("Final Amount:", round(order["final_amount"], 2))
    print("-" * 40)

print("All customers:", customer_names)
print("Unique categories:", all_categories)
print("High value orders:", high_value_orders)
print("Rounded final amounts:", rounded_final_amounts)
print("Total revenue:", round(total_revenue, 2))
print("Average order value:", average_order_value)


# Your practice tasks:
# 1. Add two more orders.
# 2. Add one new category.
# 3. Change discount rule to 15% for orders above 3000.
# 4. Print only customer names whose final amount is above 1500.
# 5. Add a function to count total products sold.
# 6. Add a function that returns the highest order amount.
# 7. Try changing GST percent and check the final report.
