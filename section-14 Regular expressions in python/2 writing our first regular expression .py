import re 
string = "abc"
pattern = "a"
#print(re.match(pattern,string))

if re.match(pattern,string):
    print("Match Found")
else:
    print('No Match Found')

