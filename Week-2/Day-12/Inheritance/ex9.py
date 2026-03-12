# Use super() to call parent constructor.

class parent:
    def __init__(self,name):
        self.name=name
    def meth(self):
        print("I am a parent class")
        print(self.name)
class child(parent):
    def __init__(self, name,name1):
        super().__init__(name)
        self.name1=name1
    def meth1(self):
        self.meth()
        print("I am a child class")
        print(self.name1)

obj=child("sakthi","Kumar")
obj.meth1()