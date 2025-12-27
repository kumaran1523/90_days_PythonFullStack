# Print employee bonus

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        bns=self.salary*0.20
        print("Bonus :",bns)
        print()
        
e1=Employee("Kumar",20000)
e2=Employee("Dev",500000)
e3=Employee("Sanya",90000)
e1.display()
e2.display()
e3.display()
