# Count occurrences of a given value.

lst=[5,6,7,8,9,3,5,4]
count=0
val=int(input("Enter a value :"))
for i in lst:
    if val==i:
        count+=1

print("The occurance :",count)