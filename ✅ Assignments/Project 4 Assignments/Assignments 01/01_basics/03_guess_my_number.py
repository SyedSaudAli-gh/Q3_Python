# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def main():
    
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99... Enter a guess: ")
    
    user_guess = int(input("Guess the number: "))
    
    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        user_guess = int(input("Enter a guess: "))
        
    print(f"Congrats! The number was: {str(secret_number)}")
    
if __name__ == "__main__":
    main()
