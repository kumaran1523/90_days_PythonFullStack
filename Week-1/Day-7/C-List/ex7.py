# Remove duplicates from list.

lst=[2,5,6,9,6,6,5,2,2,3,9]
print("List is :",lst)
unique=[]
for i in lst:
    if i not in unique:
        unique.append(i)
    
print("Unique list is :",unique)
    