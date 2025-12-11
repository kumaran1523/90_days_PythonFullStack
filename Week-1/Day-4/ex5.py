# 5. Print even numbers only

limit=int(input('Enter a limit:'))
lst=[]
for i in range(limit):
    number=int(input(f"Enter a number {i+1}: "))
    lst.append(number)

even_lst=[]
for j in lst:
    if(j%2==0):
        even_lst.append(j)

print("The even number is:",*even_lst)
