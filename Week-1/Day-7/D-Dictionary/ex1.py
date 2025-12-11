# Create a dictionary of 5 students with marks.

student={}

limit=int(input('Enter a limit:'))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

for k,v in student.items():
    print(k,":",v)