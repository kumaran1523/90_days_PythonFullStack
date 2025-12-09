# 16. Slice list to get middle elements

limit=int(input('Enter a limit:'))
lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1}:"))
    lst.append(number)
print(lst)

middle=lst[len(lst)//2] #example like lst[len(6//2)]=lst[3]
print(f"The middle element of {lst} is :{middle}")