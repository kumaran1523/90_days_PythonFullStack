# 4. Count how many times a value appears


# cnt=[10,3,4,5,2,3,4,4]
# print(cnt.count(4))

number=int(input("Enter how many values store in list:"))
lst=[]

for i in range(number):
    ent=int(input(f"Enter a number {i+1}: "))
    lst.append(ent)
    
findValue=int(input("Enter a value to find the count or repeatation:"))

cnt=lst.count(findValue)

print(f"The count of {findValue} is {cnt}")
    