# 8. Remove duplicates

limit=int(input("Enter a limit:"))

lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1}:"))
    lst.append(number)
    
unique_list=[]

for j in lst:
    if j not in unique_list:
        unique_list.append(j)
        
print("The original list is :",lst)
print("--------------------------------")
print("The Unique list is :",unique_list)
        
        