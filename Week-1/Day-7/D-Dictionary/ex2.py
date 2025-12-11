# Add a new key–value pair.

student={}

limit=int(input('Enter a limit:'))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print('\n The dictionary are:')
for k,v in student.items():
    print(k,":",v)

limit2=int(input("Enter a limit to add:"))
for j in range(limit2):    
	name1=input(f'Enter Name {j+1} :')
	mark1=int(input(f"Enter a {name}'s mark : "))
	student[name1]=mark1
print('\n The updated dictionary are:')
for k,v in student.items():
    print(k,":",v)

