# 24. Convert list → set to remove duplicates.

limit=int(input("Enter a limit:"))
lst=[]

for i in range(limit):
    num=int(input(f"Enter a lst {i+1} :"))
    lst.append(num)
    
print("The list are: ",lst)

remove_duplicate=set(lst)

print('The list without duplicate is :',remove_duplicate)