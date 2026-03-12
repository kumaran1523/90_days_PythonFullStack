# Override area() in Circle and Rectangle.

class Shape:
    def area(self):
        print('Area is not defined')
class Circle(Shape):
    def area(self):
        print("Area is 3.14 *r*r ")
class Rectangle(Shape):
    def area(self):
        print('Area is l * b')

c=Circle()
r=Rectangle()
c.area()
r.area()