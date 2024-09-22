def decorator(func):
    def wrapper():
        print("Wrapper up side ")
        func()
        print("Wrapper down side ")
    return wrapper

@decorator
def chocolate():
    print("chocolate")

@decorator
def cake():
    print("cake")


chocolate()
cake()
