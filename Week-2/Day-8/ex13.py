# Find longest word in file.

longest_word=""
with open('stud.txt',"r") as f:
    for i in f:
        word=i.split() #split() is udes to divide string into multiple words
        for j in word:
            if len(j)>len(longest_word):
                longest_word=j
            
print("The longest word is:",longest_word)
print("The length is :",len(longest_word))
