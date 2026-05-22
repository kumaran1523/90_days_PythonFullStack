'''
9. Sum of Squares
Sample Input
5
Sample Output
Sum of squares = 55
'''
n=int(input("Enter :"))
sum=0
for i in range(1,n+1):
    sum+=(i*i)
print(f"Sum of squares = {sum}")