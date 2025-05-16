class Department:
    def __init__(self,  name):
        self.name = name

class Employee:
    def __init__(self, id, name,  department):
        self.id = id
        self.name = name
        self.department = department
        
dep = Department("Software Department")
emp = Employee( 985110 , "Saud" , dep )

print(f"Employee ID: {emp.id}")
print(f"Employee Name: {emp.name}")
print(f"Department Name: {emp.department.name}")
