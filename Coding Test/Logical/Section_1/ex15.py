'''
15. Spy Number

Sum of digits equals product of digits.

Example:
123 → Sum = 6, Product = 6

Sample Input
123
Sample Output
123 is a Spy number
'''

n=int(input("enter :"))
temp=n
sum=0
product=1

while n!=0:
    digit=n%10
    sum+=digit
    product*=digit
    n//=10
if sum==product:
    print(f"{temp} is a spy number")
else:
    print(f"{temp} is not a spy number")

