class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"The dog's name: {self.name} and Breed: {self.breed}")
        
d1 = Dog("Tommy", "American Bully")
d1.bark()