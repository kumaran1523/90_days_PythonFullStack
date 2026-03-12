# Create an object of Student and call both methods.

class Person:
    def role(self):
        print('I am a person')
class Student(Person):
    def show_role(self):
        self.role()
        print("I am a student")

obj=Student()
obj.role()
obj.show_role()
 