# Reverse list without using reverse().

lst=[5,6,8,6,1,5,6]

rev=[]

i=len(lst)-1

while i>=0:
    rev.append(lst[i]) 
    i-=1

print(rev)   

print("--------------------")
#Another method

lst1=[5,2,3,9,8,5,3,1,4]

rev1=lst1[::-1]

print(rev1)