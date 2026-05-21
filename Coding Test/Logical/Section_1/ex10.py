'''
10. Strong Number

Sum of factorial of digits equals the number.

Example:
145 → 1!+4!+5!=145

Sample Input
145
Sample Output
145 is a Strong number
'''

n=int(input("Enter a number :"))
temp=n
sum=0


while n!=0:
    digit=n%10
    res=1
    for i in range(1,digit+1):
        res*=i
    sum+=res
    n//=10
if sum==temp:
    print("Strong number")
else:
    print("Not a strong number")
