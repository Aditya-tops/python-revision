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
        for index, product in enumerate(products):
            print(f"{index}: {product['name']} : {product['description']} : ${product['price']}")
        product_id = int(input("Enter the ID of the product you want to add to the cart: "))

        # check if product is already present in the cart
        if products[product_id] in cart:
            products[product_id]['quantity'] +=  1
        else:
            products[product_id]['quantity']=1
            cart.append(products[product_id])


        total = 0
        print(f"Current cart contents are:")
        for product in cart:
            print(f"{product['name']}:{product['price']}: QTY:{product['quantity']}")
            total = total + product['price']*product['quantity']
        print(f"Cart total is : ${total}")
    else:
        break

print(f"Thank you, your final cart contents are: {cart}")
