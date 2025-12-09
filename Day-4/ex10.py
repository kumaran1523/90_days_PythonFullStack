# 10. Merge two lists

list1=[10,20,30,40]
list2=[20,30,40,60]

list3=[]
for i in list1:
    list3.append(i)

for j in list2:
    list3.append(j)
    
print(list3)

print("--------------------------")

list4=list1+list2
print(list3)

print("----------------------------")

list1.extend(list2)
print(list1)

