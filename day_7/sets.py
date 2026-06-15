# Sets in Python
# A set is a collection of unique values.
# Sets are useful when you want to remove duplicates or compare groups of data.


# 1. Creating a set
fruits = {"apple", "banana", "mango"}
print("Fruits:", fruits)


# 2. Sets do not allow duplicate values
# Example: user IDs from website visits.
visitor_ids = {101, 102, 103, 101, 104, 102}
print("Unique visitor IDs:", visitor_ids)


# 3. Creating an empty set
# Important: {} creates an empty dictionary, not an empty set.
empty_set = set()
print("Empty set:", empty_set)


# 4. Add item to a set
skills = {"Python", "HTML", "CSS"}
skills.add("JavaScript")
print("Skills after adding:", skills)


# 5. Remove item from a set
skills.remove("HTML")
print("Skills after removing HTML:", skills)

# discard() is safer because it will not give an error if the item is missing.
skills.discard("Java")
print("Skills after discard:", skills)


# 6. Check if an item exists
# Example: checking if a student is present in class.
present_students = {"Amit", "Priya", "Neha", "Rahul"}

print("Is Priya present?", "Priya" in present_students)
print("Is Karan present?", "Karan" in present_students)


# 7. Convert list to set to remove duplicates
# Example: product categories selected by customers.
categories = ["mobile", "laptop", "mobile", "camera", "laptop"]
unique_categories = set(categories)

print("Original categories:", categories)
print("Unique categories:", unique_categories)


# 8. Union
# Union means all unique items from both sets.
# Example: students who joined online or offline classes.
online_students = {"Amit", "Priya", "Rahul"}
offline_students = {"Neha", "Rahul", "Karan"}

all_students = online_students.union(offline_students)
print("All students:", all_students)


# 9. Intersection
# Intersection means common items in both sets.
# Example: students who joined both online and offline classes.
both_classes = online_students.intersection(offline_students)
print("Students in both classes:", both_classes)


# 10. Difference
# Difference means items that are in one set but not in the other.
# Example: students who only joined online class.
only_online = online_students.difference(offline_students)
print("Only online students:", only_online)


# 11. Real-world example: common products in two shops
shop_a_products = {"milk", "bread", "rice", "tea"}
shop_b_products = {"tea", "sugar", "bread", "coffee"}

common_products = shop_a_products.intersection(shop_b_products)
only_shop_a = shop_a_products.difference(shop_b_products)
all_products = shop_a_products.union(shop_b_products)

print("Common products:", common_products)
print("Only in shop A:", only_shop_a)
print("All available products:", all_products)


# 12. Loop through a set
# Set order is not fixed, so output order can change.
for product in all_products:
    print("Product:", product)


# 13. What should you know about sets?
# - Sets store only unique values
# - Sets do not keep a fixed order
# - Sets are useful for removing duplicates
# - Sets are useful for comparing groups
# - Use union() for all items
# - Use intersection() for common items
# - Use difference() for items missing from another set
