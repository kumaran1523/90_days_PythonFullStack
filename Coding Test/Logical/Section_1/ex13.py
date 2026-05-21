'''
13. Neon Number

Sum of digits of square equals the number.

Example:
9² = 81 → 8 + 1 = 9

Sample Input
9
Sample Output
9 is a Neon number
'''

n=int(input("Enter :"))

square=n*n
sum=0
while square!=0:
    digit=square%10
    sum+=digit
    square//=10
if sum==n:
    print(f"{n} is a neon number")
else:
    print(f"{n} is not a neon number")
