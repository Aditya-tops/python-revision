numbers = ["1","2","3","4","5"]

new_list = list(map(int,numbers))
print(type(new_list))
print(new_list)

prices = [100,200,300,400,500]
new_liist = list(map(lambda x: x - x*5/100,prices))
print(new_liist)

names = [ 'bony','aditya','dhwani' ]
new_list3 = list(map(str.capitalize,names))
print(new_list3)
new_list4 = list(map(str.upper,names))
print(new_list4)




