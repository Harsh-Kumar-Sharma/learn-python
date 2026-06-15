# Tuples in Python
# A tuple is like a list, but you cannot change its values after creating it.
# This is useful for real-world data that should stay fixed.


# 1. Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)


# 2. Tuple with fixed personal information
# Example: Aadhaar/card record style data should not change accidentally.
person = ("Harsh", 22, "India")

print("Name:", person[0])
print("Age:", person[1])
print("Country:", person[2])


# 3. Tuple unpacking
# This makes tuple values easy to read.
name, age, country = person

print("Unpacked name:", name)
print("Unpacked age:", age)
print("Unpacked country:", country)


# 4. Real-world example: GPS location
# Latitude and longitude are often stored together as a tuple.
office_location = (28.6139, 77.2090)

latitude, longitude = office_location
print("Office latitude:", latitude)
print("Office longitude:", longitude)


# 5. Real-world example: menu item
# Each menu item has a name, price, and availability.
menu_item = ("Paneer Pizza", 249, True)

item_name, price, is_available = menu_item

print("Item:", item_name)
print("Price:", price)
print("Available:", is_available)


# 6. Tuples are immutable
# You cannot update a tuple value directly.
student_marks = ("Rahul", 85, 90, 78)

print("Student record:", student_marks)

# This will give an error because tuples cannot be changed:
# student_marks[1] = 95


# 7. Nested tuple
# Example: a train ticket with passenger details and route details.
train_ticket = (
    "PNR12345",
    ("Harsh", 22),
    ("Delhi", "Mumbai"),
)

pnr, passenger, route = train_ticket
passenger_name, passenger_age = passenger
source, destination = route

print("PNR:", pnr)
print("Passenger:", passenger_name)
print("Passenger age:", passenger_age)
print("From:", source)
print("To:", destination)


# 8. Tuple as dictionary key
# Tuples can be used as keys because they do not change.
# Example: storing distance between two cities.
city_distance = {
    ("Delhi", "Mumbai"): 1400,
    ("Delhi", "Jaipur"): 280,
    ("Mumbai", "Pune"): 150,
}

print("Delhi to Mumbai distance:", city_distance[("Delhi", "Mumbai")], "km")


# 9. Tuple inside a list
# A list can hold many fixed records.
employees = [
    (101, "Amit", "Developer"),
    (102, "Priya", "Designer"),
    (103, "Neha", "Manager"),
]

for employee_id, employee_name, role in employees:
    print(employee_id, employee_name, role)


# 10. When should you use a tuple?
# Use a tuple when:
# - The data should not change
# - The order of values matters
# - You want to group related values together
