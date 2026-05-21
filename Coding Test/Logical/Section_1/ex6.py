'''
6. Factorial (Iterative + Recursive)

Factorial of n = n × (n-1) × ... × 1

Sample Input
5
Sample Output
Factorial of 5 is 120
'''

n=int(input("Enter :"))
res=1
for i in range(1,n+1):
    res*=i
print(res)