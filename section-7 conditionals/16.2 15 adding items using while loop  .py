products = [
    {'name': "smartphone", 'price': 500, 'description': "A handheld device"},
    {'name': "tablet", 'price': 300, 'description': "A portable touchscreen device"},
    {'name': "Laptop", 'price': 1000, 'description': "A portable computer"},
    {'name': "Headphones", 'price': 50, 'description': "A pair of earphones"},
    {'name': "smartwatch", 'price': 300, 'description': "A wearable device used for fitness tracking and receiving notifications"},
    {'name': "bluetooth speaker", 'price': 100, 'description': "A portable speaker that connects wirelessly to devices"}
]

cart = []

while True:
    choice = input("Do you want to continue shopping? (yes/no): ").strip().lower()

    if choice == "yes":
        print("Here is a list of products and prices:")
        for product in products:
            # Use double quotes for strings within f-strings to avoid conflicts
            print(f"{product['name']} : {product['description']} : ${product['price']}")
        
        item_name = input("Enter the name of the product you want to add to the cart: ").strip().lower()
        
        # Find the product in the list and add it to the cart
        for product in products:
            if product['name'].lower() == item_name:
                cart.append(product)
                print(f"{product['name']} has been added to your cart.")
                break
        else:
            print("Sorry, that product is not available.")
        
    elif choice == "no":
        print("Thank you for shopping with us!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
