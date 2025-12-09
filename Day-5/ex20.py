# 20. Check if a value exists in the set.

limit=int(input("Enter a limit:"))
my_set=set()

for i in range(limit):
    number=int(input(f'Enter a ssrt {i+1} :'))
    my_set.add(number)
    
print("The set is:",my_set)

check_value=int(input("Enter a value to check :"))

if check_value in my_set:
    print(f"The Value {check_value} is present in sets")
else:
    print(f"The Value {check_value} is not present in sets")
    