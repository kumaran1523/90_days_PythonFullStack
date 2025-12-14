# Store marks and calculate average.
marks=[]
with open('marks.txt','w') as f:
    limit=int(input("Enter limit to add marks:"))
    for i in range(1,limit+1):
        mark=int(input(f"Enter a mark {i}: "))
        marks.append(mark)
    
    for j in marks:
        f.write(f"{str(j)} \n" ) #In file we write only text we convert here to string
        
    print(f"Average is :{sum(marks)/len(marks)}")