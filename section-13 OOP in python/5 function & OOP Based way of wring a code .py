''' in function code 
def Product_data():
    product_name = input("Enter name of product :- ")
    product_price = input("Enter price of the product :- ")
    print(product_name)
    print(product_price)

Product_data()

'''

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input("Enter name of product :- ")
        self.price = input("Enter price of the product :- ")

    def put_data(self):
        print("the name of product name is ",self.name)
        print("this product price is ",self.price)

p1 = Product("","")
p1.get_data()
p1.put_data()