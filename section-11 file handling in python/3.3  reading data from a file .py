file = open('data.txt','r')  # r mean read

content = file.readline()
print(content)

file.close()
