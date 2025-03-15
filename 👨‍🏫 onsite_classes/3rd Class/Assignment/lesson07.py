# Lesson 07: The Set & Frozenset
my_set: set = {123, 452,  5, 6}
my_set2: set = set([123, 452, 5, 6])
print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("my_set == my_set2 = ", my_set == my_set2)

print("\n________\n")

multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1,5,9,'hi') }
print(multi_type_set)

print("\n________\n")

set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)

print("\n________\n")

# Create a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_set[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print(e)  # Output: 'set' object does not support item assignment
    
print("\n________\n")

# Create a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_set[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print("*TypeError*  ABC : ", e)  # Output: 'set' object does not support item assignment

print("Program execution continues as normal because we handle the error condition in try except block")

print("\n________\n")

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print(my_set)
# Remove an item
my_set.remove(3)
my_set.remove('A')
print(my_set)  # Output: {1, 2, 4, 5}

my_set.add(6)
print(my_set)  # Output: {1, 2, 4, 5, 6}

print("\n________\n")

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_set = ", my_set)

# discard() only removes a single element.
# {1, 2, 3} is a set itself, not an element within my_set.
# Therefore, discard does not find it and returns None, without modifying the set.
print(my_set.discard({1,2,3}))

print("After: my_set = ", my_set) # return None

# To remove multiple elements, iterate and discard each one individually:
for item in {1, 2, 3}:
    my_set.discard(item)

print("After removing multiple elements: my_set = ", my_set)

print("\n________\n")

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("Before: my_set = ", my_set)
my_set.difference_update({1, 5, 3, 'A'})
print("After:  my_set = ", my_set)

print("\n________\n")

print("Before: ", my_set)
# Add multiple items
my_set.update([7, 8, 9, "Hello"])
print(my_set)  # Output: {4, 5, 6, 7, 8, 9}

print("\n________\n")
print("\n________\n")
print("\n________\n")
print("\n________\n")
print("\n________\n")
print("\n________\n")
print("\n________\n")
