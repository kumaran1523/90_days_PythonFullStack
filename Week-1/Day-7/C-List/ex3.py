# Find min and max in a list.

lst=[5,7,8,9,3,5,4,1]

max=lst[0]
min=lst[0]

for i in lst[1:]:
    if i>max:
        max=i
    if i<min:
        min=i

print("maximum is:",max)
print("minimum is:",min)


#Another built-in method

'''
lst=[7,5,6,9,8,4,2,3]

print("maximum is:",max(lst))
print("minimum is:",min(lst))
'''
