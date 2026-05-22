'''
1. GCD (HCF)

Greatest Common Divisor of two numbers.

Sample Input
12
18
Sample Output
GCD of 12 and 18 is 6
'''

a=int(input("Enter input 1 :"))
b=int(input("Enter input 2 :"))

while b != 0:
    a, b = b, a % b

print("GCD is", a)
    