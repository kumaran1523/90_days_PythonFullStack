# 9. Print Fibonacci series (n terms)
# 0 1 1 2 3 5 8 13

number=int(input("Enter number of values:"))
a=0
b=1
for i in range(1,number+1):
    print(a,end=" ")
    a,b=b,a+b
    