'''
3. Prime Number

A number greater than 1 having only 2 factors: 1 and itself.

Sample Input
13

Sample Output
13 is a Prime number
'''

n=int(input("Enter :"))

if n>1:
    for i in range(2,n):
        if n%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is Prime number")
else:
    print("Enter valid number")