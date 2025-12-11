# Count digits in a number.

num=int(input("Enter a number:"))

count=0
while num>0:
    digit=num%10
    count+=1
    num=num//10

print("Count is:",count)