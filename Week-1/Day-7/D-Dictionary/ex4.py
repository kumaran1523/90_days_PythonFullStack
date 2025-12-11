# Check if a key exists in dictionary.

student={}

limit=int(input('Enter a limit:'))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print('\n The dictionary are:')
for k,v in student.items():
    print(k,":",v)
    
name1=input("Enter name :")
if name1 in student:
    print(f"{name1} is existed in a dictionary")
else:
    print(f"{name1} is not existed in a dictionary")
    