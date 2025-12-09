# 1. Create a dictionary of 5 students with marks and print it.


limit=int(input("Enter the limit:"))
student={}

for i in range(limit):
    name=input(f'Enter a name {i+1} :')
    mark=int(input(f"Enter a {name}'s mark :"))
    student[name]=mark
    

for key,value in student.items():
    print(key ,":", value)
