# 2. Add a new key–value pair into an existing dictionary.

limit=int(input("Enter a limit to enter :"))
student={}

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print("The Entered records are:")
for k,v in student.items():
    print(k,":",v)
    
limit2=int(input("Enter how many records you need to add:"))

for j in range(limit2):
    
    new_name=input(f"Enter a name {j+1} :")
    new_mark=int(input(f"Enter a {new_name}'s mark :"))
    student[new_name]=new_mark
    
print('The Updated records are:')
for key,value in student.items():
    print(key,":",value)