# 6.	Accept a number and print its multiplication table.

num=int(input("Enter number to multiple:"))

for i in range(1,11,1):
    print(f"{i}*{num} = {i*num}")