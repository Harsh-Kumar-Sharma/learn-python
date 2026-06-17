# Day 1 to Day 10 - Mini Project Assignments
# These 2 assignments use everything you learned from Day 1 to Day 10:
# print, variables, operators, strings, lists, tuples, sets, dictionaries,
# conditionals, and loops.


# ============================================================
# Assignment 1: Grocery Store Billing System
# ============================================================
# Real-world problem:
# A small grocery store wants a simple billing system.
#
# Concepts used:
# - print() for output
# - variables for store/customer details
# - strings for names and bill text
# - lists for multiple cart items
# - dictionaries for product details
# - tuples for fixed shop location
# - sets for unique product categories
# - operators for total, discount, and tax
# - conditionals for discount logic
# - loops for reading cart items
#
# Your task:
# 1. Print store name and customer name.
# 2. Store products in a cart.
# 3. Calculate subtotal.
# 4. Apply discount if subtotal is 2000 or more.
# 5. Add GST.
# 6. Print final bill.


print("Assignment 1: Grocery Store Billing System")

store_name = "Fresh Mart"
customer_name = "Harsh Sharma"
store_location = ("Delhi", "India")

cart_items = [
    {"name": "Rice", "category": "Grocery", "price": 1200, "quantity": 1},
    {"name": "Oil", "category": "Grocery", "price": 650, "quantity": 1},
    {"name": "Tea", "category": "Beverage", "price": 250, "quantity": 2},
    {"name": "Soap", "category": "Personal Care", "price": 80, "quantity": 3},
]

subtotal = 0
categories = set()

print("Store:", store_name)
print("Customer:", customer_name)
print("Location:", store_location[0] + ", " + store_location[1])
print("Items:")

for item in cart_items:
    item_total = item["price"] * item["quantity"]
    subtotal = subtotal + item_total
    categories.add(item["category"])

    print(item["name"], "-", item["quantity"], "x", item["price"], "=", item_total)

if subtotal >= 2000:
    discount = subtotal * 10 / 100
else:
    discount = 0

amount_after_discount = subtotal - discount
gst = amount_after_discount * 18 / 100
final_amount = amount_after_discount + gst

print("Unique categories:", categories)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final amount:", final_amount)


print("\n" + "=" * 60 + "\n")


# ============================================================
# Assignment 2: Student Result Management System
# ============================================================
# Real-world problem:
# A school wants a simple result system for students.
#
# Concepts used:
# - print() for report output
# - variables for school and passing marks
# - strings for names and grades
# - lists for multiple students
# - dictionaries for each student record
# - tuples for fixed subject names
# - sets for unique grades
# - operators for total and average
# - conditionals for pass/fail and grade
# - loops for processing all students
#
# Your task:
# 1. Store multiple students and marks.
# 2. Calculate total and average marks.
# 3. Decide grade using conditionals.
# 4. Decide pass/fail.
# 5. Print a report for every student.
# 6. Print all unique grades.


print("Assignment 2: Student Result Management System")

school_name = "Bright Future School"
passing_marks = 40
subjects = ("Math", "Science", "English")

students = [
    {"roll_no": 1, "name": "Amit", "marks": [85, 90, 78]},
    {"roll_no": 2, "name": "Priya", "marks": [92, 88, 95]},
    {"roll_no": 3, "name": "Rahul", "marks": [35, 42, 39]},
    {"roll_no": 4, "name": "Neha", "marks": [65, 72, 70]},
]

unique_grades = set()
passed_students = []
failed_students = []

print("School:", school_name)
print("Subjects:", subjects)

for student in students:
    total_marks = 0

    for mark in student["marks"]:
        total_marks = total_marks + mark

    average_marks = total_marks / len(student["marks"])

    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    elif average_marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    unique_grades.add(grade)

    is_passed = True

    for mark in student["marks"]:
        if mark < passing_marks:
            is_passed = False
            break

    if is_passed:
        result = "Pass"
        passed_students.append(student["name"])
    else:
        result = "Fail"
        failed_students.append(student["name"])

    print("------------------------------")
    print("Roll No:", student["roll_no"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", total_marks)
    print("Average:", average_marks)
    print("Grade:", grade)
    print("Result:", result)

print("------------------------------")
print("Passed students:", passed_students)
print("Failed students:", failed_students)
print("Unique grades:", unique_grades)
