# Create method to display details

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    
    def display_detail(self):
        print("Name is :",self.name)
        print("Mark is :",self.mark)

s=Student("Kumaran",89)
s.display_detail()
        