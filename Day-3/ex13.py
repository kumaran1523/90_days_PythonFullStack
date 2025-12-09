# 13. Print star triangle pattern

limit=int(input("Enter a limit:"))

for i in range(1,limit+1):
    space=" "*(limit-i)
    star="* " * i
    print(space + star)
print("-----------------------")
for j in range(1,limit+1):
    print(" "*(limit-j)+"*"*(2*j-1))