"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""

def main():
    
    num1: int = int(input("Type a number to see its square: "))
    square: int = num1 ** 2
    print(f"{num1} squared is {square}")

if __name__ == "__main__":
    main()

