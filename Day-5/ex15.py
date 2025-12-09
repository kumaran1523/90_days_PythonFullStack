# 15. Take input from user: enter a name → show phone number (search in dictionary).

limit=int(input("Enter a limit:"))
contact={}

for i in range(limit):
    name=input(f"Enter a name{i+1} :")
    ph_number=input(f"Enter a {name}'s number :")
    contact[name]=ph_number
    
print("The records are:")
for k,v in contact.items():
    print(k,":",v)
    
show_number=input("Enter a name to get:")

if(show_number in contact):
    print(f"The {show_number}'s number is",contact[show_number])
else:
    print('It is not in contact')