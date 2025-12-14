# Count number of words in a file.

count=0
with open('Student.txt','r') as f:
    for i in f:
        word=i.split()
        count+=len(word)
    print(count)
        
               