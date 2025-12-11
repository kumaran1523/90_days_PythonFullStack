#  9. Find second largest

limit=int(input("Enter a limit:"))
lst=[]

for i in range(limit):
    number=int(input(f"Enter a number of {i+1}:"))
    lst.append(number)

max=lst[0]
second_max=None
for j in lst[1:]:
    if j>max:
        second_max=max
        max=j
    elif j!=max:
        if second_max is None or j>second_max:
            second_max=j
        
print("The List is :",lst)
print("-----------------------------")
print("The second max is :",second_max)
        
        
