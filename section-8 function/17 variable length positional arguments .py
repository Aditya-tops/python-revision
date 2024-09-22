def add(*args):
    sum = 0
    for n in args:
       # print("args store in list ",n)
       sum = sum + n
    return sum

print(add(2,3,5,2,5,6,4,45,4,5,3,6,4,4,7,9,5,4,4))