class InvalidAgeError(Exception):
    pass


def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be 18.")
        else:
           print("Age is Valid")
    except InvalidAgeError as e:
        print("InvalidAgeError", e) 
        
        
check_age(16)
check_age(20)