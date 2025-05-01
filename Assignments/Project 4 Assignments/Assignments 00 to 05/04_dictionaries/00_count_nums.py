# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def get_user_numbers():
    
    user_numbers = []
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
        
        number = int(user_input)
    
        user_numbers.append(number)
    
    return user_numbers
    
def count_nums(num_1st):
    
    num_dict = {}
    
    for num in num_1st:
        
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
            
    return num_dict

def print_counts(num_dict):
   
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")
        
def main():
    
    user_numbers = get_user_numbers()
    
    num_dict = count_nums(user_numbers)
    
    print_counts(num_dict)
    
if __name__ == "__main__":
    main()
