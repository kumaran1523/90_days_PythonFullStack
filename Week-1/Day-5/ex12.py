# 12. Count the frequency of each character in a string using a dictionary.

text=input("enter a text:")
freq={}

for char in text:
    if(char in freq):
        freq[char]=freq[char]+1
    else:
        freq[char]=1
    
for k,v in freq.items():
    print(k,":",v)
    