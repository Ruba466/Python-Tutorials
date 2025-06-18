# -------------------- LIST --------------------
print("----- LIST OPERATIONS -----")
fruits = ['apple', 'banana', 'mango']

# Common list functions and methods
fruits.append('orange')        # add item
fruits.insert(1, 'grape')      # insert at index
fruits.remove('banana')        # remove item
popped = fruits.pop()          # pop last item
fruits.sort()                  # sort
fruits.reverse()               # reverse
count_apple = fruits.count('apple')
length = len(fruits)

print("Fruits List:", fruits)
print("Popped Item:", popped)
print("Count of 'apple':", count_apple)
print("Length of list:", length)


# -------------------- DICTIONARY --------------------
print("\n----- DICTIONARY OPERATIONS -----")
student = {
    'name': 'John',
    'age': 20,
    'course': 'CS'
}

# Common dictionary functions
student['age'] = 21                  # update value
student['college'] = 'XYZ College'  # add new key-value
age = student.get('age')            # get value
keys = list(student.keys())         # get all keys
values = list(student.values())     # get all values
items = list(student.items())       # get all items
removed = student.pop('course')     # remove key
is_present = 'name' in student      # key exists?

print("Student Dictionary:", student)
print("Age:", age)
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
print("Removed Item:", removed)
print("Is 'name' a key?:", is_present)


# -------------------- TUPLE --------------------
print("\n----- TUPLE OPERATIONS -----")
numbers = (10, 20, 30, 10, 40)

# Common tuple functions
count_10 = numbers.count(10)
index_30 = numbers.index(30)
length = len(numbers)

print("Tuple:", numbers)
print("Count of 10:", count_10)
print("Index of 30:", index_30)
print("Length of tuple:", length)


# -------------------- SET --------------------
print("\n----- SET OPERATIONS -----")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Common set functions
a.add(10)
a.remove(2)
union_set = a.union(b)
intersect_set = a.intersection(b)
diff_set = a.difference(b)
is_subset = {3, 4}.issubset(b)

print("Set A:", a)
print("Set B:", b)
print("Union:", union_set)
print("Intersection:", intersect_set)
print("Difference (A - B):", diff_set)
print("Is {3, 4} subset of B?:", is_subset)

'''
OUTPUT

----- LIST OPERATIONS -----
Fruits List: ['mango', 'grape', 'apple']
Popped Item: orange
Count of 'apple': 1
Length of list: 3

----- DICTIONARY OPERATIONS -----
Student Dictionary: {'name': 'John', 'age': 21, 'college': 'XYZ College'}
Age: 21
Keys: ['name', 'age', 'course', 'college']
Values: ['John', 21, 'CS', 'XYZ College']
Items: [('name', 'John'), ('age', 21), ('course', 'CS'), ('college', 'XYZ College')]      
Removed Item: CS
Is 'name' a key?: True

----- TUPLE OPERATIONS -----
Tuple: (10, 20, 30, 10, 40)
Count of 10: 2
Index of 30: 2
Length of tuple: 5

----- SET OPERATIONS -----
Set A: {1, 3, 4, 10}
Set B: {3, 4, 5, 6}
Union: {1, 3, 4, 5, 6, 10}
Intersection: {3, 4}
Difference (A - B): {1, 10}
Is {3, 4} subset of B?: True

'''