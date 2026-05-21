'''
8. Sum of Digits
Sample Input
1234
Sample Output
Sum of digits = 10
'''

n=int(input("Enter : "))
sum=0

while n!=0:
    digit=n%10
    sum+=digit
    n//=10
print("Sum of digits =",sum)