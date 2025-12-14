# Search a name in file.

name=input('Enter a name to search: ')

with open("stud.txt","r") as f:
    if name in f.read():
        print("The name is in the file")
    else:
        print("The name is not in the file")