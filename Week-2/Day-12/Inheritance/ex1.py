# Create a parent class Person with method show_name()

class parent:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(f"The name is {self.name}")
obj=parent("kumar")
obj.show_name()