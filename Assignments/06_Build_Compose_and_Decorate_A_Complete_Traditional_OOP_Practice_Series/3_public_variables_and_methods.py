class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(f"\nCar Brand {self.brand}")
        
car1 = Car("Toyota")
car1.start()
    