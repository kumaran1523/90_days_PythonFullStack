# 11. Sort list ascending and descending

list1=[2,4,6,2,3,4,1,5,9]

list2=[]

for i in list1:
    list2.append(i)

list2.sort()
print(f"The Ascending order of {list1} is:{list2}")

print("---------------------------------------------------")
list3=[]

for j in list2:
    list3.append(j)
list3.sort(reverse=True)
print(f"The Descending order of {list1} is :{list3}")