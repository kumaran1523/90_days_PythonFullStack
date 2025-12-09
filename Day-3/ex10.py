# 10. Find factorial of a number

# 5!=5*4*3*2*1=120
number=int(input("Enter the factorial number:"))
mul=1
for i in range(1,number+1):
    mul=mul*i
print(f"The factorial of {number} is {mul}")