# 13. Get common elements between 2 lists

limit1=int(input('Enter the limit of list 1:'))
lst1=[]

for i in range(limit1):
    number1=int(input(f"Enter a number {i+1} : "))
    lst1.append(number1)

print(lst1)

limit2=int(input("Enter the limit of list 2:"))
lst2=[]

for j in range(limit2):
    number2=int(input(f"Enter a number {i+1} : "))
    lst2.append(number2)
    
print(lst2)

common=[]

for k in lst1:
    if k in lst2 and k not in common:
        common.append(k)

print(f"The common element between {lst1} and {lst2} is:",*common) 