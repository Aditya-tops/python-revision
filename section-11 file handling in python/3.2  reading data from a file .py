file = open('data.txt','r')  # r mean read

content = file.read(10) # .read(10) is read mode 10 meand only 10 words
print(content)

file.close()