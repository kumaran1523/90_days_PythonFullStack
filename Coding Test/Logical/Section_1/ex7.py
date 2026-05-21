'''
7. Reverse a Number
Sample Input
1234
Sample Output
4321
'''

n=int(input("Enter : "))
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)