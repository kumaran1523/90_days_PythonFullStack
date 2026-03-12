# Protect data using encapsulation.

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def meth(self):
        print(self.__balance)

obj=Bank(500)
obj.meth()