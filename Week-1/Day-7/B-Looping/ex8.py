# Print Fibonacci series of N terms.
#0 1 1 2 3 5 8 13

n=int(input('Enter limit: '))

a=0
b=1
for i in range(n):
    if i==0:
        print (a,end=" ")
    elif i==1:
        print (b,end=" ")
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        

#Another method
print()
num=int(input("Enter limit:"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
