import random

print("🎉Welcome to the number guessing game! 🎉\nYou have 10 attempts to guess the number between 50 and 100.\n\nLet's start the game! 🚀")

number_to_guess = random.randrange(50 , 100)

attempts:int = 10

guess_counter:int = 0

while guess_counter < attempts:
    guess_counter += 1
    my_guess = int(input("Enter Your Number Guess!"))
    
    if my_guess == number_to_guess:
        print(f"🎉 Yahooo! The number is {number_to_guess} you found it right!! in the {guess_counter} attempt 🎉")
        break
    elif guess_counter >= attempts and my_guess != number_to_guess:
        print(f"😢 Sorry! You've used all your attempts. The number was {number_to_guess}. Better luck next time! 😢")
        print("Game Over")
    elif my_guess > number_to_guess:
        print(f"Your guess is very high, try again! 🔼")
    elif my_guess < number_to_guess:
        print(f"Your guess is very low, try again! 🔽")
    