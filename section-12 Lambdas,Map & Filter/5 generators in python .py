'''
def function():
    counter = 0
    while counter<=10:
        yield counter
        counter = counter + 1
print(list(function()))
'''
# Generate a list of even number
def even_generator(x):
    for i in range (x):
        if i%2==0:
            yield i

print(list(even_generator(10)))


