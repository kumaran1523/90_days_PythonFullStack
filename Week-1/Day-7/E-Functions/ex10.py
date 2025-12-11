# Recursive function to print Fibonacci series.

#0 1 1 2 3 5 8 13 21 34

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
limit=int(input("Enter limit :"))

for i in range(limit):
    print(fibo(i),end=" ")