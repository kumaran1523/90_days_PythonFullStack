# Count number of lines in a file.

with open("Student.txt","r") as f:
    count=0
    for i in f:
        count+=1
    print(f"{count} lines occured")