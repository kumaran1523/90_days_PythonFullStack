	# Lambda to check even or odd.
 
even_odd=lambda a: "Even" if a%2==0 else "odd"

num=int(input("Enter a number :"))

print(even_odd(num))