# Loops in Python
# Loops are used to repeat code multiple times.
# Python has two main loops: for loop and while loop.


# 1. for loop with a list
# Example: printing student names.
students = ["Amit", "Priya", "Rahul", "Neha"]

for student in students:
    print("Student:", student)


# 2. for loop with range()
# range() helps us repeat code a fixed number of times.
for number in range(1, 6):
    print("Number:", number)


# 3. Real-world example: total cart amount
cart_prices = [299, 499, 999, 199]
total_amount = 0

for price in cart_prices:
    total_amount = total_amount + price

print("Total cart amount:", total_amount)


# 4. Real-world example: attendance count
attendance = ["present", "absent", "present", "present", "absent"]
present_count = 0

for status in attendance:
    if status == "present":
        present_count = present_count + 1

print("Total present students:", present_count)


# 5. Loop through a string
name = "Harsh"

for letter in name:
    print("Letter:", letter)


# 6. Loop through a dictionary
student_marks = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 76,
}

for student, marks in student_marks.items():
    print(student, "scored", marks)


# 7. while loop
# A while loop runs until the condition becomes False.
count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1


# 8. Real-world example: password retry
correct_password = "python123"
entered_password = "wrong"
attempts = 1

while entered_password != correct_password and attempts < 3:
    print("Wrong password. Try again.")
    entered_password = "python123"
    attempts = attempts + 1

if entered_password == correct_password:
    print("Login successful")
else:
    print("Account locked")


# 9. break statement
# break stops the loop immediately.
products = ["mobile", "laptop", "camera", "keyboard"]

for product in products:
    if product == "camera":
        print("Camera found")
        break
    print("Checking:", product)


# 10. continue statement
# continue skips the current loop step and moves to the next one.
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue
    print("Number except 3:", number)


# 11. Nested loop
# A loop inside another loop.
# Example: printing classroom seats.
rows = 3
seats = 4

for row in range(1, rows + 1):
    for seat in range(1, seats + 1):
        print("Row", row, "Seat", seat)


# 12. Real-world example: multiplication table
table_number = 5

for number in range(1, 11):
    print(table_number, "x", number, "=", table_number * number)


# 13. Real-world example: filter passed students
students_result = [
    {"name": "Amit", "marks": 85},
    {"name": "Priya", "marks": 38},
    {"name": "Rahul", "marks": 60},
    {"name": "Neha", "marks": 25},
]

passed_students = []

for student in students_result:
    if student["marks"] >= 40:
        passed_students.append(student["name"])

print("Passed students:", passed_students)


# 14. else with loop
# The else block runs when the loop finishes normally without break.
search_item = "mouse"
items = ["keyboard", "monitor", "laptop"]

for item in items:
    if item == search_item:
        print("Item found")
        break
else:
    print("Item not found")


# 15. What should you know about loops?
# - Use for loop when you know what data you want to repeat over
# - Use while loop when repetition depends on a condition
# - Use range() to repeat code a fixed number of times
# - Use break to stop a loop
# - Use continue to skip one loop step
# - Loops are used for lists, dictionaries, strings, searching, counting, and totals
# - Be careful with while loops because they can run forever if the condition never changes
