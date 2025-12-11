# 8. Print all values using values().

student={"kumar:":45,"saroo":78,"sayan":89,"sanya":99}

print("the record of key and value are: ")
for k,v in student.items():
    print(k,":",v)
    
print("The record of values are:")

for value in student.values():
    print(value)