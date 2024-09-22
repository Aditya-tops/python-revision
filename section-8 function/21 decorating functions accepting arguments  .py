def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper up side")
        func(*args, **kwargs)  # Pass the arguments properly
        print("Wrapper down side")
    return wrapper

@decorator
def chocolate():
    print("chocolate")

@decorator
def cake(name):
    print("cake " + name)

chocolate()  # No arguments needed
cake("apple")  # Pass the argument "apple"
