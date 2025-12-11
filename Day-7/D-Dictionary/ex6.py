# Print only values.

student={}

limit=int(input('Enter a limit:'))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print()
print('The dictionary are:')
for k,v in student.items():
    print(k,":",v)
 
print()
print("The Values are ")
for v in student.values():
    print(v,end=" ")