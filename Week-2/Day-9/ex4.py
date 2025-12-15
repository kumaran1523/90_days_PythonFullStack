# Use else block example

try:
    a=int(input('Enter a numerator :')) 
    b=int(input('Enter a denominator :')) 
    c=a/b
except ZeroDivisionError:
    print("Denominator is not a zero")
except ValueError:
    print('Enter Integer value')
else :
    print("Result :",c)
