# 14. Print inverted triangle

limit=int(input("Enter a limit:"))
for i in range(limit,0,-1):
    print(" "*(limit-i)+"*"*(2*i-1))