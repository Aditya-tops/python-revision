products = ["phone", "tablet", "laptop", "journal"]

# Displaying in product
print(f'Current list of item : {products}')

add_item = input("Enter product to add :- ")

add_after = input(f'After which product do you want to place {add_item} ')
index = products.index(add_after)
print(index)
products.insert(index+1,add_item)

print(f'Current list of item : {products}')

