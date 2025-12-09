# 15. Check if person is child / adult / senior (age categories)

age=int(input("Enter age:"))

if(age>1 and age<=17):
    print("Child")
elif(age>17 and age<=25):
    print("Adult")
elif(age>25 and age<=125):
    print("Senior")
else:
    print("Enter Valid age")