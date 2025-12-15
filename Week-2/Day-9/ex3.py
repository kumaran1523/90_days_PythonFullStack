# Open a file safely using try-except

try:
    with open("Stud.txt","r") as f:
       print(f.read())
except FileNotFoundError:
    print("File not found!")