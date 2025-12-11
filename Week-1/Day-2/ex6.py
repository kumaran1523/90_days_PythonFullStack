# 6. Check if a year is a leap year

year=int(input("Enter a leap year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a leap year")
        else: 
            print(f"{year} is not a leap year")  
    else: 
        print(f"{year} is a leap year")   
else: 
    print(f"{year} is not a leap year")   
        
