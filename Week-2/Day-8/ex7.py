# Read student names and print them one by one.

with open("stud.txt","r") as f:
    for i in f:
        print(i.strip())
        