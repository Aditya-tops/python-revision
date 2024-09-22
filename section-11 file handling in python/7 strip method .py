with open('data.txt','r') as file:
    #contents = file.readline()
    contents = file.readlines()

print(contents)
for line in contents:
    print(line.strip())
