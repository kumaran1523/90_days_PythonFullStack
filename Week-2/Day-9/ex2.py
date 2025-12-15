# Handle invalid user input
try:
        
    a=int(input("Enter number 1 :"))
    b=int(input("Enter number 2 :"))
    print(a/b)
except ZeroDivisionError:
    print("Not divide my zero")
except ValueError:
    print("Enter integer value")