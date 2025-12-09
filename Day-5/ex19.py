# 19. Remove an element using discard() and explain difference.

my_set=set()

my_set.add(5)
my_set.add(6)
my_set.add(7)
my_set.add(8)
my_set.add(9)

print("the sets are :",my_set)

my_set.discard(9)

print("the sets are :",my_set)

'''
remove() --> it is used to remove values but the given value is not present it provide error
discard() --> It is used to remove the value ,if the given value is not present it does not provide an error
'''

