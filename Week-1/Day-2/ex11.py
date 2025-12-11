# 11. Input marks and print grade (A, B, C, Fail)

mark=float(input("Enter marks:"))
if(mark>80 and mark<=100):
    print("Grade A")
elif(mark>60 and mark<=80):
    print("Grade B")
elif(mark>=40 and mark<=60):
    print("Grade C")
elif(mark<40 and mark>=0):
    print("Fail")
else:
    print("Enter valid mark")