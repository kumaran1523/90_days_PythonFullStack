# Print keys whose value > 50.

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

print("Who are above 50 marks")
for key,value in student.items():
     if value>=50:
         print(key)