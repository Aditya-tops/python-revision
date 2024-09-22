products = {
    "phone": 100,
    "tablet": 200,
    "laptop": 400,
    "journal": 40,
}

print(products)

# this code is check for products items
product = input("Enter input product to check the price: ")
print(f"Price of the {product} is {products[product]} $ ")

# this code is check for new add products items
new_product = input("Enter a product you want to add: ")
new_product_price = int(input(f"Enter the price for {new_product}: "))  # Convert price to an integer
products[new_product] = new_product_price # this logic is use for key value pair
print(f"Product successfully added. Here is an updated list of products: {products}")
