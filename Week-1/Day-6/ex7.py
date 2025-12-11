# 7. Write a function that counts vowels in a string.

def vowels(a):
    count=0
    for ch in a:
        if ch in 'AEIOUaeiou':
            count+=1
    print(count)
vowels("Kumaran")