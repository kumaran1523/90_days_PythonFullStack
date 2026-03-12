# Create a getter method to show balance.

class Bank:
    def __init__(self):
        self.__balance=1000
    def get_balace(self):
        return self.__balance
obj=Bank()
print(obj.get_balace())