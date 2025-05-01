"""The provided solution demonstrates a working implementation of this problem, where the main()
function guides the user through the process of entering two numbers
and displays their sum."""


def main():
    print("This program add to numbers.")
    num1:str = input("Enter the first number: ")
    num1:int = int(num1)
    num2:str = input("Enter the second number: ")
    num2:int = int(num2)
    total:int = num1 + num2
    print(f"Total number is {total}.")
    
    
if __name__ == "__main__":
    main()