import re 
string = "abc"
pattern = "ab*c" # a at the start c at the end 

if re.match(pattern,string):
    print("Match Found")
else:
    print('No Match Found')