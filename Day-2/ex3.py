# 3. Find the largest of 3 numbers

number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))
number3=int(input("Enter number 3:"))

if(number1>number2 and number1>number3):
    print(f"{number1} is greater")
elif(number2>number1 and number2>number3):
    print(f"{number2} is greater")
else:
    print(f"{number3} is greater")

