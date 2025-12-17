'''
🔵 Mini Task

Bank Account Class

•	account number
•	balance
•	deposit()
•	withdraw()
•	show_balance()
'''

class BankAccount:
    def __init__(self,acc_no,balance=0):
        self.acc_no=acc_no
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"{amount} deposited successfully")
        else:
            print("Enter valid amount")
    
    def withdraw(self,amount):
        if amount<0:
            print("Enter valid amount")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -=amount
            print("Amount withdraw successfully")
    
    def show_balance(self):
        print(f"Your balance is {self.balance}")

try:           
    account_number=int(input('Enter Account number :'))
except ValueError:
    print("Enter valid account number in digit")

user=BankAccount(account_number,0)

while True:
    print("*******************Bank Account Class*****************\n")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Show balance")
    print("4.Exit")
    print()
    try:
        choice=int(input("Enter your choice :"))
    except ValueError:
        print("Enter integer value")
    
    match choice:
        case 1:
            print('Deposite')
            amt=float(input("Enter a deposited amount :"))
            user.deposit(amt)
        case 2:
            print('Withdrawal')
            amt=float(input('Enter a withdrawl amount :'))
            user.withdraw(amt)
        case 3:
            print('Balance')
            user.show_balance()
        case 4:
            print('Exit')
            print("Exiting the account Goodbye!...")
            break
        case _:
            print('Enter valid input')