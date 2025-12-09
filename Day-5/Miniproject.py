'''
26. Contact Book using Dictionary

    Menu:

   1. Add contact

   2. View contact

   3. Update contact

   4. Delete contact

   5. View all contacts

   6. Exit
'''

contact={
    "kumaran":"8056561670",
    "saranya":"9789386565"
}

while True:
    print()
    print("Contact Book")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.update Contact")
    print("4.Delete Contact")
    print("5.view all Contact")
    print("6. Exit")
    print()
    choice=int(input("Enter your choice :"))

    match(choice):
        
        case 1:
            print("1.Add Contact")
            name=input("Enter name :")
            number=input("Enter number :")
            contact[name]=number
            print("Contact added Successfully")
            
        case 2:
            print("2.View Contact")
            view=input("Enter a name to view :")
            if(view in contact):
                print(f"{view}",contact[view])    
            else:
                print(f"{view} is not in contact list")
        
        case 3:
            print("3.update Contact")
            update_name=input("Enter a name to update :")
            if update_name in contact:
                phone_number=input("Enter a number to update:")
                contact[update_name]=phone_number
                print(f"{update_name} phone number updated succesfully")
            else:
                print(f"{update_name} is naot in contact")
                
        case 4:
            print("4.Delete Contact")
            del_con=input("Enter a name to delete:")
            if(del_con in contact):
                contact.pop(del_con)
                print(f"The contact {del_con} deleted successfully")
            else:
                print(f"The contact {del_con} not in the dictionary")
        
        case 5:
            print("5.view all Contact")
            for key,value in contact.items():
                print(key,":",value)
        
        case 6:
            print("6. Exit")
            print("Exit booking contact Goodbye!")
            break
        case _:
            print("Inavalid! Enter a valid number")       