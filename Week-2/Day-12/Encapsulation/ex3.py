# Prevent direct access to __balance.

class Bank:
    def __init__(self):
        self.__balance=1000
    def balance_check(self):
        print(f"balance is :{self.__balance}")
obj=Bank()
obj.balance_check()