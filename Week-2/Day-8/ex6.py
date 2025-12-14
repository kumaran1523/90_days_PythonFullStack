# Store 5 student names in a file.

with open("stud.txt","w") as f:
    for i in range(1,6):
        name=input(f"Enter name {i}:")
        f.write(f"{name}\n")
    
print("5 Student name added successfully....")
    