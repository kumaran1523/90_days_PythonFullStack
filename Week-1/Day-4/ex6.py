# 6. Print odd numbers only

limit=int(input("Enter a limit:"))
lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1}: "))
    lst.append(number)
    
odd_number=[]

for j in lst:
    if j%2==1:
        odd_number.append(j)

print(f"The odd numbers of{lst} is :",*odd_number)
