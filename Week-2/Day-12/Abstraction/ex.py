 # Create abstract class Shape.Implement area() in Circle.	Implement area() in Rectangle.
 
from abc import ABC,abstractmethod
 
class Shape(ABC):
     @abstractmethod
     def area(self):
         pass
class Circle(Shape):
    def area(self):
        return "Area is 3.14 * r * r "
class Rectangle(Shape):
    def area(self):
        return "Area is l * b "
    
c=Circle()
# print(c.area())

r=Rectangle()
# print(r.area())
    
obj=(c,r)

for i in obj:
    print(i.area())