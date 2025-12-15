# Use finally block example

try:
    with open("Stud.txt","r") as f:
       print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program ends!")