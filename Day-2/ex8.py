#  8. Accept two numbers and find the greatest

number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))

if(number1>number2):
    print(f"{number1} is greater")
elif(number2>number1):
    print(f"{number2} is greater")
else:
    print("Both are equal")