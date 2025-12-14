# Remove empty lines from file.

with open("Copy_Student.txt",'r') as f:
    lines=f.readlines()

with open('Copy_Student.txt',"w") as f:
    for i in lines:
        if i.strip():
            f.write(i)