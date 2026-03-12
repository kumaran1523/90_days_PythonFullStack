# Create Employee class with private salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def display_details(self):
        print(f"The name is {self.name}")        
        print(f"The Salary is {self.__salary}")       

emp=Employee("Kumar",30000)
emp.display_details()