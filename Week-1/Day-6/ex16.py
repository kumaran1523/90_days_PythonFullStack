# 16. Recursive function to print numbers 1–10.

def num(n):
    if n>10:
        return
    print(n)
    num(n+1)
num(1)