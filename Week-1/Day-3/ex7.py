# 7. Reverse a number

number=int(input("Enter a number:"))
num=number
reverse=0

while(number>0):
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
print(f"Reverse number of {num} is {reverse}")