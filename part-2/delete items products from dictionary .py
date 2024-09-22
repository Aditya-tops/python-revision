products = {
    "phone": 100,
    "tablet": 200,
    "laptop": 400,
    "journal": 40,
}

print(products)

deleted_product = input("Enter the name of the product to be deleted: ")
del products[deleted_product]
print(f"Product deleted. Here are the updated products: {products}")


'''
if deleted_product in products:
    del products[deleted_product]
    print(f"Product deleted. Here are the updated products: {products}")
else:
    print(f"Product '{deleted_product}' not found in the list.")
'''