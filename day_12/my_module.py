# This is our own module.
# A module is just a Python file that contains reusable code.


gravity = 9.8

person = {
    "first_name": "Harsh",
    "last_name": "Sharma",
    "country": "India",
}


def generate_full_name(first_name, last_name):
    return first_name + " " + last_name


def add_two_numbers(num1, num2):
    return num1 + num2


def calculate_weight(mass):
    return mass * gravity
