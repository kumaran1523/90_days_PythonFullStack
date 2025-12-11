# 13. Take 5 names and marks from the user and store in a dictionary.

student={}
for i in range(1,6):
    name=input(f'Enter a name {i} :')
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark
    
print("The Records are:") 
for key,value in student.items():
    print(key,":",value)