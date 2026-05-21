'''
12. Automorphic Number

A number whose square ends with the same number.

Example:
25² = 625

Sample Input
25
Sample Output
25 is an Automorphic number
'''

n=int(input("Enter: "))

n1=n*n
n2=str(n1)

if n2.endswith(str(n)):
    print("automorphic number")
else:
    print("Not automorphic number")
