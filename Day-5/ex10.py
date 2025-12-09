# 10. Create a dictionary and print only the keys whose value is greater than 50.

limit=int(input("Enter a limit:"))
student={}

for i in range(limit):
    name=input(f"Enter a name {i+1} :")
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark

print("the records are:")
for k,v in student.items():
    print(k,":",v)
    
print("The keys whose value is greater than 50 marks")

for key in student.keys():
    if(student[key]>50):
        print(key)
        