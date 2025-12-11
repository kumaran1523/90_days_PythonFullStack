# 10.	Accept marks and print grade (A/B/C/D/Fail).

mark=int(input("Enter mark:"))

if mark>=80 and mark<=100:
    print("Grade A")
elif mark>=60 and mark<=79:
    print("Grade B")
elif mark>=50 and mark<=59:
    print("Grade C")
elif mark>=40 and mark<=49:
    print("Grade D")
elif mark>=0 and mark<=39:
    print("Fail")
else:
    print("Enter Valid marks")
