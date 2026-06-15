# Arithmetic Operations in Python

# Addition
print('Addition: ', 2 + 3) # 5
# Subtraction
print('Subtraction: ', 5 - 3) # 2
# Multiplication
print('Multiplication: ', 2 * 3) # 6
# Division
print('Division: ', 6 / 2) # 3.0
# Modulus
print('Modulus: ', 5 % 2) # 1    # gives the remaining number after division
# Floor Division
print('Floor Division: ', 7 // 2) # 3  gives without the floating number or without the remaining
# Exponentiation
print('Exponentiation: ', 2 ** 3) # 8  # it means 2 * 2 * 2




# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)



# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))


# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b


# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


#calculating the area of a circle
radius = 10
pi = 3.14
area_of_circle = pi * radius ** 2
print('Area of a circle with radius 10 is: ', area_of_circle)

# calculating the area of a rectangle
length = 20 
width = 10
area_of_rectangle = length * width
print('Area of a rectangle with length 20 and width 10 is: ', area_of_rectangle)


print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


#boolean operators
print(3 > 2 and 2 < 3)  # True, because both conditions are true
print(3 > 2 and 2 > 3)  # False, because the second condition is false
print(3 < 2 and 2 > 3)  # False, because both conditions are false
print(3 > 2 or 2 > 3)   # True, because the first condition is true
print(3 < 2 or 2 > 3)   # False, because both conditions are false
print(3 < 2 or 2 < 3)   # True, because the second condition is true
print(not 3 > 2)        # False, because 3 > 2 is true, but we are using not operator to reverse the result
print(not 3 < 2)        # True, because 3 < 2 is false, but we are using not operator to reverse the result     


#anthoer way to compare two values
print('True' if 3 > 2 else 'False')  # True, because 3 is greater than 2
print('True' if 3 < 2 else 'False')  # False, because 3 is greater than 2

# Another way comparison
# True - because the data values are the same
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True



