'''
Write a program to print this pattern:

    *
   ***
  *****
 *******
*********
'''

rows=int(input("Enter rows:"))

for i in range(1,rows+1):
    for j in range(1,rows-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()

# rows = 5  

# for i in range(1, rows + 1):  # Loop through rows (1 to 5)
#     spaces = " " * (rows - i)        # Calculate leading spaces
#     stars = "* " * i                 # Generate stars with a space
#     print(spaces + stars)            # Combine and print each row

