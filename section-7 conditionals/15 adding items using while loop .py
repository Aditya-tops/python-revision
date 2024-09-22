cart = []

while True:
    choice = input("Do you want to add an item to the cart? (yes/no): ").strip().lower()
    if choice == "yes":
        item = input("Enter the item you want to add: ").strip()
        cart.append(item)
        print(f"Current cart contents are: {cart}")
    elif choice == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")
