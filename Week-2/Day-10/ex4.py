# Round a float number up & down

import math
num=float(input("Enter a number :"))

result1=math.ceil(num)
result2=math.floor(num)

print(f"The roundvalue of {num}  up value is {result1} ")
print(f"The roundvalue of {num}  down value is {result2} ")
print('The round value :',round(num))