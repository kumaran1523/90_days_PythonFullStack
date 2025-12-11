# Delete a key using pop().

student={}

limit=int(input('Enter a limit:'))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print('\n The dictionary are:')
for k,v in student.items():
    print(k,":",v)

name1=input("Enter a name to delete :")
if name1 in student:
    student.pop(name1)
    print('deleted successfully')
else:
    print("Enter valid name")

print('\n After deletion dictionary are:')
for k,v in student.items():
    print(k,":",v)
