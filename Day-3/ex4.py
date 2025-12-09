# 4. Find sum of numbers from 1–n

n=int(input("Enter a number:"))
sum=0

i=1
while(i<=n):
    sum+=i
    i+=1
print(f"Sum of first {n} value is:{sum}")