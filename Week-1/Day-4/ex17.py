# 17. Access last 3 elements using slicing

limit=int(input("Enter a limit:"))
lst=[]
for i in range(limit):
    num=int(input("Enter a number: "))
    lst.append(num)

print("The list is:",*lst)

last_3=lst[-3:]

print('the last 3 element in a list is :',*last_3)