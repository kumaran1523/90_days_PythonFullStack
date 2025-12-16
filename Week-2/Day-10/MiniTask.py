'''
Mini Task (Recommended)

👉 System Utility Program

•	Show date & time
•	Create folder
•	Check file exists
•	Use math calculations
'''
import datetime
import os
import math

while True:
    print('*********System utility program***************\n')
    print("1.show date and time")
    print("2.Create folder")
    print("3.check file exists")
    print("4.use math calculation")
    print("5.Exit")
    print("***********************************************")

    try:
        choice=int(input("Enter your chooice :"))
    except TypeError:
        print('Enter Argument properly')
    except ValueError:
        print('Enter Integer value')
    
    match choice:
        case 1:
            print("\nShow date and time")
            date_time=datetime.datetime.now().strftime("%d/%m/%y  %H:%M:%S")
            print('Date and time is :',date_time)
        case 2:
            print("\nCreate a folder")
            try:
                folder_name=input('enter a folder name :')
            except ValueError:
                print("print correctly ")
            if os.path.exists(folder_name):
                print("it already exist")
            else:
                os.mkdir(folder_name)
                print(f'The {folder_name} folder is created successfully ')
            
        case 3:
            print("\nCheck file Exists")
            try:
                file_name=input('Enter file name :')
            except ValueError:
                print('Enter correctly')
            if os.path.exists(file_name) and os.path.isfile(file_name):
                print('File Exists')
            else:
                print("File not exists")
        case 4:
            print("\nuse math Calculation\n")
            while True:
                print("1.square root")
                print('2.power of a number')
                print('3.factorial of a number')
                print('4.Exit')
                try:
                    ch=int(input("Enter choice :"))   
                except ValueError:
                    print('Enter integer value')
                match ch:
                    case 1:
                        print("\n Square root")
                        try:
                            n=float(input("Enter a number :"))
                        except ValueError:
                            print('Enter a proper digit')
                        result=math.sqrt(n)
                        print(f"The square root of a {n} is {result}")
                    case 2:
                        print("\n Power of a number")
                        try:
                            n1=float(input("Enter a number :"))
                            n2=int(input('Enter a digit to power a value :'))
                        except ValueError:
                            print("Enter proper digit")
                        power_value=math.pow(n1,n2)
                        print(f"The {n1} power of {n2} is {power_value} ")
                    
                    case 3:
                        print('\nFactorial of a number')
                        try:
                            fact_num=int(input("Enter a Number :"))
                        except ValueError:
                            print('Enter integer digit')
                        result=math.factorial(fact_num)
                        print(f"The factorial of {fact_num} is {result}")
                    case 4:
                        print("\nExit")
                        print("Exiting Calculation module Goodbye..!")
                        break
        case 5:
            print("\n Exit")
            print('Exiting the System utility program Goodbye....!')
            break                        