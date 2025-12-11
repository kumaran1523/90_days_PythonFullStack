# Print even numbers from a list.

limit=int(input("Enter a limit to enter:"))
lst=[]

for i in range(limit):
    num=int(input(f"Enter a num {i+1} :"))
    lst.append(num)
print("List is :",lst)

even=[]
for j in lst:
    if j%2==0:
       even.append(j)

print("Even is :",even) 