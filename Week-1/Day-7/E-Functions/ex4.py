# Function to count vowels in a string.

def count_vowel(text):
    vowel='AEIOUaeiou'
    count=0
    
    for i in text:
        if i in vowel:
            count+=1

    return count

word=input("Enter a Word:")
print('The count is :',count_vowel(word))