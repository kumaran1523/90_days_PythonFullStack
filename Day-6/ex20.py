# 20. Recursive function to find power (xⁿ).

def power(n,x):
    if x==0:
        return 1
    else:
        return n *power(n,x-1)

print(power(2,5))