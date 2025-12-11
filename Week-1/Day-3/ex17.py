# 17. Sum of odd numbers from 1–n
n=int(input("Enter a number:"))
sum=0

for i in range(1,n+1):
    if(i%2==1):
        sum+=i
print(f"The sum of first {n} odd number is {sum}")