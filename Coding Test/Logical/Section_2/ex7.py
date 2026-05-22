'''
7. Check Leap Year
Sample Input
2024
Sample Output
2024 is a Leap Year
'''

year=int(input("Enter a year :"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:       
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")
