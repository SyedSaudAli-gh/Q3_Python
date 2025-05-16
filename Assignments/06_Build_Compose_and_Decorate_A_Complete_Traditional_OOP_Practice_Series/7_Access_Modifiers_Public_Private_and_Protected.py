class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
        
e1 = Employee("Saud", "35k", 21221021)
print(f"Public -> {e1.name}")
print(f"Protected -> {e1._salary}")
print(f"Private -> {e1.__ssn}")