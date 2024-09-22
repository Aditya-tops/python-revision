file = open('data.txt','r')  # r mean read

content = file.read() # .read() is read mode
print(content)

file.close()
