class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
        
    def start(self):
        print(f"Engine with {self.horse_power}cc is starting.")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine
        
    def start_car(self):
        print(f"Starting Car: {self.model}")
        self.engine.start()
    
    
e1 = Engine(1500)


car1 = Car( "Civic", e1)
car1.start_car()