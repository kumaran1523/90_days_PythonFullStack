# Calculate age using birth year

from datetime import date 
age=int(input("enter your birth year :"))
today=date.today().year

your_age=today-age

print('your current age is :',your_age)