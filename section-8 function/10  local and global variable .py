count = 10 
print("this is golable variable = ",count)

def add():
    count = 20
    print("this is local variable = ",count)

add()

print("---------------------------------")

def addd():
    count = 1
    print("this is local variable = ",count)

def subb():
    count = 2
    print("this is local variable = ",count)

addd()
subb()