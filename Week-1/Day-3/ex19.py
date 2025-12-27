#  19. Print string in reverse using loop

character=input('Enter a String:') #hello

i=len(character)-1 #5-1=4 --> Because it starts with 0
while i>=0: #4>=0
    print(character[i],end="") #character[4]='o'
    i=i-1 #4-1=3