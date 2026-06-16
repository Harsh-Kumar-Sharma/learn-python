# Day 14 - Higher Order Functions in Python
# A higher order function is a function that:
# 1. Takes another function as an argument, or
# 2. Returns another function as a result.
#
# This sounds advanced, but you already see it in real Python code with:
# map(), filter(), reduce(), sorted(), and callbacks.


# 1. Function as a value
# In Python, a function can be stored in a variable.
def greet(name):
    return "Hello " + name


message_function = greet

print(message_function("Harsh"))


# 2. Function as an argument
# Here calculate() receives another function as input.
def square(number):
    return number * number


def calculate(function, value):
    return function(value)


print("Square using higher order function:", calculate(square, 5))


# 3. Real-world example: apply offer on bill
def ten_percent_discount(amount):
    return amount - (amount * 10 / 100)


def festival_discount(amount):
    return amount - (amount * 25 / 100)


def final_bill(amount, discount_function):
    return discount_function(amount)


print("Normal discount bill:", final_bill(2000, ten_percent_discount))
print("Festival discount bill:", final_bill(2000, festival_discount))


# 4. Function returning another function
def multiplier(number):
    def multiply(value):
        return value * number

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("Double of 10:", double(10))
print("Triple of 10:", triple(10))


# 5. Real-world example: tax calculator generator
def tax_calculator(tax_percent):
    def calculate_tax(amount):
        return amount + (amount * tax_percent / 100)

    return calculate_tax


gst_18 = tax_calculator(18)
gst_5 = tax_calculator(5)

print("Bill with 18% GST:", gst_18(1000))
print("Bill with 5% GST:", gst_5(1000))


# 6. Lambda function
# Lambda is a small one-line anonymous function.
# Syntax: lambda arguments: expression
add = lambda num1, num2: num1 + num2

print("Lambda add:", add(10, 20))


# 7. Lambda with higher order function
print("Lambda square:", calculate(lambda number: number * number, 6))


# 8. map()
# map() applies a function to every item in an iterable.
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda number: number * number, numbers))
print("Squared numbers using map:", squared_numbers)


# 9. map() real-world example: convert prices to GST prices
prices = [100, 250, 500, 1000]

prices_with_gst = list(map(lambda price: price + (price * 18 / 100), prices))
print("Prices with GST using map:", prices_with_gst)


# 10. map() with normal function
def convert_to_uppercase(name):
    return name.upper()


names = ["harsh", "amit", "priya"]
upper_names = list(map(convert_to_uppercase, names))

print("Uppercase names using map:", upper_names)


# 11. filter()
# filter() keeps only the values where the function returns True.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)


# 12. filter() real-world example: passed students
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Priya", "marks": 35},
    {"name": "Rahul", "marks": 60},
    {"name": "Neha", "marks": 25},
]

passed_students = list(filter(lambda student: student["marks"] >= 40, students))
print("Passed students using filter:", passed_students)


# 13. reduce()
# reduce() combines all values into one final value.
# It is available inside functools module.
from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda current_total, number: current_total + number, numbers)
print("Total using reduce:", total)


# 14. reduce() real-world example: cart total
cart_items = [
    {"name": "Mouse", "price": 799},
    {"name": "Keyboard", "price": 1299},
    {"name": "USB Cable", "price": 199},
]

cart_total = reduce(
    lambda total_amount, item: total_amount + item["price"],
    cart_items,
    0,
)

print("Cart total using reduce:", cart_total)


# 15. sorted() with key function
# sorted() can use a function to decide sorting logic.
employees = [
    {"name": "Amit", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Rahul", "salary": 35000},
]

employees_by_salary = sorted(employees, key=lambda employee: employee["salary"])
print("Employees sorted by salary:", employees_by_salary)


# 16. Callback function
# A callback is a function passed to another function to run later.
def send_email(username):
    print("Email sent to", username)


def send_sms(username):
    print("SMS sent to", username)


def notify_user(username, notification_function):
    print("Notification started")
    notification_function(username)
    print("Notification completed")


notify_user("Harsh", send_email)
notify_user("Priya", send_sms)


# 17. Nested functions
# A function can be created inside another function.
def outer_function():
    print("Outer function started")

    def inner_function():
        print("Inner function called")

    inner_function()
    print("Outer function completed")


outer_function()


# 18. Closure
# A closure remembers values from the outer function even after the outer
# function has finished running.
def welcome_message(course_name):
    def message(student_name):
        return "Welcome " + student_name + " to " + course_name

    return message


python_welcome = welcome_message("Python")
print(python_welcome("Harsh"))
print(python_welcome("Amit"))


# 19. Real-world example: reusable permission checker
def permission_checker(required_role):
    def check_user(user):
        return user["role"] == required_role

    return check_user


is_admin = permission_checker("admin")

user1 = {"name": "Harsh", "role": "admin"}
user2 = {"name": "Amit", "role": "user"}

print("Is user1 admin?", is_admin(user1))
print("Is user2 admin?", is_admin(user2))


# 20. map, filter, reduce together
product_prices = [500, 1200, 300, 2500, 800]

# Step 1: keep only products above 1000
expensive_prices = list(filter(lambda price: price > 1000, product_prices))

# Step 2: apply 10% discount on those products
discounted_prices = list(map(lambda price: price - (price * 10 / 100), expensive_prices))

# Step 3: calculate final total
final_total = reduce(lambda total_amount, price: total_amount + price, discounted_prices, 0)

print("Expensive prices:", expensive_prices)
print("Discounted expensive prices:", discounted_prices)
print("Final total:", final_total)


# 21. What should you know about higher order functions?
# - Functions can be stored in variables
# - Functions can be passed as arguments
# - Functions can return other functions
# - Lambda creates small one-line functions
# - map() transforms every item
# - filter() keeps only matching items
# - reduce() combines values into one result
# - sorted() can use a function with key
# - Callback functions are passed and called later
# - Closures remember values from their outer function
# - Use these only when they make code cleaner and easier to read
