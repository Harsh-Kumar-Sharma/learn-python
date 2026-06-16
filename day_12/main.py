# Day 12 - Modules in Python
# A module is a Python file that contains reusable code.
# We use modules to organize code and avoid writing the same code again.


# 1. Importing our own module
# my_module.py is a file in the same folder.
import my_module

full_name = my_module.generate_full_name("Harsh", "Sharma")
print("Full name:", full_name)

total = my_module.add_two_numbers(10, 20)
print("Total:", total)

weight = my_module.calculate_weight(60)
print("Weight for 60 kg mass:", weight)

print("Person country:", my_module.person["country"])


# 2. Import specific functions from a module
from my_module import add_two_numbers, generate_full_name

print("Imported full name:", generate_full_name("Amit", "Kumar"))
print("Imported sum:", add_two_numbers(50, 70))


# 3. Import and rename function/module
from my_module import generate_full_name as full_name_generator
from my_module import gravity as earth_gravity

print("Renamed function:", full_name_generator("Priya", "Singh"))
print("Renamed gravity:", earth_gravity)


# 4. OS module
# os is used to work with folders, files, and operating system paths.
import os

current_folder = os.getcwd()
print("Current folder:", current_folder)

day_12_path = os.path.dirname(os.path.abspath(__file__))   # __file__ gives the path of the current file (main.py)
print("Day 12 path:", day_12_path)

print("Files in day_12 folder:", os.listdir(day_12_path))   # os.listdir() gives a list of all files and folders in the specified path.


# 5. Sys module
# sys gives information about Python runtime.
import sys

# sys.version gives the version of Python that is currently running.
#  It includes major, minor, and micro versions, as well as additional information about the build and compiler.
print("Python version:", sys.version) 

# sys.argv is a list of command-line arguments passed to the script. 
# The first element (sys.argv[0]) is the name of the script itself.
#  If you run the script with additional arguments, they will be stored in sys.argv[1], sys.argv[2], etc.
print("Script name:", sys.argv[0]) 

# sys.path is a list of directories that Python searches for modules when you try to import them.
#  The first value (sys.path[0]) is usually the directory containing the script that is being executed.
#  If you run the script from the command line, it will be the current working directory.
#  If you run it from an IDE, it may be the project folder or another directory depending on the IDE's configuration.
print("Python path first value:", sys.path[0]) 


# 6. Statistics module
# statistics is useful for mean, median, mode, etc.
import statistics

ages = [20, 22, 22, 24, 25, 26, 22]

print("Mean age:", statistics.mean(ages))
print("Median age:", statistics.median(ages))
print("Most common age:", statistics.mode(ages))


# 7. Math module
# math is useful for mathematical operations.
import math

print("PI value:", math.pi)
print("Square root of 64:", math.sqrt(64))
print("2 power 3:", math.pow(2, 3))
print("Floor of 9.81:", math.floor(9.81))
print("Ceil of 9.81:", math.ceil(9.81))


# 8. Import specific function from math
from math import sqrt, floor

print("Imported sqrt:", sqrt(100))
print("Imported floor:", floor(7.99))


# 9. String module
# string gives ready-made groups of letters, digits, and symbols.
import string

print("All lowercase letters:", string.ascii_lowercase)
print("All digits:", string.digits)
print("Punctuation symbols:", string.punctuation)


# 10. Random module
# random is used to generate random numbers or pick random values.
import random

random_number = random.randint(1, 10)
print("Random number from 1 to 10:", random_number)

otp = random.randint(100000, 999999)
print("Generated OTP:", otp)

colors = ["red", "green", "blue", "yellow"]
selected_color = random.choice(colors)
print("Random selected color:", selected_color)


# 11. Real-world example: random user ID generator
def random_user_id(length):
    characters = string.ascii_letters + string.digits
    user_id = ""

    for _ in range(length):
        user_id = user_id + random.choice(characters)

    return user_id


print("Random user ID:", random_user_id(6))


# 12. Real-world example: RGB color generator
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return "rgb(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"


print("Random RGB color:", rgb_color_gen())


# 13. Real-world example: simple password generator
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password = password + random.choice(characters)

    return password


print("Generated password:", generate_password(10))


# 14. What should you know about modules?
# - A module is a .py file
# - Use import module_name to import a full module
# - Use module_name.function_name() to call a function from a full module
# - Use from module_name import function_name to import a specific function
# - Use as to rename a module, function, or variable during import
# - Python has many built-in modules like os, sys, math, random, string, statistics
# - Modules help keep code clean, reusable, and organized
# - Do not name your file the same as a built-in module, like math.py or random.py
