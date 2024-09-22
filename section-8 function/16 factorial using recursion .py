# 5! = 5x4x3x2x1 = 120
# 3! = 3x2x1 = 6
# 1! = 1
# 3! = 3 * (number-1) * (number )



def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    

print(factorial(4))  # 24
# factorial(4) --> return 4 * factorial(4-1) 
# factorial(3) --> return 3 * factorial(3-1) 
# factorial(2) --> return 2 * factorial(2-1) 
# factorial(1) --> return 1 * factorial(1-1) 


