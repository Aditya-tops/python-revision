def chocolate():
    print("chocolate")

def decorator(func):
    def wrapper():
        print("Wrapper up side ")
        func()
        print("Wrapper down side ")
    return wrapper

# Apply the decorator
chocolate = decorator(chocolate)

# Call the decorated function
chocolate()
