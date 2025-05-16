def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls
    
@add_greeting
class Person:
    def __init__(self):
        print("Person")
        
        
p1 = Person()
print(p1.greet())
