# # List
# fruits:list = ["Apple","Banana","Cherrys"]
# number:list = [10,2,39,9,4,9,0,1]
# mixed:list = ["hello", 42, 3.14, True]
# print("fruits  = ", fruits)
# print("number = ", number)
# print("mixed   = ", mixed)

# # Accessing List Elements
# fruits: list = ["apple", "banana", "cherry"]
# print(fruits[0])   #apple
# print(fruits[-2])  #banana

# # Modifying Lists
# fruits:list = ["mango", "banana", "apple"]
# print(f"Orignal Fruits{fruits}")
# fruits[-3] = "Cherry"
# print(f"Modifion Fruits{fruits}")

# # List Slicing
# slice_fruits = fruits[0:2]
# print(slice_fruits)

# # Common List Methods
# fruits.append("Watermelon")
# print(fruits)

# # Extends
# fruits.extend(["GRAPE", "KIWI"])
# print(fruits)

# # Removing Elements
# fruits.remove("apple")
# print(fruits)

# # Pop Method
# deleted = fruits.pop(1)
# print(f'Delete item {deleted}')
# print(fruits)

# # Sorting a List
# number:list = [1,9,9.1,1,2,3,6,9,8,4,10,15,10,6,8]
# number.sort()
# print(number)

# # Reverseing
# number.reverse()
# print(number)

# # Loop
# for fruit in fruits:
#     print(fruit)
    
    
# # Tuples
# tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
# tuple2: tuple = (10, 20, 30) # tuple
# mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple

# print("tuple1      =", tuple1)
# print("tuple2      =", tuple2)
# print("mixed_tuple =", mixed_tuple)


# tuple_1: tuple = (10, 20, 30) # tuple
# tuple_2: tuple = (10, 20, 30) # tuple

# print("id(tuple_1) = ", id(tuple_1)) # unique memory address
# print("id(tuple_2) = ", id(tuple_2)) # unique memory address

# print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2) # comparing by value


tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)


# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])  # Accessing first element

# Tuple slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# Tuple Length
print("Length of tuple1:", len(tuple1))

# Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
  print(item)
  
# Checking if an item exists in a tuple
print("Is 20 in tuple2?", 20 in tuple2)

# Concatenating tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# Nested tuples
nested_tuple: tuple = (tuple1 , tuple2)
print("nested_tuple =", nested_tuple)

# Unpacking tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2:"Another tuple key"}
print("Dictionary with tuple keys:",  my_dict)

print(tuple1[0])   # Output: apple
print(tuple1[-3])  # Output: apple
print(tuple1.count("apple"))
print(tuple1.index("apple"))


# prompt: print the complete list of methods and attribute of tuple, dont include dunders

# Get a list of all attributes and methods of a tuple
tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]

# Print the list of methods (excluding dunder methods)
tuple_methods

# prompt: generate a example of ['count', 'index'] in tuple

tuple1: tuple = tuple(["apple", "banana", "cherry"])
print(tuple1.count("apple"))  # Output: 1
print(tuple1.index("apple"))  # Output: 0
example_tuple: tuple = ('count', 'index')
print(example_tuple) # Output: ('count', 'index')

# Creating a Dictionary

# prompt: genrate a List of 5 american cities
american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(american_cities ,type(american_cities))

# Create a dictionary to store a person's details
person: dict = {
    "name" : "Saud Ali",
    "age": 30,
    "visited_cities": american_cities
}
print(person)

thisdict: dict = dict(name = "John", age = 36, country = "Norway") # It is also possible to use the dict() constructor to make a dictionary.
print(type(thisdict)," - ", thisdict, )

print(person["name"])
print(person.get("age" , "99"))

# Access a non-existent key
print(person.get("country", "my_default_vlaue_if_key_not_found"))  # Output: my_default_vlaue (default value)


person["email"] = "saud.saleem93@gmail.com"
print(person)
person["age"] = 31
print(person)

print("\n-----\n")

person: dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
print(person)

# Remove a key-value pair using del
del person["city"]
print(person)

# Remove a key-value pair using pop
age:int = person.pop("age" , -1)
print(f"Removed age: {age}")
print(person)

age: int = person.pop("age", -1)
print("key 'age' not found in dict so returning default value: ", age)

# Duplicate Key Not Allowed
thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
print(thisdict)

for key in thisdict:
    print(key)
    
for key, value in thisdict.items():
    print(key, ":", value)
    
    
    
# Create a phonebook
phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new contact
phonebook["David"] = "111-222-3333"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")