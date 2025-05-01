# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

num_sides: int = 6


def main():
    
    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    
    total: int = die1 + die2
    
    print(f"Dice have {num_sides} sides each.")
    print(f"Rolling die1... {die1}")
    print(f"Rolling die2... {die2}")
    print(f"Total of two dice {total}")
    
    

if __name__ == "__main__":
    main()

