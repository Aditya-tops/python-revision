'''
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_nums=[]
for number in numbers:
    if number%2==1:
        odd_nums.append(number)
print(odd_nums)
'''
# this code is using filter function
numbers = [1,2,3,4,5,6,7,8,9,10]
def odd(x):
    if x%2==1:
        return x
odd_numbers = list(filter(odd,numbers))
print(odd_numbers)

# this code is using lamda function 
nums = [1,2,3,4,5,6,7,8,9,10]
odd_nums = list(filter(lambda x: x%2==1, nums))
print("this code is using lamda function :- ",odd_nums)
