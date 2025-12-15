# Handle divide by zero error

try:
        
    a=int(input("Enter a numerator :"))
    b=int(input("Enter a denominator :"))
    print(a/b)
except ZeroDivisionError:
    print(f'{a} is not divisible by {b}')