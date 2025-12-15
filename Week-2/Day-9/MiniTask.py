'''
👉 Safe Calculator
•	Input two numbers
•	Perform add, subtract, multiply, divide
•	Handle all errors using try-except

'''

while True:
    print("************Safe Calculator*****************\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Exit")
    print("****************************************")
    
    try:
        choice=int(input("Enter a choice :"))
    except ValueError:
        print('Enter integer data')
    
        
    match choice:
        case 1:
            try:
                n1=int(input("Enter a number 1 :"))
                n2=int(input('Enter a number 2 :'))
                result=n1+n2
            except ValueError:
                print('Enter a integer Value')
            except TypeError:
                print("print correct argument")
            else:
                print("Addition is :",result)
            finally:
                print("Addition Ended")
                
        case 2:
            try:
                n1=int(input("Enter a number 1 :"))
                n2=int(input('Enter a number 2 :'))
                result=n1-n2
            except ValueError:
                print('Enter a integer Value')
            except TypeError:
                print("print correct argument")
            else:
                print("Subtraction is :",result)
            finally:
                print("Subtraction Ended")  
                
        case 3:
            try:
                n1=int(input("Enter a number 1 :"))
                n2=int(input('Enter a number 2 :'))
                result=n1*n2
            except TypeError:
                print('Type Error occured')
            except ValueError:
                print('Enter correct value')
            else:
                print("Multiplication is :",result)
            finally:
                print('multiplication Ended')
                
        case 4:  
            try:
                n1=int(input("Enter a numerator :"))
                n2=int(input('Enter a denominator :'))
                result=n1/n2
            except TypeError:
                print('Type Error occured')
            except ValueError:
                print('Enter correct value')
            except ZeroDivisionError:
                print('Zero value occured in denominator')
            else:
                print("Divide is :",result)
            finally:
                print('Divide Ended')
            
        case 5:
            print('Exiting Goodbye....!')
            break
        case _:
            print('Enter valid choice')