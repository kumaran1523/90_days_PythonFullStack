# Try accessing private variable directly (observe error).

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def meth(self):
        print(self.__balance)

obj=Bank(500)
# obj.__balance  # AttributeError: 'Bank' object has no attribute '__balance'

obj.meth()