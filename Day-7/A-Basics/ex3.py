# 3.	Accept age and check if eligible to vote.

age=int(input('Enter a :'))

if(age>=18):
    print(f"You age is {age},So you are eligible for vote")
else:
    print(f"You age is {age},So you are not eligible for vote")