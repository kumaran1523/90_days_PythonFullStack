# 16. Create a dictionary where key = number and value = its square. (1 to n)

n=int(input('Enter a number:'))
squares={}

for i in range(1,n+1):
    squares[i]=i**2

for k,v in squares.items():
    print(k,":",v)