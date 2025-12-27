# 3. Update the value of an existing key.

limit=int(input("Enter a limit to enter:"))
student={}

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark : "))
    student[name]=mark
print("The records are:")
for k,v in student.items():
    print(k,":",v)
    
update_value=input('Enter a name to update mark :')

if(update_value in student):
    update=int(input("Enter a updated mark :"))
    student[update_value]=update
else:
    print("The given name is not in a record")
    
if(update_value in student):
    print("The updated records are:")
    for key,value in student.items():
        print(key,":",value)
