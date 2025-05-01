# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


INCHES_PER_FOOT: int = 12 # Constant for the number of inches per foot

def main():
    feet: float = float(input("Enter a number of feet: "))
    
    inches: float = feet * INCHES_PER_FOOT
    
    print(f"{feet} feet is {inches} inches")
    
    
if __name__ == "__main__":
    main()
