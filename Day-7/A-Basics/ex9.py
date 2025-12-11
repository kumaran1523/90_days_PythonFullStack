# 9.	Accept 3 numbers and print the largest.

a=int(input('Enter a :'))
b=int(input('Enter b :'))
c=int(input('Enter c :'))

if a>b and a>c:
    print(f"{a} is greatest")
elif b>a and b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
