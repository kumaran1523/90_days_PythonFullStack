'''
10. Check if Number is Power of 2
Sample Input
16
Sample Output
16 is a Power of 2
'''
n=int(input("Enter :"))

temp=n

while temp%2==0:
    temp=temp//2

if temp==1:
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2")