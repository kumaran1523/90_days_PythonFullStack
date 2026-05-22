'''
6. Find Largest of 3 Numbers
Sample Input
12
45
30
Sample Output
45 is the largest number
'''

a=int(input("Enter value 1 :"))
b=int(input("Enter value 2 :"))
c=int(input("Enter value 3 :"))

if a>b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")
    