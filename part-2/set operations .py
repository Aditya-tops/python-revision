s = {"aditya","bony","dhwani","mahi"}
print("mahi" in s) #   True
print("kunal" in s) #  False

set1 = {1,2,3,4,5}
set2 = {4,5,7,8,9}

print(set1 | set2) #   union  {1, 2, 3, 4, 5, 7, 8, 9} is use to duplicat elements
print(set1 | set2) #   union  {1, 2, 3, 4, 5, 7, 8, 9} is use to duplicat elements
print(set1 & set2) #   intersection  {4, 5} is use to find common elements
print(set1 - set2) #   {1, 2, 3} 
print(set2 - set1) #   {8, 9, 7}
print(set2 ^ set1) #   {1, 2, 3, 7, 8, 9}


seta = {1,2,3,4,5}
seta.add(10)
print(seta) # {1, 2, 3, 4, 5, 10}
seta.remove(4)
print(seta) # {1, 2, 3, 5, 10}
seta.discard(2)
print(seta) # {1, 3, 5, 10}

#  seta.remove(20)
#  print(seta) # Error
seta.discard(20)
print(seta) # {1, 3, 5, 10}
print(seta.pop()) # 1

set_b = {2, 3, 4, 5, 10}
print(set_b.pop()) # 2


set_clear = {2, 3, 4, 5, 10}
set_clear.clear()
print(set_clear) # set()

