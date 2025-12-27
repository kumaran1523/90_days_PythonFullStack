# 22. Find intersection of two sets.

limit1=int(input("Enter a limit for set 1:"))
set1=set()

for i in range(limit1):
    num1=int(input(f"Enter a set {i+1} :"))
    set1.add(num1)
    
print("The set 1 is :",set1)

limit2=int(input('Enter a limit for list 2 : '))
set2=set()

for j in range(limit2):
    num2=int(input(f"Enter a set {j+1} :"))
    set2.add(num2)
    
print('The set 2 is :',set2)

print('The intersection of two sets is :',set1.intersection(set2))