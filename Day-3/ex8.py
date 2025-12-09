# 8. Check if a number is palindrome

number=int(input("Enter a number:"))
num_copy=number
reverse=0

while(number>0):
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if(reverse==num_copy):
    print(f"The given number {num_copy} is PALINDROME")
else:    
    print(f"The given number {num_copy} is not PALINDROME")
    
