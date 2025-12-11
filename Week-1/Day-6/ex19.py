# 19. Recursive function to print Fibonacci series.

# 0 1 1 2 3 5 8

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(10))

print("-----------------------------")  

for i in range(11):
    print(fibo(i),end=" ")