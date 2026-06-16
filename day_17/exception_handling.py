# Day 17 - Exception Handling in Python
# Exception handling is used to handle errors without stopping the program.
# Python uses try, except, else, and finally.
#
# Basic syntax:
# try:
#     code that may give error
# except:
#     code that runs if error happens


# 1. Basic try-except
try:
    result = 10 / 0
    print(result)
except:
    print("Something went wrong")


# 2. Handling a specific error
# It is better to mention the exact error type.
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")


# 3. ValueError example
try:
    age = int("abc")
    print("Age:", age)
except ValueError:
    print("Please enter a valid number")


# 4. TypeError example
try:
    total = "Age: " + 22
    print(total)
except TypeError:
    print("Cannot add string and number directly")


# 5. IndexError example
students = ["Amit", "Priya", "Rahul"]

try:
    print(students[5])
except IndexError:
    print("Student index does not exist")


# 6. KeyError example
student = {
    "name": "Harsh",
    "age": 22,
}

try:
    print(student["city"])
except KeyError:
    print("City key does not exist")


# 7. Multiple except blocks
try:
    number1 = int("10")
    number2 = int("0")
    result = number1 / number2
    print(result)
except ValueError:
    print("Only numbers are allowed")
except ZeroDivisionError:
    print("Second number cannot be zero")


# 8. Catching error message using as
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Error message:", error)


# 9. else block
# else runs only when no error happens.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful:", result)


# 10. finally block
# finally always runs, whether error happens or not.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error handled")
finally:
    print("This finally block always runs")


# 11. Real-world example: safe age conversion
user_age = "25"

try:
    age = int(user_age)
except ValueError:
    print("Invalid age")
else:
    print("User age:", age)


# 12. Real-world example: safe average calculation
def calculate_average(total_marks, subject_count):
    try:
        average = total_marks / subject_count
    except ZeroDivisionError:
        return "Subject count cannot be zero"
    else:
        return average


print("Average:", calculate_average(450, 5))
print("Average:", calculate_average(450, 0))


# 13. Real-world example: safe dictionary access
def get_product_price(product):
    try:
        return product["price"]
    except KeyError:
        return "Price not available"


product1 = {"name": "Mouse", "price": 799}
product2 = {"name": "Keyboard"}

print("Product 1 price:", get_product_price(product1))
print("Product 2 price:", get_product_price(product2))


# 14. Real-world example: safe list access
def get_item_by_index(items, index):
    try:
        return items[index]
    except IndexError:
        return "Invalid index"


products = ["Mouse", "Keyboard", "Monitor"]

print("Selected product:", get_item_by_index(products, 1))
print("Selected product:", get_item_by_index(products, 5))


# 15. Real-world example: file handling with exception
try:
    file = open("missing_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")


# 16. Raise your own exception
# raise is used when we want to create an error manually.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Age is valid"


try:
    print(check_age(16))
except ValueError as error:
    print("Custom error:", error)


# 17. Real-world example: validate product quantity
def add_to_cart(product_name, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        return product_name + " added to cart. Quantity: " + str(quantity)
    except ValueError as error:
        return str(error)


print(add_to_cart("Mouse", 2))
print(add_to_cart("Keyboard", 0))


# 18. Avoid using bare except for real projects
# Bare except catches every error and can hide real problems.
# Better:
# except ValueError:
# except ZeroDivisionError:
# except Exception as error:


# 19. Catching general Exception
# Use this when you do not know exactly which error can happen.
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except Exception as error:
    print("General error handled:", error)


# 20. Real-world example: simple payment validation
def process_payment(balance, amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > balance:
            raise ValueError("Insufficient balance")

        remaining_balance = balance - amount
        return "Payment successful. Remaining balance: " + str(remaining_balance)
    except ValueError as error:
        return "Payment failed: " + str(error)


print(process_payment(5000, 1200))
print(process_payment(5000, 0))
print(process_payment(5000, 8000))


# 21. What should you know about exception handling?
# - try contains code that may give an error
# - except handles the error
# - Use specific error names when possible
# - else runs when there is no error
# - finally always runs
# - as error gives the actual error message
# - raise creates your own error
# - Exception can catch most errors
# - Avoid bare except in real projects
# - Exception handling keeps your program running safely
