# Demonstrate multiple inheritance using Father and Mother.

class Father:
    def __init__(self,f_name):
        self.f_name=f_name
    def meth1(self):
        print('I am a father class')
        print(f"The name is {self.f_name}")
class Mother:
    def __init__(self,m_name):
        self.m_name=m_name
    def meth2(self):
        print('I am a Mother class')
        print(f"The name is {self.m_name}")
    
class Child(Father,Mother):
    def __init__(self, f_name,m_name,c_name):
        super().__init__(f_name)
        Mother.__init__(self,m_name)
        self.c_name=c_name
    def meth3(self):
        self.meth1()
        self.meth2()
        print('I am a Child class')
        print(f"The name is {self.c_name}")

obj=Child('Sakthivel','Mohana','Kumar')
obj.meth3() 
    