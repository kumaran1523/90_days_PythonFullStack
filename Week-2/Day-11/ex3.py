# Use constructor to initialize values

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

s=Student("Kumaran",78)
print(s.name)        
print(s.mark)        