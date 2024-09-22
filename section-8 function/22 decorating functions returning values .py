# this function is with decorator

def summer_discount_decorator(func):
    def wrapper(price):
        print("Applying summer discount...")
        discounted_price = price / 2
        return func(discounted_price)
    return wrapper

@summer_discount_decorator
def total(price):
    return price

# Call the total function with a price of 100
print(total(100))
