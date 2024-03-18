#class is used to create object
class Employee:
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
    def getsalary(self): 
       return self.salary
   
sachin = Employee("sachin","3333")
print(sachin.salary)
print(sachin.name)
sachin = Employee("hRRY","5555555555555555555")
print(sachin.salary)
print(sachin.name)
