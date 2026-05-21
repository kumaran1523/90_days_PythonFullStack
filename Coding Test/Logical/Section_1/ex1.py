'''
1. Armstrong Number

A number is an Armstrong number if the sum of its digits raised to the power of number of digits equals the number itself.

Example:
153 → 1^3+5^3+3^3=153

Sample Input
153
Sample Output
153 is an Armstrong number
'''

n=int(input("Enter :"))
temp=n
n1=len(str(n))
# print(n1)
res=0
while n!=0:
    digit=n%10
    res+=digit**n1
    n//=10
if res==temp:
    print("Armstrong number")
else:
    print("Not an armstrong number")