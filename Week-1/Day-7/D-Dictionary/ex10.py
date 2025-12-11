# Find cheapest product from dictionary.

limit=int(input("Enter a product limit:"))
product={}
for i in range(limit):
    p_name=input(f"Enter a product name {i+1} : ")
    p_price=int(input(f"Enter {p_name} price :"))
    product[p_name]=p_price

for k,v in product.items():
    print(k,":",v)

cheapest=min(product,key=product.get) # key=product.get => it is used to compare the key value
print("cheapest product is :",cheapest)