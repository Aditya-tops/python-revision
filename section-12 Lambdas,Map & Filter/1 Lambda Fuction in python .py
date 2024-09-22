'''
def square(x):
    return x**2

print(square(9))
'''
# using one parameter
result = (lambda x: x**2)(9)
print("square:- ",result)

# using two parameter
sum = (lambda x,y: x+y)(9,10)
print("Sum is :- ",sum)

# using two parameter using keyword arguments
sum = (lambda x,y: x+y)(x=50,y=10)
print("Sum is :- ",sum)

sum = (lambda x=10,y=20: x+y)(y=50)
print("Sum is :- ",sum)