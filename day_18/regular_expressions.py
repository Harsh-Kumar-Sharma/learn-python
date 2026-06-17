# Day 18 - Regular Expressions in Python
# Regular expressions, also called regex, are used to search, match,
# validate, split, and clean text patterns.
#
# Python has a built-in module called re for regular expressions.


import re


# 1. Basic search
# re.search() checks if a pattern exists anywhere in the text.
text = "Python is easy to learn"
result = re.search("Python", text)

print("1. Basic search")
if result:
    print("Pattern found")
else:
    print("Pattern not found")


print("-" * 40)


# 2. match()
# re.match() checks only from the start of the string.
text = "Python programming"

print("2. match()")
print(re.match("Python", text))
print(re.match("programming", text))


print("-" * 40)


# 3. findall()
# re.findall() returns all matching values as a list.
text = "My numbers are 9876543210 and 9123456780"
numbers = re.findall("[0-9]+", text)

print("3. findall()")
print("Numbers found:", numbers)


print("-" * 40)


# 4. split()
# re.split() splits text using a pattern.
text = "apple,banana;orange mango"
fruits = re.split("[,; ]+", text)

print("4. split()")
print("Fruits:", fruits)


print("-" * 40)


# 5. sub()
# re.sub() replaces matching text.
text = "My phone number is 9876543210"
hidden_text = re.sub("[0-9]", "*", text)

print("5. sub()")
print("Hidden text:", hidden_text)


print("-" * 40)


# 6. Important regex symbols
# .      any character except new line
# ^      starts with
# $      ends with
# *      zero or more times
# +      one or more times
# ?      zero or one time
# {n}    exactly n times
# {n,m}  between n and m times
# []     character set
# \d     digit, same as [0-9]
# \D     not a digit
# \w     word character: letters, digits, underscore
# \W     not a word character
# \s     whitespace
# \S     not whitespace


# 7. Validate mobile number
# Real-world problem:
# Check if an Indian mobile number has exactly 10 digits and starts with 6-9.
mobile_number = "9876543210"
pattern = "^[6-9][0-9]{9}$"

print("7. Validate mobile number")
if re.match(pattern, mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")


print("-" * 40)


# 8. Validate email address
# Real-world problem:
# Check if email looks valid.
email = "harsh@example.com"
email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"

print("8. Validate email")
if re.match(email_pattern, email):
    print("Valid email")
else:
    print("Invalid email")


print("-" * 40)


# 9. Extract emails from text
message = "Contact harsh@example.com or admin@test.in for help"
emails = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+", message)

print("9. Extract emails")
print("Emails:", emails)


print("-" * 40)


# 10. Extract dates
# Real-world problem:
# Extract dates written in dd-mm-yyyy format.
report = "Invoice dates are 16-06-2026 and 25-12-2026"
dates = re.findall("[0-9]{2}-[0-9]{2}-[0-9]{4}", report)

print("10. Extract dates")
print("Dates:", dates)


print("-" * 40)


# 11. Validate vehicle number
# Real-world problem:
# Check a simple Indian vehicle number format like DL01AB1234.
vehicle_number = "DL01AB1234"
vehicle_pattern = "^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"

print("11. Validate vehicle number")
if re.match(vehicle_pattern, vehicle_number):
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")


print("-" * 40)


# 12. Clean extra spaces
dirty_text = "Python     is     easy      to learn"
clean_text = re.sub("\\s+", " ", dirty_text)

print("12. Clean extra spaces")
print("Before:", dirty_text)
print("After:", clean_text)


print("-" * 40)


# 13. Remove special characters
username = "harsh@123#!"
clean_username = re.sub("[^a-zA-Z0-9]", "", username)

print("13. Remove special characters")
print("Clean username:", clean_username)


print("-" * 40)


# 14. Check password strength
# Real-world problem:
# Password must have at least 8 characters, one uppercase, one lowercase,
# one digit, and one special character.
password = "Python@123"

has_length = len(password) >= 8
has_upper = re.search("[A-Z]", password)
has_lower = re.search("[a-z]", password)
has_digit = re.search("[0-9]", password)
has_special = re.search("[^a-zA-Z0-9]", password)

print("14. Check password strength")
if has_length and has_upper and has_lower and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")


print("-" * 40)


# 15. Extract price values
bill_text = "Rice price is 1200, oil price is 650, tea price is 250"
prices = re.findall("[0-9]+", bill_text)

print("15. Extract price values")
print("Prices:", prices)


print("-" * 40)


# 16. Starts with and ends with
file_name = "report_2026.pdf"

print("16. Starts with and ends with")
print("Starts with report:", bool(re.search("^report", file_name)))
print("Ends with pdf:", bool(re.search("pdf$", file_name)))


print("-" * 40)


# 17. Using groups
# Groups help us capture parts of a pattern.
full_name = "Harsh Sharma"
name_match = re.search("([A-Za-z]+) ([A-Za-z]+)", full_name)

print("17. Using groups")
if name_match:
    print("First name:", name_match.group(1))
    print("Last name:", name_match.group(2))


print("-" * 40)


# 18. Compile regex
# re.compile() saves a regex pattern for reuse.
phone_pattern = re.compile("^[6-9][0-9]{9}$")

print("18. Compile regex")
print("Is valid:", bool(phone_pattern.match("9123456780")))
print("Is valid:", bool(phone_pattern.match("1234567890")))


print("-" * 40)


# 19. Real-world example: extract data from log line
log_line = "[2026-06-17 10:30:45] ERROR User login failed"
log_pattern = "\\[(.*?)\\] (ERROR|INFO|WARNING) (.*)"
log_match = re.search(log_pattern, log_line)

print("19. Extract data from log line")
if log_match:
    print("Time:", log_match.group(1))
    print("Level:", log_match.group(2))
    print("Message:", log_match.group(3))


print("-" * 40)


# 20. What should you know about regex?
# - Use re.search() to find a pattern anywhere
# - Use re.match() to check from the beginning
# - Use re.findall() to get all matches
# - Use re.split() to split using patterns
# - Use re.sub() to replace matching text
# - Use ^ for starts with and $ for ends with
# - Use \d or [0-9] for digits
# - Use + for one or more characters
# - Use {n} for exact length
# - Regex is useful for validation, extraction, and text cleaning
print("20. Summary completed")
