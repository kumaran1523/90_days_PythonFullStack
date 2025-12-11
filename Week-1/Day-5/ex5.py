# 5. Delete a key using pop() and print the removed value.

limit=int(input("Enter a limit:"))
student={}

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter the {name}'s mark :"))
    student[name]=mark
print('The records are:')
 
for k,v in student.items():
    print(k,":",v)
    
pop_value=input("Enter a name to pop the value: ")

if(pop_value in student):
    removed_value=student.pop(pop_value)
    print(f"The deleted record of {pop_value} is:{removed_value}")
else:
    print("The given name is not in the records")
    