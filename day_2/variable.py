

first_name = "John"
last_name = "Doe"
email = "john@gmail.com"
phone_number = "123-456-7890"
age = 30
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}




# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Email: ', email)
print('Phone number: ', phone_number)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


# declaring multiple variables in one line
a,b,c = 1,2,3
print(a,b,c)


# how to access dist values
print(person_info['firstname'])
print(person_info['lastname'])
print(person_info['country'])

#how to change dict values

person_info['city'] = 'Espoo'
print(person_info['city'])
