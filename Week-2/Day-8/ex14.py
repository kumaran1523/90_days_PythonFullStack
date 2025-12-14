#  Store dictionary data into file.
 
student={}

limit=int(input('Enter a limit : '))

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter {name}'s mark :"))
    student[name]=mark

for k,v in student.items():
    print(f"{k}:{v}")
    
with open('Dict_data.txt','w') as f:
    for key,value in student.items():
        f.write(f"{key}:{value}\n")

print("Dictionary data stores in file successfully")