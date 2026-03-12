# Demonstrate multilevel inheritance using A → B → C.

class A:
    def __init__(self,a):
        self.a=a
    def meth1(self):
        print('This is class A') 
        print(f"The value of a is :{self.a}")
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def meth2(self):
        self.meth1()
        print('This is class B') 
        print(f"The value of b is :{self.b}")
        
class C(B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def meth3(self):
        self.meth2()
        print('This is class C') 
        print(f"The value of c is :{self.c}")

obj=C(100,200,300)
obj.meth3()