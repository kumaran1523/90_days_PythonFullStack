'''
4. Print First N Prime Numbers

Sample Input
5
Sample Output
2 3 5 7 11
'''

n=int(input("Enter :"))

for i in range(2,n):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
                
        
