'''
2. Palindrome Number

A number that remains the same when reversed.

Example: 121

Sample Input
121
Sample Output
121 is a Palindrome number
'''

n=int(input("Enter a value:"))
temp=n
res=0

while n>0:
    digit=n%10
    res=res*10+digit
    n//=10
if res==temp:
    print("Palindrome")
else:
    print("Not a palindrome")