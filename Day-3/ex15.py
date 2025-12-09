#  15. Print number triangle pattern

limit=int(input("Enter a limit:"))

for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(k,end=" ")
    print()



    