	# Get common elements between 2 lists.
 
lst1=[7,5,6,7,8,4]
lst2=[1,2,3,4,5]

common=[]

for i in lst1:
    for j in lst2:
        if i == j and i not in common:
            common.append(i)

print(common)