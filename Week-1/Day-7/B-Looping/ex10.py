	# Calculate factorial using loop.
 
limit=int(input('Enter a limit:'))
fact=1
while limit>0:
    fact=fact*limit
    limit-=1

print(fact)