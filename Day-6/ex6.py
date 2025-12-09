# 6. Write a function that returns the largest of 3 numbers.

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

result=largest(5,6,1)
print("The largest value is:",result)
        