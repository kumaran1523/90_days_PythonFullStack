'''
5. Fibonacci Series

Each number is the sum of previous two numbers.

Sample Input
7
Sample Output
0 1 1 2 3 5 8
'''

n=int(input("Enter :"))
a,b=0,1
if n>1:
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
    