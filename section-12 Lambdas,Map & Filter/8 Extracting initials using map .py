'''
names = ["aditya patel","bony patel","kunal joshi"]
for name in names:
    print(name.split()[0])
'''
names = ["aditya patel","bony patel","kunal joshi"]

initials = list(map(lambda name: name,names))
print(initials)
print("----------------------------------------")
x = list(map(lambda name: name.split(),names))
print(x)
print("----------------------------------------")
y = list(map(lambda name:[n[0] for n in name.split()],names))
print(y)
print("----------------------------------------")
# using join method
z = list(map(lambda name: ''.join([n[0] for n in name.split()]), names))
print(z)



