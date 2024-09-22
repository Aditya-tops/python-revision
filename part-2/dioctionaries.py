people = { "bony":25,"kunal":22,"dhwani":20,}

print(people) # {'bony': 25, 'kunal': 22, 'dhwani': 20}
print(people["bony"]) # 25


people_id = { 1:"ford",2:'walton',3:"parker"}
print(people_id[2]) # walton

# mutable in dict
people['dhwani'] = 50
print(people) # {'bony': 25, 'kunal': 22, 'dhwani': 50}

employee = dict(dhwani=25000,mahi=30000,ayushi=15000)
print(employee) # {'dhwani': 25000, 'mahi': 30000, 'ayushi': 15000}

employee["aditya"]=50000
print(employee) # {'dhwani': 25000, 'mahi': 30000, 'ayushi': 15000, 'aditya': 50000}

del employee["dhwani"]
print(employee) # {'mahi': 30000, 'ayushi': 15000, 'aditya': 50000}
