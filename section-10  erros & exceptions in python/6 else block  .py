# how to avoid ZeroDivision Error

n = int(input("Enter numerator :- "))
d = int(input("Enter denominator :- "))
result = 0

try:
    result = n/d 
except ZeroDivisionError:
    print("Cannot divide a number by zero")
else:
    print(result)



