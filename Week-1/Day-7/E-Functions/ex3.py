# Function to check palindrome (string).
 
def is_palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False

word=input('Enter a word:')

if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    