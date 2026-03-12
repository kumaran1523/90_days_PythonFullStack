# Create a setter method to update balance.

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amt):
        self.__balance=amt
obj=Bank(1000)
print(obj.get_balance())
obj.set_balance(5000)
print(obj.get_balance())

        