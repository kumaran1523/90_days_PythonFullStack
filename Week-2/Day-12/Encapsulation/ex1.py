# Create a class Bank with private variable __balance.

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def check_bal(self):
        print(f'Balance is :{self.__balance}') 
obj=Bank(400)
obj.check_bal()