# Create methods deposit() and withdraw().

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def check_balance(self):
        print(f'Balance is : {self.__balance}')
    def deposite(self,amt):
        self.__balance+=amt
        print(f"Balance After deposite is: {self.__balance} ")
    def withdraw(self,amt):
        if amt<=self.__balance:
            self.__balance -=amt
            print(f"Balance After withdraw is: {self.__balance} ")
        else:
            print("Insufficient balance")

obj=Bank(1000)
obj.check_balance()
obj.deposite(200)
obj.withdraw(500)

            
        