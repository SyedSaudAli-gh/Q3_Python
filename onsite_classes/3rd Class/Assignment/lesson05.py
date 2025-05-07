# # The if Statement
# num = 10
# if num > 0:
#     print("The number is positive.") 
    
# # The else Statement
# num = 3
# if num > 0:
#     print("The number is positive")
# else:
#     print("The number is not positive.")
    
# # The elif Statement
# num = -1

# if num > 0 :
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
    
# # Nested if Statements
# num = 20

# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive and odd.")
# else:
#    print("The number is negative.")
   
# # Practical Examples
# num1: float = float(input("Enter the first number: "))
# num2: float = float(input("Enter the second number: "))
# selecte_operation: str = input("Enter the operation (+, -, *, /): ")

# if selecte_operation == "+":
#     result = num1 + num2
# elif selecte_operation == "-":
#      result = num1 - num2
# elif selecte_operation == "*":
#      result = num1 * num2
# elif selecte_operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero."
# else:
#     result = "Invalid operation."
    
# print(result)

# # build a calculator which takes input from the user, beside basic functionality include modulus, floor division, Exponentiation
# def calculator():
#   """
#   A calculator function that takes user input for numbers and operations,
#   including modulus, floor division, and exponentiation.
#   """
#   while True:
#     operation = input("Enter the operation (+, -, *, /, %, //, ** or 'q' to quit): ")
#     if operation.lower() == 'q':
#       break
#     if operation not in ('+', '-', '*', '/', '%', '//', '**'):
#       print("Invalid operation.")
#       continue

#     try:
#       num1 = float(input("Enter the first number: "))
#       num2 = float(input("Enter the second number: "))
#     except ValueError:
#       print("Invalid input. Please enter numbers only.")
#       continue

#     if operation == '+':
#       result = num1 + num2
#     elif operation == '-':
#       result = num1 - num2
#     elif operation == '*':
#       result = num1 * num2
#     elif operation == '/':
#       if num2 != 0:
#         result = num1 / num2
#       else:
#         result = "Error: Division by zero."
#         print(result)
#         continue
#     elif operation == '%':
#       result = num1 % num2
#     elif operation == '//':
#       if num2 != 0:
#         result = num1 // num2
#       else:
#         result = "Error: Division by zero."
#         print(result)
#         continue
#     elif operation == '**':
#       result = num1 ** num2

#     print("Result:", result)

# calculator()

# # generate a grading system for school which takes marks as an  input show grade according to the marks

# def grading_system(marks):
    
#     if marks >= 90:
#         grade = "A+"
#     elif marks >= 80:
#         grade = "A"
#     elif marks >= 70:
#         grade = "B"
#     elif marks >= 60:
#         grade = "C"
#     elif marks >= 50:
#         grade = "D"
#     else:
#         grade = "F"
#     return grade

# # Get marks as input from the user
# while True:
#   try:
#     marks = float(input("Enter the marks: "))
#     if 0 <= marks <= 100:
#       break
#     else:
#       print("Marks must be between 0 and 100.")
#   except ValueError:
#     print("Invalid input. Please enter a number.")

# # Determine the grade
# grade = grading_system(marks)

# # Print the grade
# print(f"The grade for {marks} marks is: {grade}")

# **Tutorial: Loops and Iteration in Python**

fruits = ["apple", "banana" , "orange"]
for fruit in fruits:
    print(fruit)
    
    
word = "PYTHON"
for letter in word:
    print(letter)
    

for i in range(5):
    print(i)
    
for i in range(2,22,2):
    print(i)
    
for _ in range(10):
    print(f"Hello {_}")
    
# The while Loop
count = 1
while count <= 5:
    print(count)
    count += 1
    
    
# Controlling Loops
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)
    
    
# Nested Loops
for outer in range(2,6):
    print(f'Multiplication Table {outer}')
    for inner in range(2, 6):
        print(f"{outer} x {inner} = {outer * inner}")
        
        
total = 0
for i in range(1 , 101):
    total += i
print("Sum of numbers from 1 to 100:", total)

num = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num} : {factors}")