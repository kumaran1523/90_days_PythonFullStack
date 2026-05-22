'''
8. Sum of N Natural Numbers
Sample Input
5
Sample Output
Sum of first 5 natural numbers is 15
'''

n=int(input("Enter :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of first {n} natural number is {sum}")