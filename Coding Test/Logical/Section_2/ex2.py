'''
2. LCM

Least Common Multiple of two numbers.

Sample Input
12
18
Sample Output
LCM of 12 and 18 is 36
'''

a=int(input("Enter input 1 :"))
b=int(input("Enter input 2 :"))

x=a
y=b

while y!=0:
    x,y=y,x%y
gcd=x

lcm=(a*b)//gcd
print(f"LCM of {a} and {b} is {lcm} ")