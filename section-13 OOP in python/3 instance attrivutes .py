class Product:
    quantity = 400

    def __init__(self,name,price):

        self.name = name
        self.price = price


p1 = Product("phone","300")
print(p1.name)
print(p1.price)

p2 = Product("laptop","400")
print(p2.name)
print(p2.price)