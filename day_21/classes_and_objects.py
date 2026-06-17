# Day 21 - Classes and Objects in Python
# Class and object are part of Object-Oriented Programming, also called OOP.
#
# A class is a blueprint.
# An object is a real thing created from that blueprint.
#
# Example:
# Class  = Student
# Object = Harsh, Amit, Priya


# 1. Creating a simple class
class Student:
    name = "Harsh"
    age = 22


# Creating an object
student1 = Student()

print("1. Simple class and object")
print("Student name:", student1.name)
print("Student age:", student1.age)


print("-" * 45)


# 2. __init__ constructor
# __init__ runs automatically when we create an object.
# self means the current object.
class StudentProfile:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student2 = StudentProfile("Amit", 23, "Python")
student3 = StudentProfile("Priya", 24, "Data Science")

print("2. Constructor example")
print(student2.name, student2.age, student2.course)
print(student3.name, student3.age, student3.course)


print("-" * 45)


# 3. Method inside class
# A method is a function inside a class.
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Salary:", self.salary)


employee1 = Employee("Neha", "Developer", 50000)

print("3. Method inside class")
employee1.show_details()


print("-" * 45)


# 4. Real-world example: Bank account
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdraw successful")

    def check_balance(self):
        print("Current balance:", self.balance)


account1 = BankAccount("Harsh", 5000)

print("4. Bank account example")
account1.check_balance()
account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()


print("-" * 45)


# 5. Real-world example: Product
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - quantity
            print(quantity, self.name, "sold")
        else:
            print("Not enough stock")

    def show_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)


product1 = Product("Keyboard", 1299, 10)

print("5. Product example")
product1.show_product()
product1.sell(3)
product1.show_product()


print("-" * 45)


# 6. Instance variable and class variable
# Instance variable belongs to each object.
# Class variable is shared by all objects.
class CompanyEmployee:
    company_name = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print("Company:", CompanyEmployee.company_name)
        print("Name:", self.name)
        print("Salary:", self.salary)


emp1 = CompanyEmployee("Amit", 45000)
emp2 = CompanyEmployee("Priya", 55000)

print("6. Instance variable and class variable")
emp1.show_employee()
emp2.show_employee()


print("-" * 45)


# 7. Update object attribute
emp1.salary = 50000

print("7. Updated object attribute")
emp1.show_employee()


print("-" * 45)


# 8. Inheritance
# Inheritance allows one class to use features of another class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_teacher(self):
        self.show_person()
        print("Subject:", self.subject)


teacher1 = Teacher("Rahul", 30, "Math")

print("8. Inheritance example")
teacher1.show_teacher()


print("-" * 45)


# 9. Method overriding
# Child class can change parent class method behavior.
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

print("9. Method overriding")
animal.sound()
dog.sound()


print("-" * 45)


# 10. Real-world example: Student result using class
class Result:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        average = self.average_marks()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "Fail"

    def show_result(self):
        print("Student:", self.student_name)
        print("Marks:", self.marks)
        print("Total:", self.total_marks())
        print("Average:", self.average_marks())
        print("Grade:", self.grade())


result1 = Result("Harsh", [85, 90, 88])

print("10. Student result example")
result1.show_result()


print("-" * 45)


# 11. __str__ method
# __str__ controls what prints when we print the object directly.
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name + " from " + self.city


customer1 = Customer("Neha", "Mumbai")

print("11. __str__ method")
print(customer1)


print("-" * 45)


# 12. What should you know about classes and objects?
# - A class is a blueprint
# - An object is created from a class
# - __init__ is a constructor
# - self means current object
# - Attributes store object data
# - Methods are functions inside a class
# - Instance variables are different for each object
# - Class variables are shared by all objects
# - Inheritance allows one class to reuse another class
# - super() calls parent class code
# - Method overriding changes parent method behavior
# - __str__ controls object print output
# - Classes are useful for real-world things like users, products, accounts, and orders
print("12. Summary completed")
