# Create multiple objects

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print()
s1=Student("Kumar",23)
s2=Student("Saroo",22)
s3=Student("Sanya",5)
s4=Student("Sayan",3)
s1.display()
s2.display()
s3.display()
s4.display()