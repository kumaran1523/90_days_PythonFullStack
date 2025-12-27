# 14. Store 5 product names with prices (user input) and print the cheapest product.

product={}

for i in range(1,6):
    product_name=input(f"Enter a product name {i} :")
    product_price=float(input(f"Enter a {product_name}'s price :"))
    product[product_name]=product_price
    
print('The records are :')
for key,value in product.items():
    print(key,":",value)
    
cheapest_product=min(product,key=product.get) 

'''#min(dictionary,key=dictionary.get) ==>Tha product values is stored in key and get minimum value of product name'''

print(f"The cheapest product is:{cheapest_product}")