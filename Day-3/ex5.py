# 5. Print multiplication table of any number

num=int(input("Enter a number to multiply:"))

for i in range(1,11):
    print(f"{i} * {num} = {i*num}")