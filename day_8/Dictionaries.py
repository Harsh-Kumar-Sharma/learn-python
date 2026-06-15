# Dictionaries in Python
# A dictionary stores data in key-value pairs.
# It is useful when each value has a name/label.


# 1. Creating a dictionary
student = {
    "name": "Harsh",
    "age": 22,
    "city": "Delhi",
}

print("Student:", student)


# 2. Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])


# 3. Using get()
# get() is safer because it does not give an error if the key is missing.
print("City:", student.get("city"))
print("Email:", student.get("email"))
print("Email with default:", student.get("email", "Not available"))


# 4. Adding a new key-value pair
student["course"] = "Python"
print("After adding course:", student)


# 5. Updating a value
student["age"] = 23
print("After updating age:", student)


# 6. Removing data from a dictionary
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After pop:", student)

# del also removes a key-value pair.
del student["course"]
print("After del:", student)


# 7. Checking if a key exists
print("Is name available?", "name" in student)
print("Is phone available?", "phone" in student)


# 8. Dictionary keys, values, and items
employee = {
    "id": 101,
    "name": "Amit",
    "role": "Developer",
    "salary": 45000,
}

print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())


# 9. Loop through dictionary keys
for key in employee:
    print("Key:", key)


# 10. Loop through dictionary values
for value in employee.values():
    print("Value:", value)


# 11. Loop through both keys and values
for key, value in employee.items():
    print(key, ":", value)


# 12. Real-world example: product details
product = {
    "product_id": "P1001",
    "name": "Wireless Mouse",
    "price": 799,
    "in_stock": True,
}

print("Product name:", product["name"])
print("Product price:", product["price"])

if product["in_stock"]:
    print("Product is available")
else:
    print("Product is out of stock")


# 13. Nested dictionary
# A dictionary can contain another dictionary.
user_profile = {
    "username": "harsh123",
    "email": "harsh@example.com",
    "address": {
        "house_no": 45,
        "city": "Delhi",
        "pincode": 110001,
    },
}

print("Username:", user_profile["username"])
print("User city:", user_profile["address"]["city"])


# 14. List of dictionaries
# This is very common in real projects, APIs, and databases.
students = [
    {"roll_no": 1, "name": "Amit", "marks": 85},
    {"roll_no": 2, "name": "Priya", "marks": 92},
    {"roll_no": 3, "name": "Rahul", "marks": 76},
]

for student_data in students:
    print(student_data["roll_no"], student_data["name"], student_data["marks"])


# 15. Update dictionary with another dictionary
account = {
    "name": "Neha",
    "balance": 5000,
}

new_details = {
    "balance": 6500,
    "account_type": "Savings",
}

account.update(new_details)
print("Updated account:", account)


# 16. Copy a dictionary
original_settings = {
    "theme": "dark",
    "notifications": True,
}

copied_settings = original_settings.copy()
copied_settings["theme"] = "light"

print("Original settings:", original_settings)
print("Copied settings:", copied_settings)


# 17. clear()
# clear() removes all items from a dictionary.
temporary_data = {
    "otp": 123456,
    "is_verified": False,
}

temporary_data.clear()
print("Temporary data after clear:", temporary_data)


# 18. Real-world example: counting repeated values
# Example: count how many times each fruit appears.
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
fruit_count = {}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

print("Fruit count:", fruit_count)


# 19. Real-world example: simple login check
users = {
    "harsh": "python123",
    "admin": "admin123",
}

username = "harsh"
password = "python123"

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid username or password")


# 20. What should you know about dictionaries?
# - Dictionaries store data as key-value pairs
# - Keys must be unique
# - Values can be any data type
# - Use [] when you are sure the key exists
# - Use get() when the key may be missing
# - Use update() to add or update multiple values
# - Use keys(), values(), and items() to read dictionary data
# - Dictionaries are very common in APIs, JSON data, forms, and databases
