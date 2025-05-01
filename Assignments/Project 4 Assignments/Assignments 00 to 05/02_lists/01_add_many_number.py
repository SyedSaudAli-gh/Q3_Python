# Write a function that takes a list of numbers and returns the sum of those numbers.



# def add_many_number(numbers):
#     """
#     This function takes a list of numbers and returns the sum of those numbers.
#     """
#     total = 0
    
#     for number in numbers:
#         total += number
#     return total

# sum_of_numbers = add_many_number([1, 2, 3, 4, 5, 6])

# print(f"The sum of the numbers is {sum_of_numbers}")





def add_many_number(numbers) -> int:
    
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    
    sum_of_numbers = add_many_number(numbers)
    
    print(f"The sum of the numbers is {sum_of_numbers}")
    
if __name__ == "__main__":
    main()
