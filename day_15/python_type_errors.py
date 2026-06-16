# Day 15 - Python Error Types
# Errors are problems in code that stop the program or give wrong results.
# As a fresher, you should learn common error types and how to fix them.
#
# In this file, error-causing lines are commented.
# You can uncomment them one by one to see the real error.


# 1. SyntaxError
# SyntaxError happens when Python grammar/rules are wrong.

# Wrong:
# print("Hello"

# Correct:
print("Hello")


# 2. NameError
# NameError happens when you use a variable that is not created.

# Wrong:
# print(username)

# Correct:
username = "Harsh"
print("Username:", username)


# 3. TypeError
# TypeError happens when you use the wrong data type in an operation.

# Wrong:
# age = 22
# print("Age: " + age)

# Correct:
age = 22
print("Age:", age)
print("Age: " + str(age))


# 4. IndexError
# IndexError happens when you use a list index that does not exist.

students = ["Amit", "Priya", "Rahul"]

# Wrong:
# print(students[5])

# Correct:
print("First student:", students[0])
print("Last student:", students[-1])


# 5. ValueError
# ValueError happens when the value is wrong for the operation.

# Wrong:
# number = int("abc")

# Correct:
number = int("123")
print("Converted number:", number)


# 6. KeyError
# KeyError happens when a dictionary key does not exist.

student = {
    "name": "Harsh",
    "age": 22,
}

# Wrong:
# print(student["city"])

# Correct:
print("Student name:", student["name"])
print("Student city:", student.get("city", "City not available"))


# 7. AttributeError
# AttributeError happens when you use a method/property that does not exist
# for that data type.

name = "harsh"

# Wrong:
# name.append("sharma")

# Correct:
print("Uppercase name:", name.upper())


# 8. ImportError / ModuleNotFoundError
# This happens when Python cannot import a module or function.

# Wrong:
# import not_existing_module

# Correct:
import math

print("Square root:", math.sqrt(64))


# 9. ZeroDivisionError
# This happens when you divide a number by zero.

# Wrong:
# result = 10 / 0

# Correct:
num1 = 10
num2 = 2
print("Division result:", num1 / num2)


# 10. FileNotFoundError
# This happens when you try to open a file that does not exist.

# Wrong:
# file = open("missing_file.txt")

# Correct:
file_name = "example.txt"
print("Before opening a file, check that", file_name, "exists")


# 11. IndentationError
# Python uses indentation to understand code blocks.

# Wrong:
# if True:
# print("This line is not indented")

# Correct:
if True:
    print("This line is correctly indented")


# 12. TabError
# TabError happens when tabs and spaces are mixed badly for indentation.
# Best practice: use 4 spaces for indentation.

if age >= 18:
    print("Adult")


# 13. UnboundLocalError
# This happens when a local variable is used before assigning it inside a function.

message = "Global message"


def show_message():
    local_message = "Local message"
    print(local_message)


show_message()


# 14. FloatingPointError
# This is uncommon in normal beginner code.
# Floating point numbers can still have precision surprises.

print("0.1 + 0.2:", 0.1 + 0.2)
print("Rounded value:", round(0.1 + 0.2, 2))


# 15. OverflowError
# This can happen when a number is too large for some operations.

# Wrong:
# print(math.exp(1000))

# Correct:
print("Power example:", 2 ** 10)


# 16. Real-world example: safe user age conversion
user_input_age = "22"

if user_input_age.isdigit():
    converted_age = int(user_input_age)
    print("User age:", converted_age)
else:
    print("Please enter a valid age")


# 17. Real-world example: safe dictionary reading
product = {
    "name": "Mouse",
    "price": 799,
}

print("Product:", product.get("name", "Unknown product"))
print("Stock:", product.get("stock", "Stock not available"))


# 18. Real-world example: safe list access
items = ["keyboard", "mouse", "monitor"]
index = 1

if index < len(items):
    print("Selected item:", items[index])
else:
    print("Invalid item index")


# 19. Real-world example: safe division
total_marks = 450
subject_count = 5

if subject_count != 0:
    average = total_marks / subject_count
    print("Average marks:", average)
else:
    print("Subject count cannot be zero")


# 20. Quick error summary
errors = {
    "SyntaxError": "Python grammar is wrong",
    "NameError": "Variable or function name is not found",
    "TypeError": "Wrong data type is used",
    "IndexError": "List index is out of range",
    "ValueError": "Value is not valid for operation",
    "KeyError": "Dictionary key is missing",
    "AttributeError": "Method or property does not exist",
    "ModuleNotFoundError": "Module is not found",
    "ZeroDivisionError": "Cannot divide by zero",
    "FileNotFoundError": "File does not exist",
    "IndentationError": "Code block spacing is wrong",
}

for error_name, meaning in errors.items():
    print(error_name, ":", meaning)


# 21. What should you know about Python errors?
# - Read the last line of the error message first
# - The traceback shows where the error happened
# - SyntaxError usually means spelling, brackets, quotes, or indentation issue
# - NameError usually means a variable name is wrong or not created
# - TypeError usually means wrong data type
# - IndexError means the list position does not exist
# - KeyError means the dictionary key does not exist
# - Use get() for safer dictionary access
# - Check length before accessing list indexes
# - Convert data types carefully using int(), str(), float()
# - Later, use try-except to handle errors without stopping the program
