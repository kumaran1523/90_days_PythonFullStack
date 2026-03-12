
from abc import ABC,abstractmethod

class Bank(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def details(self):
        print(f"The name is {self.name}")   
        print(f"The balance is {self.__balance}")   
    def accountType(self):
        pass
  
    def deposite(self,amount):
        self.__balance+=amount
        print(f"{amount} rupees  deposited successfully")
    def withdraw(self,amount):
        if(amount > self.__balance):
            print(f"Insufficient balance,your balance is :{self.__balance}") 
        else:
            self.__balance-=amount
            print(f"{amount} rupees Withdrawal successful and the current balance is {self.__balance}")
class savingAccount(Bank):
    def accountType(self):
        print( "This is Savings Account")
class currentAccount(Bank):
    def accountType(self):
        print('This is current Account')


# creating object

s=savingAccount("Kumar",4000)
c=currentAccount('Sakthi',10000)

s.details()
s.deposite(200)
# c.deposite(500)

s.withdraw(3800)
# c.withdraw(4060)

