def sum(numbers):
    total = 0
    for number in numbers:
        total=total+ number
        

    return total


scores = [1,2,3,4,5,6]
result = sum(scores)
print('Sum of all elements',result)