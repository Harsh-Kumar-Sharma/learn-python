# Functions in Python
# A function is a reusable block of code.
# Functions help us avoid repeating the same code again and again.


# 1. Creating and calling a simple function
def say_hello():
    print("Hello, welcome to Python functions")


say_hello()


# 2. Function with parameter
# A parameter is a value that a function receives.
def greet_user(name):
    print("Hello", name)


greet_user("Harsh")
greet_user("Amit")


# 3. Function with multiple parameters
def add_numbers(num1, num2):
    total = num1 + num2
    print("Total:", total)


add_numbers(10, 20)
add_numbers(50, 70)


# 4. Function with return value
# return sends a value back from the function.
def calculate_total(price, quantity):
    total = price * quantity
    return total


bill_amount = calculate_total(500, 3)
print("Bill amount:", bill_amount)


# 5. Real-world example: discount calculation
def apply_discount(amount, discount_percent):
    discount = amount * discount_percent / 100
    final_amount = amount - discount
    return final_amount


final_bill = apply_discount(2000, 10)
print("Final bill after discount:", final_bill)


# 6. Default parameter
# A default value is used when no value is passed.
def order_food(item, quantity=1):
    print("Order:", quantity, item)


order_food("Pizza")
order_food("Burger", 3)


# 7. Keyword arguments
# We can pass values using parameter names.
def create_profile(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


create_profile(city="Delhi", name="Priya", age=24)


# 8. Real-world example: login check
def check_login(username, password):
    if username == "harsh" and password == "python123":
        return "Login successful"
    else:
        return "Invalid username or password"


login_result = check_login("harsh", "python123")
print(login_result)


# 9. Real-world example: marks result
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


student_result = check_result(75)
print("Student result:", student_result)


# 10. Real-world example: calculate average marks
def calculate_average(marks_list):
    total = 0

    for marks in marks_list:
        total = total + marks

    average = total / len(marks_list)
    return average


average_marks = calculate_average([80, 75, 90, 85])
print("Average marks:", average_marks)


# 11. Function returning multiple values
# Python returns multiple values as a tuple.
def get_employee_details():
    name = "Amit"
    role = "Developer"
    salary = 45000
    return name, role, salary


employee_name, employee_role, employee_salary = get_employee_details()
print("Employee name:", employee_name)
print("Employee role:", employee_role)
print("Employee salary:", employee_salary)


# 12. Local variable and global variable
company_name = "Tech Solutions"


def show_company():
    department = "IT"
    print("Company:", company_name)
    print("Department:", department)


show_company()

# department is a local variable, so it cannot be used outside the function.
# print(department)  # This will give an error.


# 13. *args
# *args is used when we do not know how many values will be passed.
def add_all_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


print("Total of many numbers:", add_all_numbers(10, 20, 30, 40))


# 14. **kwargs
# **kwargs is used when we do not know how many named values will be passed.
def print_user_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print_user_details(name="Neha", age=25, city="Mumbai", course="Python")


# 15. Real-world example: reusable invoice function
def generate_invoice(customer_name, items):
    total = 0

    print("Customer:", customer_name)
    print("Items:")

    for item_name, price in items.items():
        print(item_name, ":", price)
        total = total + price

    print("Total amount:", total)
    return total


invoice_items = {
    "Mouse": 799,
    "Keyboard": 1299,
    "USB Cable": 199,
}

generate_invoice("Harsh", invoice_items)


# 16. What should you know about functions?
# - Functions are reusable blocks of code
# - Use def to create a function
# - Call a function using its name and brackets
# - Parameters receive values inside a function
# - return sends a result back from a function
# - Default parameters give fallback values
# - Keyword arguments use parameter names while calling
# - Local variables work only inside the function
# - Global variables can be used outside and inside functions
# - *args accepts many normal values
# - **kwargs accepts many named values
# - Functions make code cleaner, reusable, and easier to understand
