# 13. Simple calculator using if/elif
a=int(input("Enter value 1:"))
b=int(input("Enter value 2:"))
n=input("Enter Calculation:")
if(n=='add'):
    print(f"Addition {a+b}")
elif(n=='sub'):
    print(f"Subtraction {a-b}")
elif(n=='mul'):
    print(f"Multiplication {a*b}")
else:
    print(f"Division {a/b}")
