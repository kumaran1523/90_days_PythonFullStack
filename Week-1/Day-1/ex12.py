# 12. Write a program to calculate simple interest.

#Simple Interest (SI) = (Principal * Rate * Time) / 100

principal=float(input('Enter a principal value:'))
rate=float(input('Enter a Rate of intrest :'))
Time=float(input('Enter a Time(in years) :'))

total=principal*rate*Time
SI=total/100

print("The simple intrest is :",SI)
