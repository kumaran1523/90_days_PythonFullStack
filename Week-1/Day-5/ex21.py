# 21. Find union of two sets.

limit1=int(input('Enter a limit of set 1: '))
set_1=set()

for i in range(limit1):
    num1=int(input(f"Enter a set {i+1} :"))
    set_1.add(num1)
    
print("The set 1 is :",set_1)

limit2=int(input('Enter a limit of set 2: '))
set_2=set()

for j in range(limit2):
    num2=int(input(f"Enter a set {j+1} :"))
    set_2.add(num2)
  
print("The set 2 is :",set_2)

print("The union of two sets is :",set_1|set_2)