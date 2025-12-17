# Create method to calculate average

class Maths:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculate_avg(self):
        print("Name :",self.name)
        print('mark 1 :',self.mark1)
        print('mark 2 :',self.mark2)
        print('mark 3 :',self.mark3)
        Avg=(self.mark1+self.mark2+self.mark3)/3
        print("Average :",Avg)

m1=Maths("Kumar",56,56,56)
m2=Maths("Sayan",72,98,56)
m1.calculate_avg()
m2.calculate_avg()
