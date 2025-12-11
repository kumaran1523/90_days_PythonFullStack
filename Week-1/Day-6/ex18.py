# 18. Recursive function to find sum of digits.

def add(n):
   if n==0:
       return 0
   else:
       return n%10 + add(n//10)
   
result=add(1234)
print("The sum of digit:",result)