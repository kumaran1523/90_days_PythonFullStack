'''
14. Harshad (Niven) Number

A number divisible by sum of its digits.

Example:
18 → 1 + 8 = 9 → 18 % 9 = 0

Sample Input
18
Sample Output
18 is a Harshad number
'''

n=int(input("Enter :"))
temp=n
sum=0
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
if temp%sum==0:
    print(f"{temp} is a harshad number")
else:
    print(f"{temp} is not a harshad number")
    