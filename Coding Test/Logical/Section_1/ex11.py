'''
11. Perfect Number

Sum of proper divisors equals the number.

Example:
6 → 1 + 2 + 3 = 6

Sample Input
6
Sample Output
6 is a Perfect number

'''

n=int(input("Enter : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print("perfect number")
else:
    print("Not a perfect number")