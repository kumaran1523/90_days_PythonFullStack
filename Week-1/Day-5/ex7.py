# 7. Print all keys using keys().

limit=int(input("Enter a limit:"))
student={}

for i in range(limit):
    name=input(f'Enter a name {i+1} :')
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark
print("the records are:")   
for k,v in student.items():
    print(k,":",v)
    
print("The keys are:")
for j in student.keys():
    print(j)