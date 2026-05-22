'''
4. Check Even/Odd Without %

Using bitwise operator.

Sample Input
14
Sample Output
14 is an Even number
'''

a=int(input("Enter a :"))

if a&1==0:
    print("Even")
else:
    print("Odd")
