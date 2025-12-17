# Create class Employee with salary

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        print()
e1=Employee("Kumar",20000)
e2=Employee("Saroo",50000)
e3=Employee("Sanya",90000)
e1.display()
e2.display()
e3.display()
