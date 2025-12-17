# Create class Person with name and age

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name :",self.name)   
        print("Age :",self.age)   
    
p1=Person("Kumar",23)
p1.display()