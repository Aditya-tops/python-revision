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
    choice = input("Do you want to continue shopping ?")

    if choice == "yes":
        print("here is a list of products and prices")
        for product in products:
            print(f"{product['name']} : {product['description']} : ${product['price']}")


