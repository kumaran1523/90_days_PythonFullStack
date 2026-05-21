'''
9. Count Digits
Sample Input
98765
Sample Output
Number of digits = 5
'''

n=int(input("Enter : "))
cnt=0
while n!=0:
    digit=n%10
    cnt+=1
    n//=10
print("Number of digits=",cnt)