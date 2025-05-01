"""Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end.
The autograder is sensitive to capitalization and punctuation, be careful! Your solution should 
look like this (the below numbers are made up -- your solution should have the correct values!):"""


anton:int = 21
beth:int = anton + 6
chen:int = beth + 20
drew:int = chen + anton
ethan:int = chen

print(f"Anton is {anton} years old.") # Anton is 21 years old.
print(f"Beth is {beth} years old.") # Beth is 27 years old.
print(f"Chen is {chen} years old.") # Chen is 47 years old.
print(f"Drew is {drew} years old.") # Drew is 68 years old.
print(f"Ethan is {ethan} years old.") # Ethan is 47 years old.


