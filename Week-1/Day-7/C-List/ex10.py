	# Find second largest number in list.
 
lst=[5,6,7,9,9,5,1,2,7]

unique=[]

for i in lst:
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)

print("the second Largest value in list is :",unique[-2])
