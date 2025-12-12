student={}

def get_average(avg):
    if avg >=90: 
        return "Grade A"
    elif avg >=75:
        return "Grade B"
    elif avg >=60:
        return "Grade C"
    elif avg>=40:
        return "Grade D"
    elif avg<40:
        return "Fail"

def add_student():
    name=input('Enter a name :')
    roll_no=int(input("Enter roll number:"))
    
    if roll_no in student:
        print(f"{roll_no} is already exist")
        return
    
    marks=[]
    
    for i in range(1,4):
        num=int(input(f"Enter a mark {i} :"))
        marks.append(num)
    
    avg=sum(marks)/3
    grade=get_average(avg)   
    
    student[roll_no]={
        "name":name,
        "marks":marks,
        "Average":avg,
        "Grade":grade
    }    
    print("Students Details added successfully!")
    print()
    
def view_all_stud():
    if not student:
        print("No records in student")
        return
    print("-------------View All Students------------------")
    for roll_no,v in student.items():
        print(f"Roll no :{roll_no} | Name :{v["name"]} | Marks :{v["marks"]} | Average :{v["Average"]} | Grade :{v["Grade"]}")
        print()
        
def serach_student():
    
    roll_no=int(input('Enter roll number to search :'))
    
    if roll_no not in student:
        print(f"{roll_no} is not found in the student list")
        return
    print()
    print("Student Found......")
    print(f"Name: {student[roll_no]["name"]}")
    print(f"Marks: {student[roll_no]["marks"]}")                     
    print(f"Average: {student[roll_no]["Average"]}")                     
    print(f"Grade: {student[roll_no]["Grade"]}")   
    print()
    
def update_student_marks():
    print("-----------Update Student marks----------------\n")
    roll_no=int(input('Enter a roll number to update :'))
    if roll_no not in student:
        print(f"{roll_no} is not in Students record")
        return
    print("Student found")
    update_mark=[]
    for i in range(1,4):
        marks=int(input(f"Enter a mark {i}: "))
        update_mark.append(marks)
    
    avg=sum(update_mark)/3
    grade=get_average(avg)
    
    student[roll_no]["marks"]=marks
    student[roll_no]["Average"]=avg
    student[roll_no]["Grade"]=grade
    
    print("Student Marks Updated Successfully")
    
def delete_student():
    print("------------Delete Student-------------\n")
    roll=int(input('Enter a roll number to delete:'))
    
    if roll not in student:
        print(f"{roll} is not found")
        return
    student.pop(roll)
    print("Student record deleted sucessfully.......!")
    
def display_topper():
    if not student:
        print("Student records not found")
        return
    topper=max(student,key=lambda r:student[r]["Average"]) 
    
    '''
    def check_avg(r):
        return student[r]['Average']
    
    we write like lambda r:student[r]["Average"]
    '''
    
    print("topper in student records")
    print("Roll :",topper)
    print("Name :",student[topper]["name"])     
    print("Average :",student[topper]["Average"])     
    print("Grade :",student[topper]["Grade"])     
    print()
    
while True:
    print("---------------Students Management System---------------")
    print("1.Add new Student")
    print("2.View All Student")
    print("3.Search Student")
    print("4.Update Student Marks")
    print("5.Delete a student")
    print("6.display topper")
    print("7.Exit")
    print("---------------------------------------------------------")

    choice=int(input('Enter your choice: '))
    
    match(choice):
        
        case 1:
            add_student()
        case 2:
            view_all_stud()
        case 3:
            serach_student()
        case 4:
            update_student_marks()
        case 5:
            delete_student()
        case 6:
            display_topper()
        case 7:
            print("Exiting the student records....Goodbye!")
            break
        case _:
            print("Enter a valid choice ")
            