#  12. Check if value exists in list

limit=int(input("Enter a limit to enter:"))

lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1} : "))
    lst.append(number)

exist_value=int(input('Enter a finding value:'))

if exist_value in lst:
    print(f'{exist_value} is exist in list')
else:
    print(f'{exist_value} is not exist in list')
    