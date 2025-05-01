# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    
    phonebook = {}
    
    while True:
        name = input("Enter name: ")

        if name == "":
            break
        number = input("Enter number: ")
        
        phonebook[name] = number
        
    return phonebook

def print_phonebook(phonebook):
    
    for name in phonebook:
        print("\n" + str(name) + "->" + str(phonebook[name] + "\n"))
        
        
def lookup_number(phonebook):
    
    while True:
        name = input("Enter name to lookup: ")
        
        if name == "":
            break
        
        if name not in phonebook:
            print(name + " not found.")
        else:
            print("\n" + str(name) + "->" + str(phonebook[name] + "\n"))
            
def main():
    
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_number(phonebook)
    
if __name__ == "__main__":
    main()
