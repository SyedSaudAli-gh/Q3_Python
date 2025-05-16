class Counter:
    count = 0
    
    def __init__(self):
       Counter.count += 1
       
    @classmethod
    def display(cls):
        print(f"Total Object Create: {cls.count}")
        
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display()