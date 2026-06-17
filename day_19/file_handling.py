# Day 19 - File Handling in Python
# File handling means creating, reading, writing, appending, and deleting files.
# Python gives us a built-in open() function for working with files.
#
# Common file modes:
# "r"  read file
# "w"  write file, creates new file or overwrites old file
# "a"  append data at the end of file
# "x"  create new file, gives error if file already exists
# "r+" read and write


import csv
import json
import os


# Keep all practice files inside this folder.
current_folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_folder, "files_output")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


print("Day 19 - File Handling")
print("Output folder:", output_folder)
print("-" * 40)


# 1. Write text to a file
# "w" mode creates a file if it does not exist.
# If the file already exists, it overwrites old content.
notes_file = os.path.join(output_folder, "notes.txt")

file = open(notes_file, "w")
file.write("Python file handling is useful.\n")
file.write("We can create and write files.\n")
file.close()

print("1. notes.txt created")


print("-" * 40)


# 2. Read full file content
file = open(notes_file, "r")
content = file.read()
file.close()

print("2. Full file content")
print(content)


print("-" * 40)


# 3. Read file line by line
file = open(notes_file, "r")

print("3. Reading line by line")
for line in file:
    print(line.strip())

file.close()


print("-" * 40)


# 4. Append data to a file
# "a" mode adds new content at the end.
file = open(notes_file, "a")
file.write("Append mode adds new data at the end.\n")
file.close()

file = open(notes_file, "r")
print("4. After append")
print(file.read())
file.close()


print("-" * 40)


# 5. Best practice: use with open()
# with open() automatically closes the file.
tasks_file = os.path.join(output_folder, "tasks.txt")

with open(tasks_file, "w") as file:
    file.write("Complete Python practice\n")
    file.write("Revise file handling\n")
    file.write("Build mini project\n")

print("5. tasks.txt created using with open()")


print("-" * 40)


# 6. readlines()
# readlines() returns all lines as a list.
with open(tasks_file, "r") as file:
    task_lines = file.readlines()

print("6. Tasks as list:", task_lines)


print("-" * 40)


# 7. Check if file exists
if os.path.exists(tasks_file):
    print("7. tasks.txt exists")
else:
    print("7. tasks.txt does not exist")


print("-" * 40)


# 8. Real-world example: write student report
student_report_file = os.path.join(output_folder, "student_report.txt")

student = {
    "name": "Harsh",
    "math": 85,
    "science": 90,
    "english": 80,
}

total_marks = student["math"] + student["science"] + student["english"]
average_marks = total_marks / 3

with open(student_report_file, "w") as file:
    file.write("Student Report\n")
    file.write("Name: " + student["name"] + "\n")
    file.write("Total Marks: " + str(total_marks) + "\n")
    file.write("Average Marks: " + str(average_marks) + "\n")

print("8. Student report created")


print("-" * 40)


# 9. Real-world example: write CSV file
# CSV files are commonly used for Excel-like data.
csv_file = os.path.join(output_folder, "students.csv")

students = [
    ["Roll No", "Name", "Marks"],
    [1, "Amit", 85],
    [2, "Priya", 92],
    [3, "Rahul", 76],
]

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("9. students.csv created")


print("-" * 40)


# 10. Read CSV file
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    print("10. CSV data")
    for row in reader:
        print(row)


print("-" * 40)


# 11. Real-world example: write JSON file
# JSON is very common in APIs and backend projects.
json_file = os.path.join(output_folder, "product.json")

product = {
    "id": "P1001",
    "name": "Keyboard",
    "price": 1299,
    "in_stock": True,
}

with open(json_file, "w") as file:
    json.dump(product, file, indent=4)

print("11. product.json created")


print("-" * 40)


# 12. Read JSON file
with open(json_file, "r") as file:
    product_data = json.load(file)

print("12. JSON data")
print("Product name:", product_data["name"])
print("Product price:", product_data["price"])


print("-" * 40)


# 13. Real-world example: simple log file
log_file = os.path.join(output_folder, "app.log")

with open(log_file, "a") as file:
    file.write("User logged in\n")
    file.write("Product added to cart\n")
    file.write("Payment completed\n")

print("13. Log file updated")


print("-" * 40)


# 14. Count lines in a file
with open(log_file, "r") as file:
    lines = file.readlines()

print("14. Total log lines:", len(lines))


print("-" * 40)


# 15. Count words in a text file
with open(notes_file, "r") as file:
    text = file.read()

words = text.split()

print("15. Total words in notes.txt:", len(words))


print("-" * 40)


# 16. Handle file errors
missing_file = os.path.join(output_folder, "missing.txt")

try:
    with open(missing_file, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("16. missing.txt not found")


print("-" * 40)


# 17. List files in folder
print("17. Files in output folder")
for file_name in os.listdir(output_folder):
    print(file_name)


print("-" * 40)


# 18. Delete a file safely
temporary_file = os.path.join(output_folder, "temporary.txt")

with open(temporary_file, "w") as file:
    file.write("This file will be deleted")

if os.path.exists(temporary_file):
    os.remove(temporary_file)
    print("18. temporary.txt deleted")
else:
    print("18. temporary.txt not found")


print("-" * 40)


# 19. What should you know about file handling?
# - open() is used to open a file
# - "r" reads a file
# - "w" writes and overwrites a file
# - "a" appends data to a file
# - close() closes a file
# - with open() is best because it closes file automatically
# - read() reads full file content
# - readline() reads one line
# - readlines() reads all lines as a list
# - os.path.exists() checks if a file/folder exists
# - os.listdir() lists files in a folder
# - os.remove() deletes a file
# - csv module works with CSV files
# - json module works with JSON files
# - Always handle missing files using try-except
print("19. Summary completed")
