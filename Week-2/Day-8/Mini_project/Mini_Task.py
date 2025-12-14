# 🎯 Mini Task (Recommended)
# 👉 Student Record File System
# •	Add student
# •	View students
# •	Save to file
# •	Load from file
# (Uses Day 1–8 concepts together)


student={}

# •	Add student

def add_student():
    name=input('Enter a name :')
    roll=int(input(f"Enter {name}'s roll number :"))
    
    if roll in student:
        print ("Already exists")
    else:
        student[roll]=name
        print("Student added successfully")
    
# •	View students

def view_student():
    if not student:
        print( "Not found in record")
    else:
        print("Student records....")
        for roll,name in student.items():
            print(f"Roll Number :{roll} | name :{name}")
    
# •	Save to file

def save_file():
    with open("Student_record.txt","w") as f:
        for roll,name in student.items():
            f.write(f"{roll}:{name} \n")
        
        print('Data Saved successfully')

# •	Load from file

def load_data():
    student.clear()
    try:                      #We discussed this try (Exceptional handling) in day 9 
        with open("student_record.txt",'r') as f:
            for i in f:
                i=i.strip()
                if not i or "," not in i:
                    continue
                roll,name=i.split(",")
                student[int(roll)]=name
            print('data loaded Successfully')    
    except FileNotFoundError:
        print("File not found")

while True:
    print("---------------------------------Student record File System-----------------------\n")
    print("1.Add Student")
    print("2. View Student")
    print("3.Save to file")
    print("4.Load from file")
    print("5.Exit")
    print("-----------------------------------------------------------------------------------")
    print()
    
    choice=int(input("Enter your choice: "))
    
    match choice:
        case 1:
            add_student()
        case 2:
            view_student()
        case 3:
            save_file()
        case 4:
            load_data()
        case 5:
            print("Exiting the data Goodbye!.............")
            break
        case _:
            print("Enter valid Choice")
   