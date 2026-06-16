# Day 13 - List Comprehension in Python
# List comprehension is a short way to create a new list from an existing list,
# string, range, or any iterable data.
#
# Normal syntax:
# new_list = [expression for item in iterable]
#
# With condition:
# new_list = [expression for item in iterable if condition]


# 1. Normal loop vs list comprehension
# Task: create a list of numbers from 1 to 5.
numbers = []

for number in range(1, 6):
    numbers.append(number)

print("Using normal loop:", numbers)

numbers_using_comprehension = [number for number in range(1, 6)]
print("Using list comprehension:", numbers_using_comprehension)


# 2. Create square numbers
# Expression: number * number
squares = [number * number for number in range(1, 6)]
print("Squares:", squares)


# 3. Create cube numbers
cubes = [number * number * number for number in range(1, 6)]
print("Cubes:", cubes)


# 4. Convert words to uppercase
names = ["harsh", "amit", "priya", "neha"]
upper_names = [name.upper() for name in names]

print("Uppercase names:", upper_names)


# 5. Convert words to lowercase
mixed_names = ["HARSH", "Amit", "PRIYA"]
lower_names = [name.lower() for name in mixed_names]

print("Lowercase names:", lower_names)


# 6. Get first letter of each word
fruits = ["apple", "banana", "mango", "orange"]
first_letters = [fruit[0] for fruit in fruits]

print("First letters:", first_letters)


# 7. Filtering even numbers
# if condition is written at the end.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# 8. Filtering odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]

print("Odd numbers:", odd_numbers)


# 9. Filter names by length
# Task: get names with more than 4 letters.
students = ["Amit", "Priya", "Rahul", "Neha", "Karan"]
long_names = [student for student in students if len(student) > 4]

print("Names with more than 4 letters:", long_names)


# 10. if-else inside list comprehension
# Syntax changes when we use both if and else:
# new_list = [value_if_true if condition else value_if_false for item in iterable]
marks = [85, 32, 76, 25, 90]
results = ["Pass" if mark >= 40 else "Fail" for mark in marks]

print("Results:", results)


# 11. Real-world example: add GST to prices
prices = [100, 250, 500, 1000]
prices_with_gst = [price + (price * 18 / 100) for price in prices]

print("Prices with GST:", prices_with_gst)


# 12. Real-world example: discount only on expensive products
product_prices = [299, 999, 1499, 199, 2499]

discounted_prices = [
    price - (price * 10 / 100) if price >= 1000 else price
    for price in product_prices
]

print("Discounted prices:", discounted_prices)


# 13. Remove empty strings from a list
emails = ["harsh@example.com", "", "admin@example.com", "", "test@example.com"]
valid_emails = [email for email in emails if email != ""]

print("Valid emails:", valid_emails)


# 14. Strip spaces from words
raw_names = [" Harsh ", " Amit", "Priya ", " Neha "]
clean_names = [name.strip() for name in raw_names]

print("Clean names:", clean_names)


# 15. List comprehension with string
# A string is also iterable, so we can loop through each character.
word = "Python"
letters = [letter for letter in word]

print("Letters:", letters)


# 16. Get vowels from a string
sentence = "Python is easy to learn"
vowels = [letter for letter in sentence if letter in "aeiou"]

print("Vowels:", vowels)


# 17. Split sentence and filter words
sentence = "Python is a powerful programming language"
words = sentence.split()
big_words = [word for word in words if len(word) > 5]

print("Words with more than 5 letters:", big_words)


# 18. List of dictionaries
# This is very common when working with API data or database records.
employees = [
    {"name": "Amit", "salary": 45000, "department": "IT"},
    {"name": "Priya", "salary": 55000, "department": "HR"},
    {"name": "Rahul", "salary": 35000, "department": "IT"},
    {"name": "Neha", "salary": 65000, "department": "Finance"},
]

employee_names = [employee["name"] for employee in employees]
print("Employee names:", employee_names)

high_salary_employees = [
    employee["name"]
    for employee in employees
    if employee["salary"] >= 50000
]

print("High salary employees:", high_salary_employees)

it_employees = [
    employee["name"]
    for employee in employees
    if employee["department"] == "IT"
]

print("IT employees:", it_employees)


# 19. Create list of dictionaries using comprehension
student_names = ["Amit", "Priya", "Rahul"]
student_records = [{"id": index + 1, "name": name} for index, name in enumerate(student_names)]

print("Student records:", student_records)


# 20. Nested list comprehension
# A nested list is a list inside another list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flat_list = [number for row in matrix for number in row]
print("Flat list:", flat_list)


# 21. Nested list comprehension with condition
even_from_matrix = [number for row in matrix for number in row if number % 2 == 0]

print("Even numbers from matrix:", even_from_matrix)


# 22. Create multiplication table using comprehension
table_of_5 = [5 * number for number in range(1, 11)]

print("Table of 5:", table_of_5)


# 23. Create pairs using nested comprehension
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

product_variants = [(color, size) for color in colors for size in sizes]

print("Product variants:", product_variants)


# 24. Set comprehension
# Similar idea, but it creates a set with unique values.
duplicate_numbers = [1, 2, 2, 3, 3, 4, 5]
unique_squares = {number * number for number in duplicate_numbers}

print("Unique squares set:", unique_squares)


# 25. Dictionary comprehension
# Similar idea, but it creates key-value pairs.
number_square_dict = {number: number * number for number in range(1, 6)}

print("Number square dictionary:", number_square_dict)


# 26. Dictionary comprehension with condition
even_square_dict = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}

print("Even square dictionary:", even_square_dict)


# 27. Real-world example: username generator
full_names = ["Harsh Sharma", "Amit Kumar", "Priya Singh"]
usernames = [name.lower().replace(" ", "_") for name in full_names]

print("Usernames:", usernames)


# 28. Real-world example: find available products
products = [
    {"name": "Mouse", "in_stock": True},
    {"name": "Keyboard", "in_stock": False},
    {"name": "Monitor", "in_stock": True},
]

available_products = [
    product["name"]
    for product in products
    if product["in_stock"]
]

print("Available products:", available_products)


# 29. When should you use list comprehension?
# Use it when the logic is short and easy to read.
# If the logic becomes too long or confusing, use a normal for loop.


# 30. What should you know about list comprehension?
# - It creates a new list in one line
# - It is shorter than a normal for loop
# - It can transform values
# - It can filter values using if
# - It can use if-else for decisions
# - It can work with lists, strings, ranges, dictionaries, and nested lists
# - Set comprehension creates a set
# - Dictionary comprehension creates a dictionary
# - Keep it readable; do not make it too complex
