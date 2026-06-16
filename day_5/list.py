empty_list =  list()  # creating an empty list using the list() constructor
print(empty_list)  # []


fruits = ['banana', 'orange', 'mango', 'lemon']  # creating a list of fruits
print(fruits)  # ['banana', 'orange', 'mango', 'lemon

numbers = [1, 2, 3, 4, 5]  # creating a list of numbers
print(numbers)  # [1, 2, 3, 4, 5]


mixed_data_types = ['Asabeneh', 250, True, [1, 2, 3], {'country': 'Finland', 'city': 'Helsinki'}]  # creating a list of mixed data types
print(mixed_data_types)  # ['Asabeneh', 250, True, [1, 2, 3], {'country': 'Finland', 'city': 'Helsinki'}]


#Modifying list items
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits[0] = 'avocado'  # changing the first item of the list
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon]


#Accessing list items
fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits[0])  # banana
print(fruits[1])  # orange  


#  Slicing lists
fruits = ['banana', 'orange', 'mango', 'lemon'] 

print(fruits[0:3])  # ['banana', 'orange', 'mango'] - slicing from index 0 to 2
print(fruits[1:])   # ['orange', 'mango', 'lemon'] - slicing from index 1 to the end of the list
print(fruits[:3])   # ['banana', 'orange', 'mango'] - slicing from index 0 to 2
print(fruits[:])    # ['banana', 'orange', 'mango', 'lemon'] - slicing the whole list   


#Check Item 
fruits = ['banana', 'orange', 'mango', 'lemon']

print('banana' in fruits)  # True - because banana is in the list
print('grape' in fruits)   # False - because grape is not in the list


#Append items to a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('grape')  # adding grape to the end of the list
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'grape']


#insert items to a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'watermelon')  # inserting watermelon at index 2
print(fruits)  # ['banana', 'orange', 'watermelon', 'mango', 'lemon']

#remove items from a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('orange')  # removing orange from the list    
print(fruits)  # ['banana', 'mango', 'lemon']

#pop items from a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()  # removing the last item from the list    
print(fruits)  # ['banana', 'orange', 'mango']

# deleting items from a list
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]  # deleting the first item from the list
print(fruits)  # ['orange', 'mango', 'lemon']


#clear items from a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()  # clearing all items from the list
print(fruits)  # []

#copying a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()  # copying the list
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']

#joining two lists
list_one = [1, 2, 3]    
list_two = [4, 5, 6]
joined_list = list_one + list_two  # joining two lists using the + operator
print(joined_list)  # [1, 2, 3, 4, 5, 6]

#joining two lists using the extend() method
# The extend() method adds the elements of list_two to the end of list_one, modifying list_one in place.
list_one = [1, 2, 3]    
list_two = [4, 5, 6]
list_one.extend(list_two)  # joining two lists using the extend() method
print(list_one)  # [1, 2, 3, 4, 5, 6]


#counting items in a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(fruits.count('banana'))  # 2 - because banana appears twice in the list   

#finding the index of an item in a list
fruits = ['banana', 'orange', 'mango', 'lemon'] 
print(fruits.index('mango'))  # 2 - because mango is at index 2 in the list


#reversing a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()  # reversing the list
print(fruits)  # ['lemon', 'mango', 'orange', 'banana

#sorting a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()  # sorting the list in ascending order
print(fruits)  # ['banana', 'lemon', 'mango', 'orange

#sorting a list in descending order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort(reverse=True)  # sorting the list in descending order   
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

#sorting a list in reverse order using the sorted() function
fruits = ['banana', 'orange', 'mango', 'lemon'] 
sorted_fruits = sorted(fruits, reverse=True)  # sorting the list in reverse order using the sorted() function
print(sorted_fruits)  # ['orange', 'mango', 'lemon', 'banana']


