# Copy contents from one file to another.

with open('Student.txt','r')as source:
    with open("Copy_Student.txt","w") as destination:
        for i in source:
            destination.write(i)
            
print('The file copied succesfully')