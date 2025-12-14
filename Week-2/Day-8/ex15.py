# Read file and convert to list.

lst=[]
with open('stud.txt','r') as f:
    line=f.readlines()
    for i in line:
        lst.append(i.strip())
    print(lst)
        