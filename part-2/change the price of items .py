products = {
    "phone": 100,
    "tablet": 200,
    "laptop": 400,
    "journal": 40,
}

print(products)

price_change_product = input("Enter product for which you want to change the price :-")
price_change = input(f'Enter the new price {price_change_product}')
products[price_change_product]=price_change
print(f"Price updated sucessfully, here is a list of products {products}")