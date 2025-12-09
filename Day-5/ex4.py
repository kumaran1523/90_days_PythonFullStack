#  4. Delete a key from a dictionary using del.

student={"kumaran":56,"saroo":45,"Sayan":89,"Sanya":99}

print('The records before delete:')
for k,v in student.items():
    print(k,":",v)
    
del student["kumaran"]

print('The records after delete:')
for k,v in student.items():
    print(k,":",v)
    