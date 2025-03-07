# Data Types For Python
# mutable object can change its state or contents and immutable objects cannot.

#  Mutable Data Types:
# • List
# • Dictionary
# • byte array

# Immutable Data Types:
# • Int
# • Float
# • Complex
# • String
# • Tuple
# • set


# • Integers
# • Float
# • Complex numbers

# • Integers
a = 5 
print(a, 'is of type' , type(a))

# • Float
a = 2.2 
print(a, 'is of type' , type(a))
 
# • Complex numbers
a = 1 + 2j
print(a, 'is of type' , type(a))


# • A string is a collection of one or more characters put in a single quote, double-quote or triple quote
# • Multi-line strings can be denoted using triple quotes, ''or "''

# • String
s = 'Hello World 1'
print(s, 'is of type' , type(s))

s = "Hello World 2"
print(s, 'is of type' , type(s))

s = """
    Hello 
    World
    3
    """
print(s, 'is of type' , type(s))

# • Tuple is an ordered sequence of items same as a list.
# • It is defined within parentheses () where items are separated by commas.

# Tuple
print("############# T u p l e #############")
t = (20 , 1 , "syed" , "ali")
print(t, type(t))


t = (20 , 1 , "syed" , "ali")
# t[3] = "Khan"  #Error
print(t, type(t))


# •A set is an unordered collection of items.
# •Every set element is unique (no duplicates) and must be immutable (cannot be changed)
print("############# Set #############")
s = {1,2,5,1,3,4}
print(s, type(s))

# • List is an ordered sequence of items.
# • It is one of the most used datatype in Python and is very flexible. []
print("############# L i s t #############")
l = [20 , 1 , "syed" , "ali"]
print(l , type(l))

# # Mutable
l = [20 , 1 , "syed" , "ali"]
l[1] = 99
l[2] = "saud"
print(l , type(l))


# • Dictionary is an unordered collection of key-value pairs.
# • In Python, dictionaries are defined within braces f} with each item being a pair in the form key:value
print("############# D i c t i o n a r y #############")

d = {
    "name" : "Python",
    "dob": "20 February 1991",
    "f_name" : "Guido van Rossum"
}

print(d , type(d))
print(d["name"])
print(d["dob"])
print(d["f_name"])


dUpdate = {
    "name": "Python",
    "dob": "20 February 1991",
    "f_name": "Guido van Rossum"
}

# Update values
dUpdate["name"] = "TypeScript"

# Add new key-value
dUpdate["creator"] = "Anders Hejlsberg"

print(dUpdate)
