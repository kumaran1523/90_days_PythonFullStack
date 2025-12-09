# 7. Reverse a list without using reverse()

limit=int(input("Enter a limit:"))

lst=[]

for i in range(limit):
    number=int(input(f"Enter a number {i+1} :"))
    lst.append(number)
    
reverse_list=[]

for j in lst:
    reverse_list.insert(0,j)  #inser(position,value)

print("The original List:",lst)
print("------------------")
print("The reverse List:",reverse_list)
