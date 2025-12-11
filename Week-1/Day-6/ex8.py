# 8. Write a function that prints multiplication table of a number.

def mul(a):
    for i in range(1,11,1):
        print(f"{i}*{a}={i*a}")
        
mul(5)
        