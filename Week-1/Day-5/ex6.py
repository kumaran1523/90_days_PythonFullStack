# 6. Check if a key exists in the dictionary.

student={
    "kumar":45,
    "saroo":99,
    "sayan":89,
    "sanya":100
}

check_key=input('Enter a name:')
if(check_key in student):
    print(f"Yes, the key {check_key} is present in student record")
else:
    print(f"No, the key {check_key} is not present in student record")