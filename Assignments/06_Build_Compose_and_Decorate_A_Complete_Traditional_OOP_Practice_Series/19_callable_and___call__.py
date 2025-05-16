class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, input):
        return input * self.factor
    
m1 = Multiplier(10)
print(m1.factor)

print(callable(Multiplier))

print(m1(2))

print(callable(m1))