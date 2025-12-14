# Count frequency of each word in file.

word_Count={}

with open("stud.txt","r") as f:
    for i in f:
        word=i.split()
        for j in word:
            j=j.lower()
            if j in word_Count:
                word_Count[j]+=1
            else:
                word_Count[j]=1
                
print('frequency count')

for key,value in word_Count.items():
    print(f"{key}:{value}")