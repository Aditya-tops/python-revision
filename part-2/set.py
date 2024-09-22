numbers = set([1,2,3,4,5,6])
print(numbers) # {1, 2, 3, 4, 5, 6}

number = {1,2,3,4,5,6,7,8,9}
print(number) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

prices = {100,200,300,200,300,200}
print(prices) # {200, 100, 300}
# duplicate valuers are not allow in set

names = {"aditya","kunal","udesh","aditya"}
print(names) # {'kunal', 'aditya', 'udesh'}

s = {"aditya",True,17.5,"aditya"}
print(s) # {True, 17.5, 'aditya'}

# how to create Empty set 
a = {}
print(type(a)) # <class 'dict'>
print(a) # {}

b = set()
print(type(b)) # <class 'set'>
print(b) # set()


