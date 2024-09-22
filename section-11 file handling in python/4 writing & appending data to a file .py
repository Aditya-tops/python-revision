# file = open("data.txt",'w') write function is override a data
file = open("data.txt",'a') # a is append 
content = "\nthe is a third line"
file.write(content)
file.close()