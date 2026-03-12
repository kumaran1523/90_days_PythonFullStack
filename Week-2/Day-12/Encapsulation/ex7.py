# Add bonus marks using method.

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.__mark=mark
    def view_details(self):
        print(f"The name is : {self.name}")
        print(f"The mark is : {self.__mark}")
    def update_mark(self,m):
        self.__mark +=m

obj=Student("Kumar",50)
obj.view_details()
#Update mark 
obj.update_mark(20)
obj.view_details()