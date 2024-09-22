products = ["phone", "tablet", "laptop", "journal"]

# Displaying in product
print(f'Current list of item : {products}')

# asking user to remove a product
remove_item = input("Enter prouct to remove from the ablove list :- ")
products.remove(remove_item)

# display the entire list after removing item
print(f'Current list of item : {products}')


# code to add product 
add_item = input("Enter product to add :- ")
products.append(add_item)

# Displaying the entire list after adding items
print(f'Current list of item : {products}')
