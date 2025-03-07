# Class #2 Assignment #2 - Python operators

# 1. Arithmetic operators
x = 3
y = 2
print(f"Addition {x + y}")
print(f"Subtraction {x - y}")
print(f"Multiplication {x * y}")
print(f"Division {x / y}")
print(f"Modulus {x % y}")
print(f"Exponentiation {x ** y}")
print(f"Floor division {x // y}\n")


# 2. Assignment operators
x = 50
print(f"Assignment {x}")
x += 3
print(f"Addition Assignment {x}")
x -= 1
print(f"Subtraction Assignment {x}")
x *= 2
print(f"Multiplication Assignment {x}")
x /= 4
print(f"Division Assignment {x}")
x %= 2
print(f"Modulus Assignment {x}")
x //= 3
print(f"Floor division Assignment {x}")
x **= 5
print(f"Exponentiation Assignment {x}")

# Bitwise Operators Example
a = 20
b = 22

# Binary Representation
print(f"a in binary: {bin(a)}")
print(f"b in binary: {bin(b)}")

# Bitwise AND
print(f"AND: {a & b} -> {bin(a & b)}")

# Bitwise OR
print(f"OR: {a | b} -> {bin(a | b)}")

# Bitwise XOR
print(f"XOR: {a ^ b} -> {bin(a ^ b)}")

# Bitwise NOT
print(f"NOT: {~a} -> {bin(~a)}")

# Bitwise LEFT SHIFT
print(f"LEFT SHIFT: {a << 2} -> {bin(a << 2)}")

# Bitwise RIGHT SHIFT
print(f"RIGHT SHIFT: {a >> 1} -> {bin(a >> 1)}\n")


# Comparison operators
x = 3
y = 2
print(f"Equal '{x == y}'")
print(f"Not Equal '{x != y}'")
print(f"Greater than '{x > y}'")
print(f"Less than '{x < y}'")
print(f"Greater than or equal to '{x >= y}'")
print(f"Less than or equal to '{x <= y}'\n")

# Logical operators
print(f"AND '{5 > 3 and 5 > 10}'")
print(f"OR '{5 < 3 or 5 < 10}'")
print(f"NOT '{not 5 > 3}'\n")

# Identity operators
x = 5
y = 5
z = 10
print(f"IS '{x is y}'")  # True because thay are only one data stored in same memory location
print(f'ID: X {id(x)}') # Same ID X
print(f"ID: Y {id(y)}") # Same ID Y
print(f"ID: Z {id(z)}") # Different ID Z
print(f"IS NOT '{x is not z}'\n")

a = "Saud"
b = "Saud"
print(f"IS '{a is b}'") # True because thay are only one data stored in same memory location
print(f'ID: A {id(a)}') # Same ID A
print(f"ID: B {id(b)}\n") # Same ID B

l: list = [1, 2, 3]
t: list = [1, 2, 3]
print(f"IS '{l is t}'") # False because thay are multi data stored in different memory location like List, tuple, set, dictionary
print(f'ID: L {id(l)}') # Different ID L
print(f"ID: T {id(t)}") # Different ID T
print(f"IS NOT '{l is not t}'\n")

# Membership operators
x:list = [1,2,3,4,5]
b = 1 in x
print(f"IN '{b}'")
b = 10 in x
print(f"IN '{b}'\n")

admin_names:list = ["Asharib", "Saud", "Ali", "Ahmed"]

user:str = input("Enter your name: ")
if user in admin_names:
    print(f"Welcome {user}! You are admin\n")
else:
    print(f"You are not admin{user}\n")