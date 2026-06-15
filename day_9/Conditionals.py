# Conditionals in Python
# Conditionals help your program make decisions.
# Python uses if, elif, and else for decision making.


# 1. Basic if condition
age = 20

if age >= 18:
    print("You are eligible to vote")


# 2. if-else condition
temperature = 35

if temperature > 30:
    print("It is a hot day")
else:
    print("It is not too hot")


# 3. if-elif-else condition
# Example: student grade system.
marks = 82

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")


# 4. Comparison operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

wallet_balance = 500
product_price = 300

if wallet_balance >= product_price:
    print("You can buy this product")
else:
    print("Not enough balance")


# 5. Logical operator: and
# Both conditions must be True.
username = "harsh"
password = "python123"

if username == "harsh" and password == "python123":
    print("Login successful")
else:
    print("Invalid login")


# 6. Logical operator: or
# At least one condition must be True.
payment_method = "upi"

if payment_method == "cash" or payment_method == "upi":
    print("Payment accepted")
else:
    print("Payment method not accepted")


# 7. Logical operator: not
# not reverses True to False and False to True.
is_blocked = False

if not is_blocked:
    print("User can access the account")
else:
    print("User is blocked")


# 8. Real-world example: discount system
cart_amount = 2500
is_member = True

if cart_amount >= 2000 and is_member:
    print("You get 20% discount")
elif cart_amount >= 2000:
    print("You get 10% discount")
else:
    print("No discount")


# 9. Real-world example: traffic light
signal = "green"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")


# 10. Real-world example: ATM withdrawal
account_balance = 10000
withdraw_amount = 3000

if withdraw_amount <= 0:
    print("Enter a valid amount")
elif withdraw_amount > account_balance:
    print("Insufficient balance")
else:
    account_balance = account_balance - withdraw_amount
    print("Withdrawal successful")
    print("Remaining balance:", account_balance)


# 11. Nested if condition
# A condition inside another condition.
age = 21
has_id_card = True

if age >= 18:
    if has_id_card:
        print("Entry allowed")
    else:
        print("ID card required")
else:
    print("Entry not allowed")


# 12. Short if condition
is_online = True

if is_online:
    print("User is online")


# 13. Short if-else / ternary operator
marks = 45
result = "Pass" if marks >= 40 else "Fail"
print("Result:", result)


# 14. Checking value in list
available_sizes = ["S", "M", "L", "XL"]
selected_size = "M"

if selected_size in available_sizes:
    print("Size is available")
else:
    print("Size is not available")


# 15. Checking empty value
email = ""

if email:
    print("Email entered")
else:
    print("Email is required")


# 16. Real-world example: job eligibility
experience = 2
knows_python = True
knows_sql = True

if experience >= 1 and knows_python and knows_sql:
    print("Eligible for Python developer job")
elif knows_python:
    print("Eligible for Python intern role")
else:
    print("Need to learn Python first")


# 17. What should you know about conditionals?
# - Use if to check a condition
# - Use elif to check another condition
# - Use else when no condition is True
# - Use and when all conditions must be True
# - Use or when at least one condition must be True
# - Use not to reverse a condition
# - Indentation is very important in conditionals
# - Conditionals are used in login, payment, forms, discounts, and validations
