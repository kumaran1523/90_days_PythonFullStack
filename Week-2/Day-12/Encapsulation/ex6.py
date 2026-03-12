# Create Student class with private marks.

class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.__mark1=mark1
        self.__mark2=mark2
        self.__mark3=mark3
    def view_details(self):
        print(f"The name is {self.name}")
        print(f"The mark 1 is {self.__mark1}")
        print(f"The mark 2 is {self.__mark2}")
        print(f"The mark 3 is {self.__mark3}")
obj=student("Kumar",56,45,89)
obj.view_details()
    
        
        