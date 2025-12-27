# 11. Merge two dictionaries into one.

dict1={
    'kumar':45,
    "ganga":78,
}

dict2={
    "harshu":89,
    "Dev":99
}
print("The dict1 dictionary is:")
for k,v in dict1.items():
    print(k,":",v)

print("The dict2 dictionary is:")
for k,v in dict2.items():
    print(k,":",v)
    
# dict3={}

# for k,v in dict1.items():
#     dict3[k]=v
# for k,v in dict2.items():
#     dict3[k]=v

dict3=dict1.copy()
dict3.update(dict2)

print("The merge of two dictionaries are: ")
for key,value in dict3.items():
    print(key,":",value)
    
