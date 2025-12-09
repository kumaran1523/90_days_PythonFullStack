# 18. Remove an element using remove().

my_set=set()

my_set.add(5)
my_set.add(6)
my_set.add(7)
my_set.add(8)
my_set.add(9)
my_set.add(5) #remove duplicate

print("the sets are :",my_set)

my_set.remove(5)

print("After removing value 5 is ",my_set)