fruits = [ 'apple', 'mango', 'peach', 'orange', 'watermelon', 'grape']

print('apple' in fruits) # True
print('tometo' in fruits) # False
print('pieapple' not in fruits) # True


# len Function
print('len is fruits :- ',len(fruits))

# insert Function
fruits.insert(1,"Pineapple")  # ['apple', 'Pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape']
print('new fruits list is :- ',fruits)

fruits.append("hello")
print(fruits) # ['apple', 'Pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'hello']

fruits.append(["guava","apricot"])
print(fruits) #['apple', 'Pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'hello', ['guava', 'apricot']]

fruits.extend(["guava","apricot"])
print(fruits) #['apple', 'Pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'hello', ['guava', 'apricot'], 'guava', 'apricot']

fruits.remove('orange')
print(fruits) # ['apple', 'Pineapple', 'mango', 'peach', 'watermelon', 'grape', 'hello', ['guava', 'apricot'], 'guava', 'apricot']

fruits.pop()
print(fruits) # ['apple', 'Pineapple', 'mango', 'peach', 'watermelon', 'grape', 'hello', ['guava', 'apricot'], 'guava']

fruits.pop()
fruits.pop()
print(fruits) # ['apple', 'Pineapple', 'mango', 'peach', 'watermelon', 'grape', 'hello']

print(fruits.index('hello')) # 6

scores = [1,2,3,4,5,6,7,8,9,10]
print(max(scores))
print(min(scores))



