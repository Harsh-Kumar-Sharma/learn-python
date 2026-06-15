# # Single line comment

letter= 'a'   #  A string could be a single character or a word or a sentence. It is a sequence of characters.
print(letter)
print(len(letter))  # 1 - because there is only one character in the string
first_name = 'Asabeneh'
print(first_name)
print(len(first_name))  # 9 - because there are 9 characters in the string

sentence = 'I am enjoying 30 days of python programming'
print(sentence)
print(len(sentence))  # 39 - because there are 39 characters in the string including spaces



#multi line comment
""" 
this is a multi line comment
in python   
we can use three double quotes or three single quotes to write a multi line comment
"""

multi_line_string = """This is a multi line string
in python           
we can use three double quotes or three single quotes to write a multi line string
"""
# Another way of doing the same thing

multi_line_string1 = '''This is a multi line string
in python   
we can use three double quotes or three single quotes to write a multi line string
'''

print(multi_line_string)
print(multi_line_string1)

print(len(multi_line_string))  # 122 - because there are 122 characters in the string including spaces and new line characters
print(len(multi_line_string1))  # 122 - because there are 122 characters in the string including spaces and new line characters



# string concatenation
first_name = 'Asabeneh' 
last_name = 'Yetayeh'
full_name = first_name + ' ' + last_name  # concatenating first name and last name with a space in between
print(full_name)

# string interpolation
age = 250
sentence = f'{full_name} is {age} years old.'  # using f-string for string interpolation
print(sentence)


# unpacking characters of a string
language = 'Python' 

a,b,c,d,e,f = language  # unpacking characters of the string into variables
print(a)  # P   
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n


# string indexing
language = 'Python'

print(language[0])  # P
print(language[1])  # y 
print(language[2])  # t
print(language[3])  # h
print(language[4])  # o
print(language[5])  # n

# If we want to start from right end we can use negative indexing. -1 is the last index

print(language[-1])  # n
print(language[-2])  # o    
print(language[-3])  # h
print(language[-4])  # t
print(language[-5])  # y
print(language[-6])  # P


#slicing strings
language = 'Python'

print(language[0:6])  # Python - slicing from index 0 to 5
print(language[0:3])  # Pyt - slicing from index 0 to 2
print(language[3:6])  # hon - slicing from index 3 to 5
print(language[:6])   # Python - slicing from index 0 to 5
print(language[0:])   # Python - slicing from index 0 to the end of the string
print(language[:])    # Python - slicing the whole string   


# Another way of slicing strings[start:stop:step]
language = 'Python' 
print(language[0:6:2])  # Pto - slicing from index 0 to 5 with a step of 2
print(language[0:6:3])  # Ph - slicing from index 0 to 5 with a step of 3
print(language[0:6:4])  # Po - slicing from index 0 to 5 with a step of 4
print(language[0:6:5])  # P - slicing from index 0 to 5 with a step of 5
print(language[0:6:6])  # P - slicing from index 0 to 5 with a step of 6


# Escape sequence

print('I am a \'single quoted\' string in python')  # using escape sequence to include single quotes in the string
print("I am a \"double quoted\" string in python")  # using escape sequence to include double quotes in the string
print('I am a backslash \\ string in python')  # using escape sequence to include backslash in the string
print('I am a new line \n string in python')  # using escape sequence to include new line in the string
print('I am a tab \t string in python')  # using escape sequence to include tab in the string


#string methods

print(language.upper())  # PYTHON - converting the string to uppercase
print(language.lower())  # python - converting the string to lowercase  
print(language.capitalize())  # Python - capitalizing the first letter of the string
print(language.title())  # Python - capitalizing the first letter of each word in the string
print(language.swapcase())  # pYTHON - swapping the case of the string
print(language.startswith('P'))  # True - checking if the string starts with 'P'
print(language.endswith('n'))  # True - checking if the string ends with 'n'
print(language.isalpha())  # True - checking if the string contains only alphabets
print(language.isdigit())  # False - checking if the string contains only digits
print(language.isalnum())  # True - checking if the string contains only alphanumeric characters
print(language.split())  # ['Python'] - splitting the string into a list of words
print(language.replace('P', 'J'))  # Jython - replacing 'P' with 'J' in the string
print(language.replace('o', 'a'))  # Pythan - replacing 'o' with 'a'
print(language.replace('P', 'J').replace('o', 'a'))  # Jythan - replacing 'P' with 'J' and 'o' with 'a'
print(language.find('t'))  # 2 - finding the index of the first occurrence of 't' in the string
print(language.find('z'))  # -1 - finding the index of the first occurrence of 'z' in the string, returns -1 if not found
print(language.count('o'))  # 1 - counting the number of occurrences of 'o' in the string
print(language.count('z'))  # 0 - counting the number of occurrences of 'z' in the string, returns 0 if not found
