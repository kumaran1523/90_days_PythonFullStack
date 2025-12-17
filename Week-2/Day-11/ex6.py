# Create class Student with marks and find pass/fail

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        if self.mark>40:
            print("Name :",self.name)
            print("Mark is :",self.mark)
            print("pass\n")       
        else:
            print("Name :",self.name)
            print("Mark is :",self.mark)
            print("fail\n")        
s1=Student("Kumaran",23)
s2=Student("Sanya",98)
s1.display()
s2.display()