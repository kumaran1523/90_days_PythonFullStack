#  20. Count vowels in a string

character=input("Enter a String:")
count=0
vowels='aeiouAEIOU'
for i in character:
    if i in vowels:
        count=count+1
print(f"The count vowel of {character} is {count}")
    
        