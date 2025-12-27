#  9. Print all key-value pairs using items().

student={
    "kumar":45,
    "Ganga":89,
    "sayan":78,
    "sanya":99
}

print("The printable of key and value using items():")

for key,value in student.items():
    print(key,":",value)