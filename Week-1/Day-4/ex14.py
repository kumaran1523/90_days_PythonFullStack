#  14. Replace value at a given index

limit=int(input('Enter a limit:'))
lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1}: "))
    lst.append(number)

print("The entered list are:",*lst)
index_value=int(input('Enter index value to change:'))    
replace_value=int(input("Enter a value to replace:"))
print(end=" ")
if(index_value >=0 and index_value<len(lst)):
    lst[index_value]=replace_value
    print("The updated list are: ",*lst)