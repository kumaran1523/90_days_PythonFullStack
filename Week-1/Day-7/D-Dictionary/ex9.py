# Merge two dictionaries.

student1={
    "kumar":56,
    'sanya':100
}
student2={
    "Saroo":98,
    'sayan':78
}

merge_items={}
for k,v in student1.items():
    merge_items[k]=v
for k,v in student2.items():
    merge_items[k]=v

print("merge is :",merge_items)


# another method 

student1.update(student2)
print(student1)