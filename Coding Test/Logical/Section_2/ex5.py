'''
5. Swap Two Numbers (Without Temp Variable)
Sample Input
10
20
Sample Output
After swapping:
a = 20
b = 10
'''

a=int(input("Enter a :"))
b=int(input("Enter b :"))

a=a+b
b=a-b
a=a-b

print(f"a = {a}")
print(f"b = {b}")

