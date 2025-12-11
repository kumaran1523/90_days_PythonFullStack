# Check if a number is prime.

num=int(input("Enter a prime number: "))


if num>1:
    for j in range(2,num):
        if num%j==0:
            print(f"{num} is not a prime")
            break
    else:
        print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")